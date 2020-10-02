import os
import re
import pandas as pd
import numpy as np
import pymatgen as mg


def categorize_phases(row):
    '''Creates BCC/FCC/other classifier used for visualizations'''
    
    if row['PROPERTY: Type of phases'] == 'BCC':
        val = 'BCC'
    elif row['PROPERTY: Type of phases'] == 'FCC':
        val = 'FCC'
    else:
        val = 'other'
    return val


def remove_uncertainty(cell):
    '''Sanitizes values given as range '''
    
    val = str(cell)
    
    if '$\pm$' in str(cell):
        val = cell.split('$\pm$')[0]
    if '>' in val:
        val = val.replace('>', '')
    if '<' in val:
        val = val.replace('<', '')
    if 'nan' in val:
        val = ''
        
    return val


def average_range(cell):
    '''Returns average if given range of values.'''
    
    val = str(cell).replace(" ", "")
    
    if re.findall(r"\b\d+-\d+\b", val):
        data = [float(x) for x in val.split('-')]
        val = np.average(data)
        
    return val


def neg_elongation(row):
    '''Assigns a negative sign for compression data. Used for visualization purposes.'''
    
    if row['PROPERTY: Type of test'].strip() == "C" and row['PROPERTY: Elongation (%)'] != "":
        val = -float(row['PROPERTY: Elongation (%)'])
    else:
        val = float(row['PROPERTY: Elongation (%)'])
    return val


def normalize_and_alphabetize_formula(formula):
    '''Normalizes composition labels. Used to enable matching / groupby on compositions.'''
    
    if formula:
        try:
            comp = mg.Composition(formula)
            weights = [comp.get_atomic_fraction(ele) for ele in comp.elements]
            normalized_weights = [round(w/max(weights), 3) for w in weights]
            normalized_comp = "".join([str(x)+str(y) for x,y in zip(comp.elements, normalized_weights)])
            
            return mg.Composition(normalized_comp).alphabetical_formula
        except:
            print("INVALID: ", formula)
            return None
    else:
        return None
    
def standardize_synthesis_method(synth_method):
    '''Standardizes synthesis method strings.'''
    
    return synth_method.replace(" ", "")


def calculate_density(formula):
    '''Calculates densisty based on Rule of Mixtures (ROM).'''
    
    comp = mg.Composition(formula)
    
    weights = [comp.get_atomic_fraction(e)for e in comp.elements]
    vols = np.array([e.molar_volume for e in comp.elements])
    atomic_masses = np.array([e.atomic_mass for e in comp.elements])
    
    val = np.sum(weights*atomic_masses) / np.sum(weights*vols)

    return round(val, 1)


def calculate_youngs_modulus(formula):
    '''Calculates Young Modulus based on Rule of Mixtures (ROM).'''
    
    comp = mg.Composition(formula)
    
    weights = np.array([comp.get_atomic_fraction(e)for e in comp.elements])
    vols = np.array([e.molar_volume for e in comp.elements])
    ym_vals = np.array([e.youngs_modulus for e in comp.elements])
    
    if None in ym_vals:
        return ''
    
    val = np.sum(weights*vols*ym_vals) / np.sum(weights*vols)
    
    return int(round(val, 0))


def classify_processing_method(process_method):
    '''Creates a processing method classifier based on recorded synthesis method.'''
    
    if process_method == 'AC' or process_method == 'DC':
        return 'CAST'
    
    if 'SPD' in process_method or 'AM' in process_method or 'HIP' in process_method:
        return 'OTHER'
    
    if 'GA' in process_method or 'MA' in process_method or 'SPS' in process_method or 'VHP' in process_method or process_method == 'S':
        return 'POWDER'
    
    if 'CR' in process_method or 'HR' in process_method or 'HF' in process_method:
        return 'WROUGHT'
    
    if process_method == 'A' or process_method == 'H' or '+A' in process_method or '+H' in process_method or 'Aged' in process_method:
        return 'ANNEAL'


def classify_microstructure(phases):
    '''Creates a microstructure classifier based on recorded phases.'''
    
    phases = phases.replace(' ', '')
    
    valid_phases = ['FCC', 'BCC', 'HCP', 'L12', 'B2', 'Laves', 'Laves (C14)', 'Laves (C15)']
    
    if phases == '':
        return ''
    
    phase_list = phases.split('+')
    
    if len(phase_list) == 1 and phase_list[0] in valid_phases:
        return phases
    elif len(phase_list) == 1 and phase_list[0] not in valid_phases:
        return 'Other'
    
    if len(phase_list) > 1 and len(set(phase_list)) == 1 and phase_list[0] in valid_phases:
        return phases
    elif len(phase_list) > 1 and len(set(phase_list)) == 1 and phase_list[0] not in valid_phases:
        return 'Other'
    
    if len(phase_list) > 1 and len(set(phase_list)) > 1 and phase_list[0] in valid_phases:

        
        # if all phases are a subset of valid phases, return all phases
        if set(phase_list).issubset(set(valid_phases)):
            return phases
        else:
            sub_valid = []
            for phase in phase_list:
                if phase in valid_phases:
                    sub_valid.append(phase)
            
            # return valid phases + invalid labeled as "Sec."
            if len(sub_valid) > 0:
                return '+'.join(sub_valid)+"+Sec."
           
            # no valid phases
            else:
                return 'Other'
    else:
        return 'Other'