from __future__ import division
import numpy as np
import csv
import params

if __name__ == '__main__':
    star_name_list = np.genfromtxt (params.name_list, dtype=str, delimiter='\t')
    with open(params.output_folder+'output.txt', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for name in star_name_list:
            iraf_file = params.output_folder+name+'_output.txt'
            with open(iraf_file, 'r') as f_i:
                lines = f_i.read().splitlines()
                print lines
            if (len(lines)>0):
                f.write(lines[-1].split()[-1])
                f.write('\n')
            
