META_INFO = {
    'engine_type' : {
        'search_engine' : True,
    },
    'input_types'               : ['.mzML'],
    'output_extension'          : '.mzid',
    'create_own_folder'         : True,
    'citation'                  : 'Tabb DL, Fernando CG, Chambers MC. '\
        '(2007) MyriMatch: highly accurate tandem mass spectral peptide '\
        'identification by multivariate hypergeometric analysis.',

    'include_in_git'            : False,
    
    'engine': {
        'win32' : {
            '64bit' : {
                'exe'            : 'myrimatch.exe',
                'url'            : '',
                'zip_md5'        : 'afc021ece562109e753b49333fe75df1',
                'additional_exe' : [],
            },
            '32bit' : {
                'exe'            : 'myrimatch.exe',
                'url'            : '',
                'zip_md5'        : '59d00d759ae6f9225f42ed72844a9ca2',
                'additional_exe' : [],
            },
        },
    },
}


DEFAULT_PARAMS = {
    'validation_score_field'    : 'MyriMatch:MVH',
    'evalue_field'              : 'MyriMatch:MVH',
    'validation_minimum_score'  : 0,
    'bigger_scores_better'      : True
}

USEARCH_PARAM_KEY_VALUE_TRANSLATOR = {
    'semi_enzyme'  : {
        False : '1',
        True: '2'},
    'score_a_ions' : {
        True : 'a',
        False: ''},
    'score_b_ions' : {
        True : 'b',
        False: ''},
    'score_c_ions' : {
        True : 'c',
        False: ''},
    'score_x_ions' : {
        True : 'x',
        False: ''},
    'score_y_ions' : {
        True : 'y',
        False: ''},
    'score_z_ions' : {
        True : 'z',
        False: ''},

    'precursor_isotope_range'   : {
        '0'     : '[0,]',
        '0,1'   : '[0,1]',
        '0,1,2' : '[0,1,2]'
    },
}

USED_USEARCH_PARAMS= set([
    'enzyme',
    'semi_enzyme',
    'modifications',
    'frag_mass_tolerance',
    'frag_mass_tolerance_unit',
    'maximum_missed_cleavages',
    'maximal_accounted_observed_peaks',
    'max_pep_length',
    'min_pep_length',
    'num_match_spec',
    'precursor_mass_type',
    'precursor_min_mass',
    'precursor_mass_tolerance_minus',
    'precursor_mass_tolerance_unit',
    'precursor_max_charge',
    'score_a_ions',
    'score_b_ions',
    'score_c_ions',
    'score_x_ions',
    'score_y_ions',
    'score_z_ions',
    'database',
    'batch_size',
    'validation_score_field',
    'evalue_field',
    'validation_minimum_score',
    'bigger_scores_better',
    'cpus'


    # 'myri_average': 'AvgPrecursorMzTolerance', #default=1.5m/z
    # 'myri_compute_xcorr':'ComputeXCorr', #default=true
    # 'myri_':'ClassSizeMultiplier', #default=2
    # 'myri_':'EstimateSearchTimeOnly',
    # 'myri_':'FragmentationAutoRule',
    # 'myri_':'KeepUnadjustedPrecursorMz',
    # 'myri_':'MaxDynamicMods',
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    # 'myri_':''
    ])

USEARCH_PARAM_VALUE_TRANSLATIONS = {

    'trypsin'               :'Trypsin',
    'trypsin_p'             :'Trypsin/P',
    'chymotrypsin'          :'Chymotrypsin',
    'lysc'                  :'Lys-C',

    # -       “Trypsin” (allows for cut after K or R)
    # -       “Trypsin/P” (normal trypsin cut, disallows cutting when the site is before a proline)
    # -       "Chymotrypsin” (allows cut after F,Y,W,L. Disallows cutting before proline)
    # -       "TrypChymo” (combines “Trypsin/P” and “Chymotrypsin” cleavage rules)
    # -       “Lys-C”
    # -       “Lys-C/P” (Lys-C, disallowing cutting before proline)
    # -       “Asp-N”
    # -       “PepsinA” (Cuts right after F, L)
    # -       “CNBr” (Cyanogen bromide)
    # -       “Formic_acid” (Formic acid)
    # -       “NoEnzyme” (not supported; use the proper enzyme and set MinTerminiCleavages to 0)
    #   another supported enzymes see: http://www.ebi.ac.uk/ontology-lookup/browse.do?ontName=MS&termId=MS:1001045&termName=cleavage%20agent%20name

    'monoisotopic':'mono'

}
