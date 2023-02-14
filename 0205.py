import numpy as np


def ConvQuatToMat(pos, ori):
  q0 = ori[0]
  q1 = ori[1]
  q2 = ori[2]
  q3 = ori[3]

  # t = np.array([[pos[0]],
  #                 [pos[1]],
  #                 [pos[2]]])

  r00 = 2 * (q0 * q0 + q1 * q1) - 1
  r01 = 2 * (q1 * q2 - q0 * q3)
  r02 = 2 * (q1 * q3 + q0 * q2)
      
  r10 = 2 * (q1 * q2 + q0 * q3)
  r11 = 2 * (q0 * q0 + q2 * q2) - 1
  r12 = 2 * (q2 * q3 - q0 * q1)
      
  r20 = 2 * (q1 * q3 - q0 * q2)
  r21 = 2 * (q2 * q3 + q0 * q1)
  r22 = 2 * (q0 * q0 + q3 * q3) - 1

  R = np.array([[r00, r01, r02],
                  [r10, r11, r12],
                  [r20, r21, r22]])

  # RotationMat = np.concatenate([R, t], 1)
  # a = np.array([[0,0,0,1]])
  # RotationMat = np.concatenate([RotationMat, a])
  return R

pos1 = [-23.0780832778,-0.0202448357426,10.1999821029]
ori1 = [0.826162059389,-0.0211078304103,0.562866538945,-0.0138420562075]

pos2 = [54.4009407779,0.102018600218,-31.8319075869]
ori2 = [0.994243274731,-0.0534384469865,-0.0922518295111,0.0106869106612]

focal = 1084.20385742 / 1113.74719238
# focal = 1300 / 1084.20385742
print(focal)

R = ConvQuatToMat(pos1, ori1)
R_f = ConvQuatToMat(pos2, ori2)

t = np.array([[pos1[0], pos1[1], pos1[2]]])

t_f = np.array([[pos2[0], pos2[1], pos2[2]]])

i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open("/home/chang/project_new/engfactory.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
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
clouds_xyz = clouds_xyz * focal
clouds_xyz = clouds_xyz - t_f
clouds_xyz = np.dot(R_f, clouds_xyz.T)
# clouds_xyz = clouds_xyz * focal

clouds = np.concatenate([clouds_xyz.T, clouds_rgb], 1)

i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open("/home/chang/project_new/7eng.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose = int(aa[0])
    if i == use_pose + 5:
      bb = line.split()
      use_cloud = int(bb[0])
    if i >= use_pose + 6 and i <= use_cloud + use_pose + 5:
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

clouds_xyz = clouds_xyz - t
clouds_xyz = np.dot(R, clouds_xyz.T)
# clouds_xyz = clouds_xyz * focal

clouds_f = np.concatenate([clouds_xyz.T, clouds_rgb], 1)

clouds = np.concatenate([clouds, clouds_f], 0)

np.savetxt("clouds.txt", clouds, fmt='%f', delimiter=' ')