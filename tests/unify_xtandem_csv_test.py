#!/usr/bin/env python3.4
# encoding: utf-8
'''

Test the unify_csv function for xtandem engine

'''
import ursgal
import csv
import pickle
import os


R = ursgal.UController(
    profile = 'LTQ XL low res',
    params  = {
        'database': os.path.join( 'tests', 'data', 'BSA.fasta'),
    },
    force   = False
)

scan_rt_lookup = pickle.load(
    open(
        os.path.join(
            'tests',
            'data',
            '_test_ursgal_lookup.pkl')
        ,
        'rb'
    )
)

unify_csv_main = R.unodes['unify_csv_1_0_0']['class'].import_engine_as_python_function()
input_csv = os.path.join(
    'tests',
    'data',
    'xtandem_sledgehammer',
    'test_BSA1_xtandem_sledgehammer.csv'
)
output_csv = os.path.join(
    'tests',
    'data',
    'xtandem_sledgehammer',
    'test_BSA1_xtandem_sledgehammer_unified.csv'
)
unify_csv_main(
    input_file     = input_csv,
    output_file    = output_csv,
    scan_rt_lookup = scan_rt_lookup,
    params = {
        'aa_exception_dict' : {
            'U' : {
                'unimod_name' : 'Delta:S(-1)Se(1)',
                'original_aa' : 'C',
                'unimod_name_with_cam': 'SecCarbamidomethyl',
            },
        },
        'modifications' : [
            'M,opt,any,Oxidation',        # Met oxidation
            'C,fix,any,Carbamidomethyl',  # Carbamidomethylation
            '*,opt,Prot-N-term,Acetyl'    # N-Acteylation
        ],
        'label':'',
        'decoy_tag': 'decoy_',
        'enzyme' : 'trypsin',
        'semi_enzyme' : False,
        'database': os.path.join( 'tests', 'data', 'BSA.fasta'),
    },
    search_engine  = 'xtandem_sledgehammer',
)

ident_list = [ ]
for line_dict in csv.DictReader(open(output_csv, 'r')):
    ident_list.append( line_dict )
# print(ident_list)

def unify_xtandem_test():
    for test_id, test_dict in enumerate(ident_list):
        yield unify_xtandem, test_dict


def unify_xtandem( test_dict ):
    assert 'uCalc m/z' in test_dict.keys()
    assert 'index=' not in test_dict['Spectrum ID']

    for key in [
            'Retention Time (s)',
            'Spectrum ID',
            'Modifications',
            'Spectrum Title'
        ]:
        test_value = test_dict[key]
        expected_value = test_dict['Expected {0}'.format(key)]
        if key == 'Retention Time (s)':
            test_value = round(float(test_value), 4)
            expected_value = round(float(expected_value), 4)

        assert test_value == expected_value


if __name__ == '__main__':
    print(__doc__)
    for test_id, test_dict in enumerate(ident_list):
        unify_xtandem(test_dict)

