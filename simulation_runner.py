#!/usr/bin/env python
# coding: utf-8

# ## Simulation runer class
# Here the functions will create the geometry as vtr file for the simulations

# In[1]:


import damask
from damask import Geom
import numpy as np
import subprocess,shlex
import os


# In[2]:


class simulation():
    def run(simulation_folder,geom,load):
        """
        Run the DAMASK simulations.
        Returns the returncode after the simulation is done.
        
        Parameters
        ----------
        simulation_folder : str
          Path to the simulation folder
        geom              : str
          Name of the geom file
        load              : str
          Name of the load file
        """
        cmd = f'DAMASK_grid -l {load} -g {geom}'
        p = subprocess.Popen(cmd,shell=True)
        while p.poll() == None:
            p.poll()
        return p.poll()




