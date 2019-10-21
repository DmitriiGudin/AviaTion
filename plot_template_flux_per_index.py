# Created by Dmitrii Gudin (U Notre Dame).

from __future__ import division
import numpy as np
import sys
import params
import h5py
import matplotlib
import matplotlib.pyplot as plt


wavelength_array = np.arange (3000, 10000+1, 1)


def plot_stuff(f, i):
    Spectrum, T_EFF, LOG_G, FE_H, C_FE = f['/spectrum'][i], f['/T_EFF'][i][0], f['/LOG_G'][i][0], f['/FE_H'][i][0], f['/C_FE'][i][0]
    plt.clf()
    plt.title("Spectrum "+str(i)+": Teff = "+str(T_EFF)+", log(g) = "+str(LOG_G)+", [Fe/H] = "+str(FE_H)+", [C/Fe] = "+str(C_FE), size=24)
    plt.xlabel("Wavelength (A)", size=24)
    plt.ylabel("Flux", size=24)
    plt.tick_params(labelsize=18)
    plt.xlim(min(wavelength_array), max(wavelength_array))
    plt.ylim(min(Spectrum), max(Spectrum))
    plt.plot(wavelength_array, Spectrum, linewidth=2, color='black')
    plt.gcf().set_size_inches(25.6, 14.4)
    plt.show()


if __name__ == '__main__':
    File_in = h5py.File(params.template_hdf5_file, 'r')
    while (True):
        input_line = raw_input ("Enter the index. Enter 'q' to abort.\n")
        if input_line == 'q':
            print "Goodbye!"
            break
        else: 
            try:
                index = int(input_line)
            except:
                print "Erroneous input. Try again!"
                continue
        index = int(input_line)
        if index < 0 or index >= len(File_in['/spectrum'][:]):
            print "Such index does not exist. Enter a value between 0 and ",len(File_in['/spectrum'][:])-1
            continue
        plot_stuff(File_in, index)
        
