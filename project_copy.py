import numpy as np
i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open("/home/chang/project_new/7eng_chain_cloud.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    # i = i+1
    # if i == 3:
    #   aa = line.split()
    #   use_pose = int(aa[0])
    # if i == use_pose + 5:
    #   bb = line.split()
    #   use_cloud = int(bb[0])
    # if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      clouds_xyz = np.append(clouds_xyz, np.array([[x, y, z]]), axis = 0)
      clouds_rgb = np.append(clouds_rgb, np.array([[r, g, b, a]]), axis = 0)
      use_cloud +=1

one = np.ones((use_cloud, 1))
clouds_xyz = np.concatenate([clouds_xyz, one], 1)

new_Mat = np.array([[0.9954653,-0.09064216,-0.02885877,-2.45307016],
                  [0.09307815,0.99073669,0.09888012,0.23192433],
                  [0.01962874,-0.10111785,0.9946808,1.32253994],
                  [0,0,0,1]])
clouds_xyz = np.dot(new_Mat, clouds_xyz.T)
clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
clouds = np.concatenate([clouds_xyz, clouds_rgb], 1)

i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open("/home/chang/project_new/engfactory_chain_cloud.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    # i = i+1
    # if i == 3:
    #   aa = line.split()
    #   use_pose = int(aa[0])
    # if i == use_pose + 5:
    #   bb = line.split()
    #   use_cloud = int(bb[0])
    # if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      clouds_xyz = np.append(clouds_xyz, np.array([[x, y, z]]), axis = 0)
      clouds_rgb = np.append(clouds_rgb, np.array([[r, g, b, a]]), axis = 0)
      use_cloud +=1


clouds_f = np.concatenate([clouds_xyz, clouds_rgb], 1)
clouds = np.concatenate([clouds, clouds_f], 0)

np.savetxt("clouds.txt", clouds, fmt='%f', delimiter=' ')