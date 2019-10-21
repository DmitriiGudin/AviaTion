# Created by Dmitrii Gudin (U Notre Dame).

from __future__ import division
import numpy as np
import h5py
import os
import params
import random


# Parameter grid for the new template files.
Teff_mask = np.array([4750, 5250, 5750, 6500, 8000])
FeH_mask = np.array([-3.5, -2, -1, 0, 1])
CFe_mask = np.array([-1, 1.5, 2.5, 4])


def get_template_indeces_list (f):
    Teff_FeH_list = []
    for Teff in Teff_mask:
        for FeH in FeH_mask:
            for CFe in CFe_mask:
                temp_Teff, temp_FeH, temp_CFe = f['/T_EFF'][:], f['/FE_H'][:], f['/C_FE'][:]
                indeces_Teff = np.where(abs(Teff-temp_Teff) == min(abs(Teff-temp_Teff)))[0]
                indeces_FeH = np.where(abs(FeH-temp_FeH) == min(abs(FeH-temp_FeH)))[0]
                indeces_CFe = np.where(abs(CFe-temp_CFe) == min(abs(CFe-temp_CFe)))[0]
                indeces = np.intersect1d(indeces_CFe, np.intersect1d(indeces_Teff, indeces_FeH))
                Teff_FeH_list.append(list(indeces))
    return Teff_FeH_list


if __name__ == '__main__':
    File_in = h5py.File(params.template_hdf5_file, 'r')
    available_indeces = get_template_indeces_list (File_in)
    print available_indeces
    print ""
    print ""
    for i in available_indeces:
        print "Teff = ", File_in['/T_EFF'][i][0]
        print "[Fe/H] = ", File_in['/FE_H'][i][0]
        print "[C/Fe] = ", File_in['/C_FE'][i][0]
        print i
        print ""

    print ""
    print "Random set: (Teff, [Fe/H], [C/Fe] : index, log(g))"
    for indeces in available_indeces:
        i = random.choice(indeces)
        print File_in['/T_EFF'][i][0], ", ", File_in['/FE_H'][i][0], ", ", File_in['/C_FE'][i][0], " : ", i, ", ", File_in['/LOG_G'][i][0]
    File_in.close()
    
    
    
