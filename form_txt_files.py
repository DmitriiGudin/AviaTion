from __future__ import division
import numpy as np
import h5py
import csv
import params


# Returns the index of the best template for the specified parameters.
def get_best_template_index (f, Teff, logg, FeH, CFe):
    temp_Teff, temp_logg, temp_FeH, temp_CFe = f['/T_EFF'][:], f['LOG_G'][:], f['FE_H'][:], f['C_FE'][:]
    # 1 - Teff
    if not (np.isnan(Teff)):
        indeces = np.where(abs(Teff-temp_Teff) == min(abs(Teff-temp_Teff)))[0]
        temp_CFe, temp_logg, temp_FeH = temp_CFe[indeces], temp_logg[indeces], temp_FeH[indeces]
        final_Teff = temp_Teff[indeces][0][0]  
    else:
        final_Teff = f['/T_EFF'][np.random.randint(len(f['/T_EFF'][:]))]
    # 2 - FeH
    if not (np.isnan(FeH)):
        indeces = np.where(abs(FeH-temp_FeH) == min(abs(FeH-temp_FeH)))[0]
        temp_CFe, temp_logg = temp_CFe[indeces], temp_logg[indeces]
        final_FeH = temp_FeH[indeces][0][0]
    else:
        final_FeH = f['/FE_H'][np.random.randint(len(f['/FE_H'][:]))]
    # 3 - CFe
    if not (np.isnan(CFe)):
        indeces = np.where(abs(CFe-temp_CFe) == min(abs(CFe-temp_CFe)))[0]
        temp_logg = temp_logg[indeces]
        final_CFe = temp_CFe[indeces][0][0]
    else:
        final_CFe = f['/C_FE'][np.random.randint(len(f['/C_FE'][:]))]
    # 4 - logg
    if not (np.isnan(logg)):
        indeces = np.where(abs(logg-temp_logg) == min(abs(logg-temp_logg)))[0]
        final_logg = temp_logg[indeces][0][0]
    else:
        final_logg = f['/LOG_G'][np.random.randint(len(f['/LOG_G'][:]))]
    # Final index
    temp_Teff, temp_logg, temp_FeH, temp_CFe = f['/T_EFF'][:], f['LOG_G'][:], f['FE_H'][:], f['C_FE'][:]
    index = np.intersect1d (np.intersect1d(np.where(temp_Teff==final_Teff)[0],np.where(temp_logg==final_logg)[0]), np.intersect1d(np.where(temp_FeH==final_FeH)[0],np.where(temp_CFe==final_CFe)[0]))
    if len(index)>1:
        return index[np.random.randint(len(index))]
    else:
        return index


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
       
        
        
    
