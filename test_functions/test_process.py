import os
import sys
import numpy as np
import pandas as pd

p = os.path.abspath('../')
if p not in sys.path:
    sys.path.append(p)

from utils import *


def test_categorize_phases():
    assert categorize_phases({'PROPERTY: Type of phases':'BCC'}) =='BCC'
    assert categorize_phases({'PROPERTY: Type of phases':'BCC+FCC'}) =='other'

    
    
def test_remove_uncertainty():
    assert remove_uncertainty('2$\pm$5') == '2'
    assert remove_uncertainty('>2') == '2'
    assert remove_uncertainty('<2') == '2'
    
    
def test_average_range():
    assert average_range('2-5') == 3.5
    assert average_range(' 2 - 5 ') == 3.5
    
    
def test_neg_elongation():
    assert neg_elongation({'PROPERTY: Type of test':'C ', 'PROPERTY: Elongation (%)':'30'}) == -30
    assert neg_elongation({'PROPERTY: Type of test':'T', 'PROPERTY: Elongation (%)':'30'}) == 30
    
    
def test_normalize_and_alphabetize_formula():
    assert normalize_and_alphabetize_formula('HfNbTaTiZr') == 'Hf1 Nb1 Ta1 Ti1 Zr1'
    assert normalize_and_alphabetize_formula('ZrHfTaNbTi') == 'Hf1 Nb1 Ta1 Ti1 Zr1'
    assert normalize_and_alphabetize_formula('Fex') == None
    
    
def test_standardize_synthesis_method():
    assert standardize_synthesis_method("AC + A ") == 'AC+A'
    
    
def test_calculate_density():
    assert calculate_density('Fe') == 7.9
    assert calculate_density('HfNbTa') == 12.9
    assert calculate_density('CoFeNiSi0.25') == 7.7
    assert calculate_density('Al2CoCrCuFeNi') == 6.3

    
def test_calculate_youngs_modulus():
    assert calculate_youngs_modulus('CoFeNi') == 207
    assert calculate_youngs_modulus('CoFeNiSi0.25') == 186   

    
def test_classify_processing_method():
    assert classify_processing_method('AC+A')=='ANNEAL'
    assert classify_processing_method('AC')=='CAST'
    assert classify_processing_method('SPS+A')=='POWDER'
    assert classify_processing_method('CR+A')=='WROUGHT'
    
    
def test_classify_microstructure():
    assert classify_microstructure('BCC+FCC') == 'BCC+FCC'
    assert classify_microstructure('BCC+sigma') == 'BCC+Sec.'


    
