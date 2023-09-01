#!/usr/bin/env python3


from SigProfilerAssignment import Analyzer as Analyze   # https://github.com/AlexandrovLab/SigProfilerAssignment
import pandas as pd


Analyze.cosmic_fit(samples = 'data/data_for_deconstructSigs.dat', input_type = 'matrix', output = 'signature_results', genome_build = 'GRCh38', signature_database = '../input/COSMIC_v3_SBS_GRCh38-RELEVANT.txt', make_plots = False, sample_reconstruction_plots = False)
df = pd.read_csv('signature_results/Assignment_Solution/Activities/Assignment_Solution_Activities.txt', sep = '\t', index_col = 'Samples').T
df.to_csv('signature_results/SPA-contribution.dat')
