from __future__ import division
import numpy as np
import h5py
import csv
import params

if __name__ == '__main__':
    star_name_list = np.genfromtxt (params.name_list, dtype=str, delimiter='\t')
    with open(params.script_file, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for name in star_name_list:
            f.write('\n')
            f.write('onedspec')
            f.write('\n')
            #f.write('rspectext '+params.txt_folder+name+'_obs.txt '+params.fit_folder+name+'_obs.fit')
            f.write('cp '+params.obs_fit_folder+name+'.fits '+params.fit_folder+name+'_obs.fit')
            f.write('\n')
            f.write('rspectext '+params.txt_folder+name+'_temp.txt '+params.fit_folder+name+'_temp.fit')
            f.write('\n')
            f.write('noao.rv')
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit DATE-OBS '1993-03-17T04:56:38.0' add=yes verify=no")
	    f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit RA '12:00:00' add=yes verify=no")
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit DEC '12:00:00' add=yes verify=no")
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit EPOCH '1993.0' add=yes verify=no")
            f.write('\n') 
            f.write("hedit "+params.fit_folder+name+"_temp.fit OBSERVAT 'KPNO' add=yes verify=no")
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit VHELIO 0.0 add=yes verify=no")
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit CRVAL1 3000")
            f.write('\n')
            f.write("hedit "+params.fit_folder+name+"_temp.fit CDELT1 1")
            f.write('\n')
            f.write('fxcor '+params.fit_folder+name+'_obs.fit[*,1,1] '+params.fit_folder+name+'_temp.fit interactive=no verbose=stxtonly output="'+params.output_folder+name+'_output"')
            f.write('\n')
            
