from __future__ import division
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def plot_RV(RV):
    plt.clf()
    plt.title("RAVE sample", size=24)
    plt.xlabel("Radial velocity (km/s)", size=24)
    plt.ylabel("Count", size=24)
    plt.tick_params(labelsize=18)
    plt.xlim(min(RV), max(RV))
    plt.hist(RV, bins=60, color='black', fill=False, linewidth=3, histtype='step')
    plt.gcf().set_size_inches(25.6, 14.4)
    plt.gcf().savefig("hist.png", dpi=100)
    plt.close()


if __name__=='__main__':
    RV = np.genfromtxt("output.txt", dtype=float, delimiter='\t')
    RV = RV[~np.isnan(RV)]
    plot_RV(RV)
