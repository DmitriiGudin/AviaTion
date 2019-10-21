from __future__ import division
import numpy as np
import h5py
import csv
import params


def get_column(N, Type, filename):
    return np.genfromtxt(filename, delimiter=',', dtype=Type, skip_header=1, usecols=N, comments=None)


# Returns the index of the best template for the specified parameters.
def get_best_template_index (Teff, logg, FeH, CFe):
    temp_Teff, temp_FeH, temp_CFe, indeces = get_column(0, params.template_indeces_file, float), get_column(1, params.template_indeces_file, float), get_column(2, params.template_indeces_file, float), get_column(4, params.template_indeces_file, int)
    indeces_Teff, indeces_FeH, indeces_CFe = np.where(abs(temp_Teff-Teff)==min(abs(temp_Teff-Teff)))[0], np.where(abs(temp_FeH-FeH)==min(abs(temp_FeH-FeH)))[0], np.where(abs(temp_CFe-CFe)==min(abs(temp_CFe-CFe)))[0]
    return indeces[np.intersect1d(np.intersect1d(indeces_Teff,indeces_FeH),indeces_CFe)][0]

if __name__ == '__main__':
    # Load the *.hdf5 files.
    template_hdf5_file = h5py.File (params.template_hdf5_file, 'r')
    obs_hdf5_file = h5py.File (params.obs_hdf5_file, 'r')
    # Retrieve the spectrum arrays.
    template_wavelength = np.array(params.template_wavelengths)
    spectrum = template_hdf5_file['/spectrum'][:]
    obs_wavelength = obs_hdf5_file['/wavelength'][:]
    obs_spectrum = obs_hdf5_file['/spectrum'][:]
    # Iterate over all observation spectra and retrieve their parameters.
    for i in range(len(obs_hdf5_file['/name'][:])):
        name, T_EFF, LOG_G, FE_H, C_FE, wavelength, spectrum = obs_hdf5_file['/name'][i], obs_hdf5_file['/T_EFF'][i], obs_hdf5_file['/LOG_G'][i], obs_hdf5_file['/FE_H'][i], obs_hdf5_file['/C_FE'][i], obs_hdf5_file['/wavelength'][i][~np.isnan(obs_hdf5_file['/wavelength'][i])], obs_hdf5_file['/spectrum'][i][~np.isnan(obs_hdf5_file['/spectrum'][i])]
        # Retrieve the best template spectrum and parameters.
        temp_index = get_best_template_index (template_hdf5_file, T_EFF, LOG_G, FE_H, C_FE)
        T_EFF_0, LOG_G_0, FE_H_0, C_FE_0, wavelength_0, spectrum_0 = template_hdf5_file['/T_EFF'][:][temp_index], template_hdf5_file['/LOG_G'][:][temp_index], template_hdf5_file['/FE_H'][:][temp_index], template_hdf5_file['/C_FE'][:][temp_index], template_wavelength, template_hdf5_file['/spectrum'][:][temp_index]
        # Save the spectra as *.txt.
        print "Saving data of the spectrum number", i+1, "out of", len(obs_hdf5_file['/name'][:]), "..."
        with open(params.txt_folder+name+'_obs.txt', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(zip(wavelength, spectrum))
        with open(params.txt_folder+name+'_temp.txt', 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(zip(wavelength_0, spectrum_0[0]))
    # Save the list of star names.
    with open(params.txt_folder+'name_list.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(list(obs_hdf5_file['/name'][:]))
    print "Done."
       
        
        
    
