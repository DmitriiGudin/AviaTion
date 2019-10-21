from __future__ import division
import numpy as np


template_hdf5_file = "/home/may/Work/CrossCorrelation/hdf5_data/CEMP_grid_non_normed.hdf5" # Location of the *.hdf5 file containing the set of template spectra.
CC_template_hdf5_file = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/CC_template_hdf5_file.hdf5" # Location of the $.hdf5 file to save template cross-correlation spectra to.
obs_hdf5_file = "/scratch365/dgudin/RAVE_spectra/RAVE_spectra.hdf5" # Location of the *.hdf5 file containing the set of the observation spectra.
obs_fit_folder = "/scratch365/dgudin/RAVE_spectra/" # Location of the folder containing the observation *.fits files.
name_list = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/txt_files/name_list.txt" # Location of the file containing the list of the observation star names.
txt_folder = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/txt_files/" # Location of the folder to which the text files are going to be saved.
fit_folder = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/fit_files/" # Location of the folder to which the Fit files are going to be saved.
output_folder = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/output_files/" # Location of the folder to which the output files are going to be saved.
script_file = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/run.cl" # Location of the script calculating the radial velocities.
template_indeces_file = "/afs/crc.nd.edu/user/d/dgudin/AviaTion/template_reliable_indeces.csv"

template_wavelengths = range (3000, 10000+1) # Array of wavelength values present in the template spectra.
