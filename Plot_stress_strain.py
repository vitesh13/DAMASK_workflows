#!/usr/bin/env python
# coding: utf-8

import damask
import numpy as np
import h5py
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as PyPlot

def plot(job_file):
  """
  Plot the stress strain curve from the job file

  Parameters
  ----------
  job_file : str
    Name of the job_file
  """
  d = damask.Result(job_file)
  stress_path = d.get_dataset_location('avg_sigma')
  stress = np.zeros(len(stress_path))
  strain = np.zeros(len(stress_path))
  hdf = h5py.File(d.fname)
  for count,path in enumerate(stress_path):
      stress[count] = np.array(hdf[path])
      strain[count] = np.array(hdf[path.split('avg_sigma')[0]     + 'avg_epsilon'])
  
  stress = np.array(stress)/1E6
  PyPlot.plot(strain,stress,linestyle='-',linewidth='2.5')
  PyPlot.xlabel(r'$\varepsilon_{VM} $',fontsize=18)
  PyPlot.ylabel(r'$\sigma_{VM}$ (MPa)',fontsize=18)
