#!/usr/bin/env python3.4
import ursgal
import os


class svm_1_0_0( ursgal.UNode ):
    """svm_1_0_0 UNode"""
    def __init__(self, *args, **kwargs):
        super(svm_1_0_0, self).__init__(*args, **kwargs)


    def preflight(self):
        if not self.params['input_file'].lower().endswith('.csv'):
            raise ValueError(
                '\nSVM input file must be a unified CSV file, '\
                'but you specified: ' + self.params['input_file']
            )

        in_path = os.path.join(
            self.params['input_dir_path'],
            self.params['input_file']
        )

        out_path = os.path.join(
            self.params['output_dir_path'],
            self.params['output_file']
        )

        self.params['command_list'] = [
            'python3.4',
            self.exe,
            '--input_csv',
            in_path,
            '--output_csv',
            out_path,
            '--kernel',
            self.params['kernel'],
            '--fdr_cutoff',
            str(self.params['fdr_cutoff']),
            '-c',
            str(self.params['c']),
            '--mb_ram',
            str(self.params['available_RAM_in_MB']),
        ]

        if self.params['columns_as_features']:
            self.params['command_list'].append(
                '--columns_as_features'
            )
            self.params['command_list'].append(
                ' '.join(self.params['columns_as_features'])
            )

    def postflight(self):
        return
