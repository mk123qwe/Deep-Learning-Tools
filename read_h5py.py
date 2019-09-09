import os
import numpy as np
import h5py

f = h5py.File('D:\\..\\grayscale_maps.h5','r')
# You can view all the primary keys
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
    print(f[key].value)
