import numpy as np
import pandas as pd

raw_data = [[0,0,0]]
norm = [[0]]

clouds_xyz_a = np.empty((0,3),float)
clouds_rgb_a = np.empty((0,4),int)

clouds_xyz_b = np.empty((0,3),float)
clouds_rgb_b = np.empty((0,4),int)

with open("/home/chang/project_new/engfactory_cloud.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = cc[3]
    g = cc[4]
    b = cc[5]
    a = 255
    clouds_xyz_a = np.append(clouds_xyz_a, np.array([[x, y, z]]), axis = 0)
    clouds_rgb_a = np.append(clouds_rgb_a, np.array([[r, g, b, a]]), axis = 0)

with open("/home/chang/project_new/7eng_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = cc[3]
    g = cc[4]
    b = cc[5]
    a = 255
    clouds_xyz_b = np.append(clouds_xyz_b, np.array([[x, y, z]]), axis = 0)
    clouds_rgb_b = np.append(clouds_rgb_b, np.array([[r, g, b, a]]), axis = 0)

for i in clouds_xyz_a:

  raw = clouds_xyz_b - i
  raw_data = np.concatenate([raw_data,raw])

  calc = np.power(raw,2).sum(axis=1)
  calc = np.expand_dims(calc,axis=0).T

  norm = np.concatenate([norm,calc],axis=0)

result = np.concatenate([raw_data,norm],axis=1)
result = result[result[:, 3].argsort()]
result = result[1:200,0:3].mean(axis=0)

clouds_xyz_b =  clouds_xyz_b - result

clouds_a = np.concatenate([clouds_xyz_a, clouds_rgb_a], axis=1)
clouds_b = np.concatenate([clouds_xyz_b, clouds_rgb_b], axis=1)
clouds = np.concatenate([clouds_xyz_a, clouds_rgb_b], axis=0)

np.savetxt("clouds_test.txt", clouds, fmt='%f', delimiter=' ')