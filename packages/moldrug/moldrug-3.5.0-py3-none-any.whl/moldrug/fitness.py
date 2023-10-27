#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import deepcopy
from shutil import rmtree
from moldrug import utils, constraintconf, verbose
from rdkit import Chem
from rdkit.Chem import QED, Descriptors
import os
import numpy as np
from typing import Dict, List
# from warnings import import warn
from meeko import MoleculePreparation, PDBQTMolecule, RDKitMolCreate, PDBQTWriterLegacy

def __get_mol_cost(
    mol:Chem.rdchem.Mol,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:str = None,
    boxcenter:List[float] = None,
    boxsize:List[float] = None,
    score_only = True,
    desirability:Dict = None
    ):
    """
    This function is for developing. It calculate the cost of a single molecule.
    I use it for testing.

    Parameters
    ----------
    mol : Chem.rdchem.Mol
        The molecule to calculate the cost
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
         This is the name of the vina executable, could be a path to the binary object (absolute path is recommended),
         which must have  execution permits (chmod a+x <your binary file>), by default 'vina'
    receptor_pdbqt_path : str, optional
        Where the receptor pdbqt file is located, by default None
    boxcenter : List[float], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : List[float], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    score_only : bool, optional
        If True only a vina single point evaluation if not vina will perform optimization, by default True
    desirability : Dict, optional
        The definition of the desirability to use for each used variable = [qed, sa_score, vina_score].
        Each variable only will accept the keys [w, and the name of the desirability function of :meth:`moldrug.utils.DerringerSuichDesirability`],
        by default None which means that it will use
        desirability = {
        'qed':  {'w': 1,'LargerTheBest': {'LowerLimit': 0.1,'Target': 0.75,'r': 1}
        },
        'sa_score': {'w': 1,'SmallerTheBest': {'Target': 3,'UpperLimit': 7,'r': 1}
        },
        'vina_score': {'w': 1,'SmallerTheBest': {'Target': -12,'UpperLimit': -6,'r': 1}
        }
        }
    Returns
    -------
    dict
        A dict with the keywords:qed, vina_score, sa_score and cost.

    Raises
    ------
    RuntimeError
        Inconsistences on user definition of the desirability function parameters.
    """

    if not desirability:
        desirability = {
            'qed': {
                'w': 1,
                'LargerTheBest': {
                    'LowerLimit': 0.1,
                    'Target': 0.75,
                    'r': 1
                }
            },
            'sa_score': {
                'w': 1,
                'SmallerTheBest': {
                    'Target': 3,
                    'UpperLimit': 7,
                    'r': 1
                }
            },
            'vina_score': {
                'w': 1,
                'SmallerTheBest': {
                    'Target': -12,
                    'UpperLimit': -6,
                    'r': 1
                }
            }
        }

    if not os.path.exists(wd):
        os.makedirs(wd)
    # Initializing result dict
    results = dict()
    # Importing sascorer
    sascorer = utils.import_sascorer()
    # multicriteria optimization,Optimization of Several Response Variables

    # Getting estimate of drug-likness
    results['qed'] = QED.weights_mean(mol)

    # Getting synthetic accessibility score
    results['sa_score'] = sascorer.calculateScore(mol)

    # Getting vina_score and update pdbqt
    # Making the ligand pdbqt
    preparator = MoleculePreparation()
    mol_setups = preparator.prepare(Chem.AddHs(mol, addCoords=True))
    with open(os.path.join(os.path.join(wd, 'ligand.pdbqt')), 'w') as f:
        f.write(PDBQTWriterLegacy.write_string(mol_setups[0])[0])

    # If the vina_executable is a path
    if os.path.isfile(vina_executable):
        vina_executable = os.path.abspath(vina_executable)

    # Creating the command line for vina
    cmd_vina_str = f"{vina_executable} --receptor {receptor_pdbqt_path}"\
        f" --center_x {boxcenter[0]} --center_y {boxcenter[1]} --center_z {boxcenter[2]}"\
        f" --size_x {boxsize[0]} --size_y {boxsize[1]} --size_z {boxsize[2]}"\
        f" --ligand {os.path.join(wd, 'ligand.pdbqt')}"
    if score_only:
        cmd_vina_str += " --score_only"
    else:
        cmd_vina_str += f" --out {os.path.join(wd, 'ligand_out.pdbqt')}"
    cmd_vina_result = utils.run(cmd_vina_str)
    if score_only:
        for line in cmd_vina_result.stdout.split('\n'):
            # Check over different vina versions
            if line.startswith('Affinity'):
                results['vina_score'] = float(line.split()[1])
                break
            elif 'Estimated Free Energy of Binding' in line:
                results['vina_score'] = float(line.split(':')[1].split()[0])
                break
    else:
        best_energy = utils.VINA_OUT(os.path.join(wd, 'ligand_out.pdbqt')).BestEnergy()
        results['vina_score'] = best_energy.freeEnergy
        pdbqt_mol = PDBQTMolecule.from_file(os.path.join(wd, 'ligand_out.pdbqt'), skip_typing=True)
        with Chem.SDWriter(os.path.join(wd, 'ligand_out.sdf')) as w:
            w.write(RDKitMolCreate.from_pdbqt_mol(pdbqt_mol)[0])
    # Getting the desirability
    base = 1
    exponent = 0
    for variable in desirability:
        for key in desirability[variable]:
            if key == 'w':
                w = desirability[variable][key]
            elif key in utils.DerringerSuichDesirability():
                d = utils.DerringerSuichDesirability()[key](results[variable], **desirability[variable][key])
            else:
                raise RuntimeError(f"Inside the desirability dictionary you provided for the variable = {variable} a non implemented key = {key}. "\
                "Only are possible: 'w' (standing for weight) and any possible "\
                f"Derringer-Suich desirability function: {utils.DerringerSuichDesirability().keys()}")
        base *= d**w
        exponent += w

    # We are using a geometric mean. And because we are minimizing we have to return
    results['desirability'] = 1 - base**(1/exponent)
    return results

def _vinadock(
    Individual:utils.Individual,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:str = None,
    boxcenter:List[float] = None,
    boxsize:List[float] = None,
    exhaustiveness:int = 8,
    ad4map:str = None,
    ncores:int = 1,
    num_modes:int = 1,
    constraint:bool = False,
    constraint_type:str = 'score_only', # score_only, local_only
    constraint_ref:Chem.rdchem.Mol = None,
    constraint_receptor_pdb_path:str = None,
    constraint_num_conf:int = 100,
    constraint_minimum_conf_rms:int = 0.01):
    """
    This function is intend to be used to perform docking for all the cost functions implemented on :mod:`moldrug.fitness`
    If ad4map (available from moldrug-3.0.0) is set, the last version of vina (`releases <https://github.com/ccsb-scripps/AutoDock-Vina/releases>`_)
    must be installed. To see how to use AutoDock4 force fields in the new version of vina, follow
    `this tutorial <https://autodock-vina.readthedocs.io/en/latest/docking_zinc.html>_`

    Parameters
    ----------
    Individual : utils.Individual
        An Individual with the pdbqt attribute (only needed for non constraint docking).
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
        This is the name of the vina executable, could be a path to the binary object (absolute path is recommended),
        which must have  execution permits (chmod a+x <your binary file>), by default 'vina'
    receptor_pdbqt_path : str, optional
        Where the receptor pdbqt file is located, by default None
    boxcenter : List[float], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : List[float], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    exhaustiveness : int, optional
         Parameter of vina that controls the accuracy of the docking searching, by default 8
    ad4map : str, optional
        Affinity maps for the autodock4.2 (ad4) or vina scoring function, by default None
    ncores : int, optional
        Number of cpus to use in Vina, by default 1
    num_modes : int, optional
        How many modes should Vina export, by default 1
    constraint : bool, optional
        Controls if constraint docking will be perform, by default False
    constraint_type : str, optional
        This is the type of constraint docking. Could be local_only
        (vina will perform local optimization and score the resulted pose)
        or score_only (in this case the provided pose by the internal conformer
        generator will only be scored), by default 'score_only'
    constraint_ref : Chem.rdchem.Mol, optional
        The part of the molecule that we would like to constraint, by default None
    constraint_receptor_pdb_path : str, optional
        The same as constraint_receptor_pdbqt_path but in pdb format, by default None
    constraint_num_conf : int, optional
        Maximum number of conformer to be generated internally by MolDrug , by default 100
    constraint_minimum_conf_rms : int, optional
        RMS to filter duplicate conformers, by default 0.01

    Returns
    -------
    tuple
        A tuple with two elements:
        (vina score, pdbqt string)

    Raises
    ------
    Exception
        Inappropriate constraint_type. must be local_only or score_only. Only will be checked if constraint is set to True.
    """

    constraint_type = constraint_type.lower()

    # Creating the error directory if needed
    if not os.path.isdir('error'):
        os.makedirs('error')
    # Creating the working directory if needed
    if not os.path.exists(wd):
        os.makedirs(wd)

    # Converting to absolute path in case that vina_executable points to a file
    if os.path.isfile(vina_executable):
        vina_executable = os.path.abspath(vina_executable)
    # Creating the command line for vina
    cmd_vina_str = f"{vina_executable}"\
        f" --cpu {ncores} --exhaustiveness {exhaustiveness} --num_modes {num_modes}"

    if ad4map:
        cmd_vina_str += f" --scoring ad4 --maps {os.path.abspath(ad4map)}"
    else:
        cmd_vina_str += f" --receptor {os.path.abspath(receptor_pdbqt_path)}"\
            f" --center_x {boxcenter[0]} --center_y {boxcenter[1]} --center_z {boxcenter[2]}"\
            f" --size_x {boxsize[0]} --size_y {boxsize[1]} --size_z {boxsize[2]}"\

    if constraint:
        # Check for the correct type of docking
        if constraint_type in ['score_only', 'local_only']:
            cmd_vina_str += f" --{constraint_type}"
        else:
            raise Exception("constraint_type only admit two possible values: score_only, local_only.")

        # Generate constrained conformer
        try:
            out_mol = constraintconf.generate_conformers(
                mol = Chem.RemoveHs(Individual.mol),
                ref_mol = Chem.RemoveHs(constraint_ref),
                num_conf = constraint_num_conf,
                #ref_smi=Chem.MolToSmiles(constraint_ref),
                minimum_conf_rms=constraint_minimum_conf_rms)
        except Exception as e:
            # TODO I should add this kind of lines on the code. It is quite useful for debug
            if verbose:
                print(f"constraintconf.generate_conformers fails inside moldrug.fitness._vinadock with {e}")
            vina_score_pdbqt = (np.inf, "NonValidConformer")
            return vina_score_pdbqt
        # Remove conformers that clash with the protein in case of score_only, for local_only vina will handle the clash.
        if constraint_type == 'score_only':
            clash_filter = constraintconf.ProteinLigandClashFilter(protein_pdbpath = constraint_receptor_pdb_path, distance=1.5)
            clashIds = [conf.GetId() for conf in out_mol.GetConformers() if clash_filter(conf)]
            _ = [out_mol.RemoveConformer(clashId) for clashId in clashIds]

        # Check first if some valid conformer exist
        if len(out_mol.GetConformers()):
            vina_score_pdbqt = (np.inf, None)
            for conf in out_mol.GetConformers():
                temp_mol = deepcopy(out_mol)
                temp_mol.RemoveAllConformers()
                temp_mol.AddConformer(out_mol.GetConformer(conf.GetId()), assignId=True)

                preparator = MoleculePreparation()
                mol_setups = preparator.prepare(Chem.AddHs(temp_mol, addCoords=True))
                with open(os.path.join(wd, f'{Individual.idx}_conf_{conf.GetId()}.pdbqt'), 'w') as f:
                    f.write(PDBQTWriterLegacy.write_string(mol_setups[0])[0])

                # Make a copy to the vina command string and add the out (is needed) and ligand options
                cmd_vina_str_tmp = cmd_vina_str[:]
                cmd_vina_str_tmp += f" --ligand {os.path.join(wd, f'{Individual.idx}_conf_{conf.GetId()}.pdbqt')}"

                if constraint_type == 'local_only':
                    cmd_vina_str_tmp += f" --out {os.path.join(wd, f'{Individual.idx}_conf_{conf.GetId()}_out.pdbqt')}"
                try:
                    cmd_vina_result = utils.run(cmd_vina_str_tmp)
                except Exception as e:
                    if os.path.isfile(receptor_pdbqt_path):
                        with open(receptor_pdbqt_path, 'r') as f:
                            receptor_str = f.read()
                    else:
                        receptor_str = None

                    error = {
                        'Exception': e,
                        'Individual': Individual,
                        f'used_mol_conf_{conf.GetId()}': temp_mol,
                        f'used_ligand_pdbqt_conf_{conf.GetId()}': PDBQTWriterLegacy.write_string(mol_setups[0])[0],
                        'receptor_str': receptor_str,
                        'boxcenter': boxcenter,
                        'boxsize': boxsize,
                    }
                    utils.compressed_pickle(f'error/idx_{Individual.idx}_conf_{conf.GetId()}_error', error)
                    # warn(f"\nVina failed! Check: idx_{Individual.idx}_conf_{conf.GetId()}_error.pbz2 file in error.\n")
                    vina_score_pdbqt = (np.inf, PDBQTWriterLegacy.write_string(mol_setups[0])[0])
                    return vina_score_pdbqt

                vina_score = np.inf
                for line in cmd_vina_result.stdout.split('\n'):
                    # Check over different vina versions
                    if line.startswith('Affinity'):
                        vina_score = float(line.split()[1])
                        break
                    elif 'Estimated Free Energy of Binding' in line:
                        vina_score = float(line.split(':')[1].split()[0])
                        break
                if vina_score < vina_score_pdbqt[0]:
                    if constraint_type == 'local_only':
                        if os.path.isfile(os.path.join(wd, f'{Individual.idx}_conf_{conf.GetId()}_out.pdbqt')):
                            with open(os.path.join(wd, f'{Individual.idx}_conf_{conf.GetId()}_out.pdbqt'), 'r') as f:
                                pdbqt = f.read()
                        else:
                            pdbqt = "NonExistedFileToRead"
                        vina_score_pdbqt = (vina_score, pdbqt)
                    else:
                        vina_score_pdbqt = (vina_score, PDBQTWriterLegacy.write_string(mol_setups[0])[0])
        else:
            vina_score_pdbqt = (np.inf, "NonGenConformer")
    # "Normal" docking
    else:
        cmd_vina_str += f" --ligand {os.path.join(wd, f'{Individual.idx}.pdbqt')} --out {os.path.join(wd, f'{Individual.idx}_out.pdbqt')}"
        with open(os.path.join(wd, f'{Individual.idx}.pdbqt'), 'w') as lig_pdbqt:
            lig_pdbqt.write(Individual.pdbqt)
        try:
            utils.run(cmd_vina_str)
        except Exception as e:
            if os.path.isfile(receptor_pdbqt_path):
                with open(receptor_pdbqt_path, 'r') as f:
                    receptor_str = f.read()
            else:
                receptor_str = None

            error = {
                'Exception': e,
                'Individual': Individual,
                'receptor_str': receptor_str,
                'boxcenter': boxcenter,
                'boxsize': boxsize,
            }
            utils.compressed_pickle(f'error/{Individual.idx}_error', error)
            # warn(f"\nVina failed! Check: {Individual.idx}_error.pbz2 file in error.\n")

            vina_score_pdbqt = (np.inf, 'VinaFailed')
            return vina_score_pdbqt

        # Getting the information
        best_energy = utils.VINA_OUT(os.path.join(wd, f'{Individual.idx}_out.pdbqt')).BestEnergy()
        vina_score_pdbqt = (best_energy.freeEnergy, ''.join(best_energy.chunk))

    return vina_score_pdbqt

def Cost(
    Individual:utils.Individual,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:str = None,
    boxcenter:List[float] = None,
    boxsize:List[float] = None,
    exhaustiveness:int = 8,
    ad4map:str = None,
    ncores:int = 1,
    num_modes:int = 1,
    constraint:bool = False,
    constraint_type:str = 'score_only', # score_only, local_only
    constraint_ref:Chem.rdchem.Mol = None,
    constraint_receptor_pdb_path:str = None,
    constraint_num_conf:int = 100,
    constraint_minimum_conf_rms:int = 0.01,
    desirability:Dict = None,
    ):
    """
    This is the main Cost function of the module. It use the concept of desirability functions. The response variables are:

    #. `Vina score. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041641/>`_
    #. `Quantitative Estimation of Drug-likeness (QED). <https://www.nature.com/articles/nchem.1243>`_
    #. `Synthetic accessibility score.  <https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-1-8)>`_

    If ad4map is set, the last version of vina (`releases <https://github.com/ccsb-scripps/AutoDock-Vina/releases>`_)
    must be installed. To see how to use AutoDock4 force fields in the new version of vina, follow
    `this tutorial <https://autodock-vina.readthedocs.io/en/latest/docking_zinc.html>_`

    Parameters
    ----------
    Individual : utils.Individual
        A Individual with the pdbqt attribute
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
        This is the name of the vina executable, could be a path to the binary object (absolute path is recommended),
        which must have  execution permits (chmod a+x <your binary file>),  by default 'vina'
    receptor_pdbqt_path : str, optional
        Where the receptor pdbqt file is located, by default None
    boxcenter : list[float], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : list[float], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    exhaustiveness : int, optional
        Parameter of vina that controls the accuracy of the docking searching, by default 8
    ad4map : str, optional
        Affinity maps for the autodock4.2 (ad4) or vina scoring function, by default None
    ncores : int, optional
        Number of cpus to use in Vina, by default 1
    num_modes : int, optional
        How many modes should Vina export, by default 1
    constraint : bool, optional
        Controls if constraint docking will be perform, by default False
    constraint_type : str, optional
        This is the type of constraint docking.
        Could be local_only (vina will perform local optimization and score the resulted pose)
        or score_only (in this case the provided pose by the internal conformer generator will only be scored),
        by default 'score_only'
    constraint_ref : Chem.rdchem.Mol, optional
        The part of the molecule that we would like to constraint, by default None
    constraint_receptor_pdb_path : str, optional
        The same as constraint_receptor_pdbqt_path but in pdb format, by default None
    constraint_num_conf : int, optional
        Maximum number of conformer to be generated internally by MolDrug , by default 100
    constraint_minimum_conf_rms : int, optional
        RMS to filter duplicate conformers, by default 0.01
    desirability : dict, optional
        The definition of the desirability to use for each used variable = [qed, sa_score, vina_score].
        Each variable only will accept the keys [w, and the name of the desirability function of :meth:`moldrug.utils.DerringerSuichDesirability`],
        by default None which means that it will be used:
        desirability = {
        'qed': {'w': 1,'LargerTheBest': {'LowerLimit': 0.1,'Target': 0.75, 'r': 1}
        },
        'sa_score': {'w': 1,'SmallerTheBest': {'Target': 3,'UpperLimit': 7,'r': 1}
        },
        'vina_score': {'w': 1,'SmallerTheBest': {'Target': -12,'UpperLimit': -6,'r': 1}
        }
        }
    Returns
    -------
    utils.Individual
        A new instance of the original Individual with the the new attributes:
        pdbqt, qed, vina_score, sa_score and cost.
        cost attribute will be a number between 0 and 1, been 0 the optimal value.
    Example
    -------
    .. ipython:: python

        from moldrug import utils, fitness
        from rdkit import Chem
        import tempfile, os
        from moldrug.data import ligands, boxes, receptor_pdbqt
        tmp_path = tempfile.TemporaryDirectory()
        ligand_mol = Chem.MolFromSmiles(ligands.r_x0161)
        I = utils.Individual(ligand_mol)
        receptor_path = os.path.join(tmp_path.name,'receptor.pdbqt')
        with open(receptor_path, 'w') as r: r.write(receptor_pdbqt.r_x0161)
        box = boxes.r_x0161['A']
        # Using the default desirability
        NewI = fitness.Cost(
            Individual = I,wd = tmp_path.name,
            receptor_pdbqt_path = receptor_path,boxcenter = box['boxcenter'],
            boxsize = box['boxsize'],exhaustiveness = 4,ncores = 4)
        print(NewI.cost, NewI.vina_score, NewI.qed, NewI.sa_score)
    """
    if not desirability:
        desirability = {
            'qed': {
                'w': 1,
                'LargerTheBest': {
                    'LowerLimit': 0.1,
                    'Target': 0.75,
                    'r': 1
                }
            },
            'sa_score': {
                'w': 1,
                'SmallerTheBest': {
                    'Target': 3,
                    'UpperLimit': 7,
                    'r': 1
                }
            },
            'vina_score': {
                'w': 1,
                'SmallerTheBest': {
                    'Target': -12,
                    'UpperLimit': -6,
                    'r': 1
                }
            }
        }

    sascorer = utils.import_sascorer()
    # multicriteria optimization,Optimization of Several Response Variables
    # Getting estimate of drug-likness
    Individual.qed = QED.weights_mean(Individual.mol)

    # Getting synthetic accessibility score
    Individual.sa_score = sascorer.calculateScore(Individual.mol)

    # Getting vina_score and update pdbqt
    Individual.vina_score, Individual.pdbqt = _vinadock(
        Individual = Individual,
        wd = wd,
        vina_executable = vina_executable,
        receptor_pdbqt_path =  receptor_pdbqt_path,
        boxcenter = boxcenter,
        boxsize = boxsize,
        exhaustiveness = exhaustiveness,
        ad4map = ad4map,
        ncores = ncores,
        num_modes = num_modes,
        constraint = constraint,
        constraint_type = constraint_type,
        constraint_ref = constraint_ref,
        constraint_receptor_pdb_path = constraint_receptor_pdb_path,
        constraint_num_conf = constraint_num_conf,
        constraint_minimum_conf_rms = constraint_minimum_conf_rms,
    )
    # Adding the cost using all the information of qed, sas and vina_cost
    # Construct the desirability
    # Quantitative estimation of drug-likeness (ranges from 0 to 1). We could use just the value perse, but using LargerTheBest we are more permissible.

    base = 1
    exponent = 0
    for variable in desirability:
        for key in desirability[variable]:
            if key == 'w':
                w = desirability[variable][key]
            elif key in utils.DerringerSuichDesirability():
                d = utils.DerringerSuichDesirability()[key](getattr(Individual, variable), **desirability[variable][key])
            else:
                raise RuntimeError(f"Inside the desirability dictionary you provided for the variable = {variable} "\
                f"a non implemented key = {key}. Only are possible: 'w' (standing for weight) and any "\
                f"possible Derringer-Suich desirability function: {utils.DerringerSuichDesirability().keys()}")
        base *= d**w
        exponent += w

    # We are using a geometric mean. And because we are minimizing we have to return
    Individual.cost = 1 - base**(1/exponent)
    return Individual

def CostOnlyVina(
    Individual:utils.Individual,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:str = None,
    boxcenter:List[float] = None,
    boxsize:List[float] = None,
    exhaustiveness:int = 8,
    ad4map:str = None,
    ncores:int = 1,
    num_modes:int = 1,
    constraint:bool = False,
    constraint_type:str = 'score_only', # score_only, local_only
    constraint_ref:Chem.rdchem.Mol = None,
    constraint_receptor_pdb_path:str = None,
    constraint_num_conf:int = 100,
    constraint_minimum_conf_rms:int = 0.01,
    wt_cutoff:float = None,
    ):
    """
    This Cost function performs Docking and return the vina_score as Cost.

    Parameters
    ----------
    Individual : utils.Individual
        A Individual with the pdbqt attribute
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
        This is the name of the vina executable, could be a path to the binary object (absolute path is recommended),
        which must have  execution permits (chmod a+x <your binary file>),  by default 'vina'
    receptor_path : str, optional
        Where the receptor pdbqt file is located, by default None
    boxcenter : list[float], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : list[float], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    exhaustiveness : int, optional
        Parameter of vina that controls the accuracy of the docking searching, by default 8
    ad4map : str, optional
        Affinity maps for the autodock4.2 (ad4) or vina scoring function, by default None
    ncores : int, optional
        Number of cpus to use in Vina, by default 1
    num_modes : int, optional
        How many modes should Vina export, by default 1
    constraint : bool, optional
        Controls if constraint docking will be perform, by default False
    constraint_type : str, optional
        This is the type of constraint docking.
        Could be local_only (vina will perform local optimization and score the resulted pose)
        or score_only (in this case the provided pose by the internal conformer generator will only be scored),
        by default 'score_only'
    constraint_ref : Chem.rdchem.Mol, optional
        The part of the molecule that we would like to constraint, by default None
    constraint_receptor_pdb_path : str, optional
        The same as constraint_receptor_pdbqt_path but in pdb format, by default None
    constraint_num_conf : int, optional
        Maximum number of conformer to be generated internally by MolDrug , by default 100
    constraint_minimum_conf_rms : int, optional
        RMS to filter duplicate conformers, by default 0.01
    wt_cutoff : float, optional
        If some number is provided the molecules with a molecular weight higher
        than wt_cutoff will get as vina_score = cost = np.inf. Vina will not be invoked, by default None
    Returns
    -------
    utils.Individual
        A new instance of the original Individual with the the new attributes:
        pdbqt, vina_score and cost. In this case cost = vina_score,
        the lowest the values the best individual.
    Example
    -------
    .. ipython:: python

        from moldrug import utils, fitness
        from rdkit import Chem
        import tempfile, os
        from moldrug.data import ligands, boxes, receptor_pdbqt
        tmp_path = tempfile.TemporaryDirectory()
        ligand_mol = Chem.MolFromSmiles(ligands.r_x0161)
        I = utils.Individual(ligand_mol)
        receptor_path = os.path.join(tmp_path.name,'receptor.pdbqt')
        with open(receptor_path, 'w') as r: r.write(receptor_pdbqt.r_x0161)
        box = boxes.r_x0161['A']
        NewI = fitness.CostOnlyVina(
            Individual = I,wd = tmp_path.name,receptor_pdbqt_path = receptor_path,
            boxcenter = box['boxcenter'],boxsize = box['boxsize'],
            exhaustiveness = 4,ncores = 4)
        print(NewI.cost, NewI.vina_score)
    """
    # If the molecule is heavy, don't perform docking and assign infinite to the cost attribute. Add the pdbqt to pdbqts and np.inf to vina_scores
    if wt_cutoff:
        if Descriptors.MolWt(Individual.mol) > wt_cutoff:
            Individual.vina_score = np.inf
            Individual.cost = np.inf
            Individual.pdbqt = 'TooHeavy'
            return Individual

    # Getting vina_score and update pdbqt
    Individual.vina_score, Individual.pdbqt = _vinadock(
        Individual = Individual,
        wd = wd,
        vina_executable = vina_executable,
        receptor_pdbqt_path =  receptor_pdbqt_path,
        boxcenter = boxcenter,
        boxsize = boxsize,
        exhaustiveness = exhaustiveness,
        ad4map = ad4map,
        ncores = ncores,
        num_modes = num_modes,
        constraint = constraint,
        constraint_type = constraint_type,
        constraint_ref = constraint_ref,
        constraint_receptor_pdb_path = constraint_receptor_pdb_path,
        constraint_num_conf = constraint_num_conf,
        constraint_minimum_conf_rms = constraint_minimum_conf_rms,
    )
    Individual.cost = Individual.vina_score
    return Individual

def CostMultiReceptors(
    Individual:utils.Individual,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:List[str] = None,
    vina_score_type:List[str] = None,
    boxcenter:List[List[float]] = None,
    boxsize:List[List[float]] = None,
    exhaustiveness:int = 8,
    ad4map:List[str] = None,
    ncores:int = 1,
    num_modes:int = 1,
    constraint:bool = False,
    constraint_type:str = 'score_only', # score_only, local_only
    constraint_ref:Chem.rdchem.Mol = None,
    constraint_receptor_pdb_path:List[str] = None,
    constraint_num_conf:int = 100,
    constraint_minimum_conf_rms:int = 0.01,
    desirability:Dict = None
    ):
    """
    This function is similar to :meth:`moldrug.fitness.Cost` but it will add the possibility
    to work with more than one receptor. It also use the concept of desirability and the response variables are:

    #. `Vina scores. <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041641/>`_
    #. `Quantitative Estimation of Drug-likeness (QED). <https://www.nature.com/articles/nchem.1243>`_
    #. `Synthetic accessibility score.  <https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-1-8)>`_

    In this case every vina score (for all the provided receptors) will be used for the construction of the desirability.

    If ad4map is set, the last version of vina (`releases <https://github.com/ccsb-scripps/AutoDock-Vina/releases>`_)
    must be installed. To see how to use AutoDock4 force fields in the new version of vina, follow
    `this tutorial <https://autodock-vina.readthedocs.io/en/latest/docking_zinc.html>_`

    Parameters
    ----------
    Individual : utils.Individual
        A Individual with the pdbqt attribute
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
        This is the name of the vina executable, could be a path to the binary object (absolute path is recommended),
        which must have  execution permits (chmod a+x <your binary file>), by default 'vina'
    receptor_pdbqt_path : list[str], optional
        A list of location of the receptors pdbqt files, by default None
    vina_score_type : list[str], optional
        This is a list with the keywords 'min' and/or 'max'. E.g.
        If two receptor were provided and for the first one we would like to find a minimum in the vina scoring function
        and for the other one a maximum (selectivity for the first receptor); we must provided the list: ['min', 'max'], by default None
    boxcenter : list[list[float]], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : list[list[float]], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    exhaustiveness : int, optional
        Parameter of vina that controls the accuracy of the docking searching, by default 8
    ad4map : list[str], optional
        A list of affinity maps for the autodock4.2 (ad4) or vina scoring function.
        For every receptor you should have a separate directory with all the maps, by default None
    ncores : int, optional
         Number of cpus to use in Vina, by default 1
    num_modes : int, optional
        How many modes should Vina export, by default 1
    constraint : bool, optional
        Controls if constraint docking will be perform, by default False
    constraint_type : str, optional
        This is the type of constraint docking.
        Could be local_only (vina will perform local optimization and score the resulted pose) or
        score_only (in this case the provided pose by the internal conformer generator will only be scored),
        by default 'score_only'
    constraint_ref : Chem.rdchem.Mol, optional
        The part of the molecule that we would like to constraint, by default None
    constraint_receptor_pdb_path : list[str], optional
        The same as constraint_receptor_pdbqt_path but in pdb format, by default None
    constraint_num_conf : int, optional
        Maximum number of conformer to be generated internally by MolDrug , by default 100
    constraint_minimum_conf_rms : int, optional
        RMS to filter duplicate conformers, by default 0.01
    desirability : dict, optional
        The definition of the desirability to use for each used variable = [qed, sa_score, vina_scores].
        Each variable only will accept the keys [w, and the name of the desirability function of :meth:`moldrug.utils.DerringerSuichDesirability`].
        In the case of vina_scores there is another layer for the vina_score_type= [min, max],
        by default is None which means that it will use:
        desirability = {
        'qed': {
        'w': 1,'LargerTheBest': {'LowerLimit': 0.1,'Target': 0.75,'r': 1}
        },
        'sa_score': {
        'w': 1,'SmallerTheBest': {'Target': 3,'UpperLimit': 7,'r': 1}
        },
        'vina_scores': {
        'min':{'w': 1,'SmallerTheBest': {'Target': -12,'UpperLimit': -6,'r': 1}},
        'max':{'w': 1,'LargerTheBest': {'LowerLimit': -4,'Target': 0,'r': 1}}
        }
        }

    Returns
    -------
    utils.Individual
        A new instance of the original Individual with the the new attributes:
        pdbqts [a list of pdbqt], qed, vina_scores[a list of vina_score], sa_score and cost.
        cost attribute will be a number between 0 and 1, been 0 the optimal value.

    Example
    -------
    .. ipython:: python

        from moldrug import utils, fitness
        from rdkit import Chem
        import tempfile, os
        from moldrug.data import ligands, boxes, receptor_pdbqt
        tmp_path = tempfile.TemporaryDirectory()
        ligand_mol = Chem.MolFromSmiles(ligands.r_x0161)
        I = utils.Individual(ligand_mol)
        receptor_paths = [os.path.join(tmp_path.name,'receptor1.pdbqt'),os.path.join(tmp_path.name,'receptor2.pdbqt')]
        with open(receptor_paths[0], 'w') as r: r.write(receptor_pdbqt.r_x0161)
        with open(receptor_paths[1], 'w') as r: r.write(receptor_pdbqt.r_6lu7)
        boxcenter = [boxes.r_x0161['A']['boxcenter'], boxes.r_6lu7['A']['boxcenter']]
        boxsize = [boxes.r_x0161['A']['boxsize'], boxes.r_6lu7['A']['boxsize']]
        vina_score_type = ['min', 'max']
        # Using the default desirability
        NewI = fitness.CostMultiReceptors(
            Individual = I,
            wd = tmp_path.name,receptor_pdbqt_path = receptor_paths,
            vina_score_type = vina_score_type, boxcenter = boxcenter,boxsize = boxsize,exhaustiveness = 4,ncores = 4)
        print(NewI.cost, NewI.vina_score, NewI.qed, NewI.sa_score)
    """
    if not desirability:
        desirability = {
            'qed': {
                'w': 1,
                'LargerTheBest': {
                    'LowerLimit': 0.1,
                    'Target': 0.75,
                    'r': 1
                }
            },
            'sa_score': {
                'w': 1,
                'SmallerTheBest': {
                    'Target': 3,
                    'UpperLimit': 7,
                    'r': 1
                }
            },
            'vina_scores': {
                'min':{
                    'w': 1,
                    'SmallerTheBest': {
                        'Target': -12,
                        'UpperLimit': -6,
                        'r': 1
                    }
                },
                'max':{
                    'w': 1,
                    'LargerTheBest': {
                        'LowerLimit': -4,
                        'Target': 0,
                        'r': 1
                    }
                }
            }
        }

    if not ad4map:
        ad4map = [None]*len(receptor_pdbqt_path)

    sascorer = utils.import_sascorer()
    Individual.qed = QED.weights_mean(Individual.mol)

    # Getting synthetic accessibility score
    Individual.sa_score = sascorer.calculateScore(Individual.mol)

    # Getting Vina score
    pdbqt_list = []
    Individual.vina_score = []
    for (i, _) in enumerate(receptor_pdbqt_path):
        # Getting vina_score and update pdbqt
        if constraint:
            vina_score, pdbqt = _vinadock(
                Individual = Individual,
                wd = wd,
                vina_executable = vina_executable,
                receptor_pdbqt_path =  receptor_pdbqt_path[i],
                boxcenter = boxcenter[i],
                boxsize = boxsize[i],
                exhaustiveness = exhaustiveness,
                ad4map = ad4map[i],
                ncores = ncores,
                num_modes = num_modes,
                constraint = constraint,
                constraint_type = constraint_type,
                constraint_ref = constraint_ref,
                constraint_receptor_pdb_path = constraint_receptor_pdb_path[i],
                constraint_num_conf = constraint_num_conf,
                constraint_minimum_conf_rms = constraint_minimum_conf_rms,
            )
        else:
            vina_score, pdbqt = _vinadock(
                Individual = Individual,
                wd = wd,
                vina_executable = vina_executable,
                receptor_pdbqt_path =  receptor_pdbqt_path[i],
                boxcenter = boxcenter[i],
                boxsize = boxsize[i],
                exhaustiveness = exhaustiveness,
                ad4map = ad4map[i],
                ncores = ncores,
                num_modes = num_modes,
            )
        Individual.vina_score.append(vina_score)
        pdbqt_list.append(pdbqt)
    # Update the pdbqt attribute
    Individual.pdbqt = pdbqt_list

    # make a copy of the default values of desirability
    # pops the region of vina_scores
    desirability_to_work_with = desirability.copy()
    vina_desirability_section = desirability_to_work_with.pop('vina_scores')
    # Initialize base and exponent
    base = 1
    exponent = 0
    # Runs for all properties different to vina_scores
    for variable in desirability_to_work_with:
        for key in desirability_to_work_with[variable]:
            if key == 'w':
                w = desirability_to_work_with[variable][key]
            elif key in utils.DerringerSuichDesirability():
                d = utils.DerringerSuichDesirability()[key](getattr(Individual, variable), **desirability_to_work_with[variable][key])
            else:
                raise RuntimeError(f"Inside the desirability dictionary you provided for the variable = {variable} "\
                    f"a non implemented key = {key}. Only are possible: 'w' (standing for weight) and "\
                    f"any possible Derringer-Suich desirability function: {utils.DerringerSuichDesirability().keys()}. "\
                    "Only in the case of vina_scores [min and max] keys")
        base *= d**w
        exponent += w

    # Run only for vina_scores
    for vs, vst in zip(Individual.vina_score, vina_score_type):
        for key in vina_desirability_section[vst]:
            if key == 'w':
                w = vina_desirability_section[vst][key]
            elif key in utils.DerringerSuichDesirability():
                d = utils.DerringerSuichDesirability()[key](vs, **vina_desirability_section[vst][key])
            else:
                raise RuntimeError(f"Inside the desirability dictionary you provided for the variable = vina_scores[{vst}] "\
                    f"a non implemented key = {key}. Only are possible: 'w' (standing for weight) and "\
                    f"any possible Derringer-Suich desirability function: {utils.DerringerSuichDesirability().keys()}.")
        base *= d**w
        exponent += w

    # We are using a geometric mean. And because we are minimizing we have to return
    Individual.cost = 1 - base**(1/exponent)
    return Individual

def CostMultiReceptorsOnlyVina(
    Individual:utils.Individual,
    wd:str = '.vina_jobs',
    vina_executable:str = 'vina',
    receptor_pdbqt_path:List[str] = None,
    vina_score_type:List[str] = None,
    boxcenter:List[List[float]] = None,
    boxsize:List[List[float]] = None,
    exhaustiveness:int = 8,
    ad4map:List[str] = None,
    ncores:int = 1,
    num_modes:int = 1,
    constraint:bool = False,
    constraint_type:str = 'score_only', # score_only, local_only
    constraint_ref:Chem.rdchem.Mol = None,
    constraint_receptor_pdb_path:List[str] = None,
    constraint_num_conf:int = 100,
    constraint_minimum_conf_rms:int = 0.01,
    desirability:Dict = None,
    wt_cutoff = None,
    ):
    """
    This function is similar to :meth:`moldrug.fitness.
    CostOnlyVina` but it will add the possibility to work with more than one receptor.
    It also use the concept of desirability.
    The response variables are the vina scores on each receptor.

    If ad4map is set, the last version of vina (`releases <https://github.com/ccsb-scripps/AutoDock-Vina/releases>`_)
    must be installed. To see how to use AutoDock4 force fields in the new version of vina, follow
    `this tutorial <https://autodock-vina.readthedocs.io/en/latest/docking_zinc.html>_`

    Parameters
    ----------
    Individual : utils.Individual
        A Individual with the pdbqt attribute
    wd : str, optional
        The working directory to execute the docking jobs, by default '.vina_jobs'
    vina_executable : str, optional
        This is the name of the vina executable, could be a path to the binary object (absolute path is recommended), which must have
        execution permits (chmod a+x <your binary file>), by default 'vina'
    receptor_pdbqt_path : list[str], optional
        A list of location of the receptors pdbqt files, by default None
    vina_score_type : list[str], optional
        This is a list with the keywords 'min' and/or 'max'. E.g.
        If two receptor were provided and for the first one we would like to find a minimum in the vina scoring function
        and for the other one a maximum (selectivity for the first receptor); we must provided the list: ['min', 'max'], by default None
    boxcenter : list[float], optional
        A list of three floats with the definition of the center of the box in angstrom for docking (x, y, z), by default None
    boxsize : list[float], optional
        A list of three floats with the definition of the box size in angstrom of the docking box (x, y, z), by default None
    exhaustiveness : int, optional
        Parameter of vina that controls the accuracy of the docking searching, by default 8
    ad4map : list[str], optional
        A list of affinity maps for the autodock4.2 (ad4) or vina scoring function.
        For every receptor you should have a separate directory with all the maps, by default None
    ncores : int, optional
         Number of cpus to use in Vina, by default 1
    num_modes : int, optional
        How many modes should Vina export, by default 1
    constraint : bool, optional
        Controls if constraint docking will be perform, by default False
    constraint_type : str, optional
        This is the type of constraint docking.
        Could be local_only (vina will perform local optimization and score the resulted pose)
        or score_only (in this case the provided pose by the internal conformer generator will only be scored),
        by default 'score_only'
    constraint_ref : Chem.rdchem.Mol, optional
        The part of the molecule that we would like to constraint, by default None
    constraint_receptor_pdb_path : list[str], optional
        The same as constraint_receptor_pdbqt_path but in pdb format, by default None
    constraint_num_conf : int, optional
        Maximum number of conformer to be generated internally by MolDrug , by default 100
    constraint_minimum_conf_rms : int, optional
        RMS to filter duplicate conformers, by default 0.01
    desirability : dict, optional
        The definition of the desirability when min or max is used.
        Each variable only will accept the keys [w, and the name of the desirability function of :meth:`moldrug.utils.DerringerSuichDesirability`].
        by default None, which means that it will be used:
        desirability = {
        'min': {'w': 1,'SmallerTheBest': {'Target': -12,'UpperLimit': -6,'r': 1}
        },
        'max': {'w': 1,'LargerTheBest': {'LowerLimit': -4,'Target': 0,'r': 1}
        }
        }
    wt_cutoff : float, optional
        If some number is provided,
        the molecules with a molecular weight higher than wt_cutoff
        will get as vina_score = cost = np.inf. Vina will not be invoked, by default None

    Returns
    -------
    utils.Individual
        A new instance of the original Individual with the the new attributes:
        pdbqts [a list of pdbqt], vina_scores [a list of vina_score], and cost.
        cost attribute will be a number between 0 and 1, been 0 the optimal value.
    Example
    -------
    .. ipython:: python

        from moldrug import utils, fitness
        from rdkit import Chem
        import tempfile, os
        from moldrug.data import ligands, boxes, receptor_pdbqt
        tmp_path = tempfile.TemporaryDirectory()
        ligand_mol = Chem.MolFromSmiles(ligands.r_x0161)
        I = utils.Individual(ligand_mol)
        receptor_paths = [os.path.join(tmp_path.name,'receptor1.pdbqt'),os.path.join(tmp_path.name,'receptor2.pdbqt')]
        with open(receptor_paths[0], 'w') as r: r.write(receptor_pdbqt.r_x0161)
        with open(receptor_paths[1], 'w') as r: r.write(receptor_pdbqt.r_6lu7)
        boxcenter = [boxes.r_x0161['A']['boxcenter'], boxes.r_6lu7['A']['boxcenter']]
        boxsize = [boxes.r_x0161['A']['boxsize'], boxes.r_6lu7['A']['boxsize']]
        vina_score_type = ['min', 'max']
        # Using the default desirability
        NewI = fitness.CostMultiReceptorsOnlyVina(
            Individual = I,wd = tmp_path.name,receptor_pdbqt_path = receptor_paths,
            vina_score_type = vina_score_type, boxcenter = boxcenter,boxsize = boxsize,
            exhaustiveness = 4,ncores = 4)
        print(NewI.cost, NewI.vina_score)
    """
    if not desirability:
        desirability = {
            'min':{
                'w': 1,
                'SmallerTheBest': {
                    'Target': -12,
                    'UpperLimit': -6,
                    'r': 1
                }
            },
            'max':{
                'w': 1,
                'LargerTheBest': {
                    'LowerLimit': -4,
                    'Target': 0,
                    'r': 1
                }
            }
        }

    pdbqt_list = []
    Individual.vina_score = []

    if not ad4map:
        ad4map = [None]*len(receptor_pdbqt_path)

    # If the molecule is heavy, don't perform docking and assign infinite to the cost attribute. Add "TooHeavy" string to pdbqts and np.inf to vina_scores
    if wt_cutoff:
        if Descriptors.MolWt(Individual.mol) > wt_cutoff:
            for _ in receptor_pdbqt_path:
                pdbqt_list.append('TooHeavy')
                Individual.vina_score.append(np.inf)
            Individual.cost = np.inf
            # Update the pdbqt attribute
            Individual.pdbqt = pdbqt_list
            return Individual

    # Getting Vina score
    pdbqt_list = []
    Individual.vina_score = []
    for (i, _) in enumerate(receptor_pdbqt_path):
        # Getting vina_score and update pdbqt
        if constraint:
            vina_score, pdbqt = _vinadock(
                Individual = Individual,
                wd = wd,
                vina_executable = vina_executable,
                receptor_pdbqt_path =  receptor_pdbqt_path[i],
                boxcenter = boxcenter[i],
                boxsize = boxsize[i],
                exhaustiveness = exhaustiveness,
                ad4map = ad4map[i],
                ncores = ncores,
                num_modes = num_modes,
                constraint = constraint,
                constraint_type = constraint_type,
                constraint_ref = constraint_ref,
                constraint_receptor_pdb_path = constraint_receptor_pdb_path[i],
                constraint_num_conf = constraint_num_conf,
                constraint_minimum_conf_rms = constraint_minimum_conf_rms,
            )
        else:
            vina_score, pdbqt = _vinadock(
                Individual = Individual,
                wd = wd,
                vina_executable = vina_executable,
                receptor_pdbqt_path =  receptor_pdbqt_path[i],
                boxcenter = boxcenter[i],
                boxsize = boxsize[i],
                exhaustiveness = exhaustiveness,
                ad4map = ad4map[i],
                ncores = ncores,
                num_modes = num_modes,
            )
        Individual.vina_score.append(vina_score)
        pdbqt_list.append(pdbqt)
    # Update the pdbqt attribute
    Individual.pdbqt = pdbqt_list

    # Initialize base and exponent
    base = 1
    exponent = 0
    # Run for vina_scores
    for vs, vst in zip(Individual.vina_score, vina_score_type):
        for key in desirability[vst]:
            if key == 'w':
                w = desirability[vst][key]
            elif key in utils.DerringerSuichDesirability():
                d = utils.DerringerSuichDesirability()[key](vs, **desirability[vst][key])
            else:
                raise RuntimeError(f"Inside the desirability dictionary you provided for the variable = vina_scores[{vst}] "\
                f"a non implemented key = {key}. "\
                "Only are possible: 'w' (standing for weight) "\
                f"and any possible Derringer-Suich desirability function: {utils.DerringerSuichDesirability().keys()}.")
        base *= d**w
        exponent += w

    # We are using a geometric mean. And because we are minimizing we have to return
    Individual.cost = 1 - base**(1/exponent)
    return Individual


if __name__ == '__main__':
    pass