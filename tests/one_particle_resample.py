import sys
import matplotlib.pylab as plt
import numpy as np

from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) ) # adds src to module list

from src.particle import Particle
from src.particle import Spherical_Plummer_Vectorized


p           = Particle([1.,0.,0.,0.,0.,0.,0.], 1.)
p_resample  = p.Resample_Plummer_Positions(1000000)
r           = [np.linalg.norm(x) for x in p_resample]


bin_edges = np.linspace(-1,1,51)
bins      = bin_edges[1:] - (bin_edges[1] - bin_edges[0])
x_hist, _ = np.histogram(p_resample.T[0],bins=bin_edges)
y_hist, _ = np.histogram(p_resample.T[1],bins=bin_edges)
z_hist, _ = np.histogram(p_resample.T[2],bins=bin_edges)

r_bin_edges = np.linspace(0,10.,101)
r_bins      = r_bin_edges[1:] - (r_bin_edges[1] - r_bin_edges[0])
r_hist,_    = np.histogram(r, bins=r_bin_edges,normed=True)


plt.plot(r_bins, r_hist)
plt.plot(r_bins, Spherical_Plummer_Vectorized(r_bins,1))
plt.show()

plt.plot(bins, x_hist, lw=2)
plt.plot(bins, y_hist, lw=2)
plt.plot(bins, z_hist, lw=2)

plt.show()
