import numpy as np


def ConvQuatToMat(pos, ori):
  q0 = ori[0]
  q1 = ori[1]
  q2 = ori[2]
  q3 = ori[3]

  t = np.array([[pos[0]],
                  [pos[1]],
                  [pos[2]]])

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

  RotationMat = np.concatenate([R, t], 1)
  a = np.array([[0,0,0,1]])
  RotationMat = np.concatenate([RotationMat, a])
  return RotationMat

pos1 = [-23.9229750476, -0.0535605255219, 9.33555329034]
ori1 = [0.786117857896, -0.0201473329851, 0.617380595993, -0.0213356424875]

pos2 = [53.3270992038, 0.046179437072, -31.181354216]
ori2 = [0.998085638374, -0.0564309751221, -0.0244827196724, 0.00645456588391]

focal = 1084.20385742 / 1113.74719238
# focal = 1300 / 1084.20385742
print(focal)

R = ConvQuatToMat(pos2, ori1)
R_f = ConvQuatToMat(pos1, ori2)
Mat = np.dot(R ,np.linalg.inv(R_f))
print(R)
print(np.dot(Mat,R_f))

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

one = np.ones((use_cloud, 1))
# clouds_xyz = clouds_xyz*focal
clouds_xyz = np.concatenate([clouds_xyz, one], 1)

clouds_xyz = np.dot(np.linalg.inv(Mat), clouds_xyz.T)
new_Mat = np.array([[0.98065958,-0.19366996,0.02826179,-4.52308749],
                  [0.19065961,0.97791355,0.0856388,3.99397214],
                  [-0.04422325,-0.07859412,0.99592533,-0.96718937],
                  [0,0,0,1]])
clouds_xyz = np.dot(new_Mat, clouds_xyz)
clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
# clouds_xyz = clouds_xyz * focal
# clouds_xyz = clouds_xyz + [ 1.86367226, 1.55769382,-1.19781009]
clouds = np.concatenate([clouds_xyz, clouds_rgb], 1)

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

clouds_f = np.concatenate([clouds_xyz, clouds_rgb], 1)
clouds = np.concatenate([clouds, clouds_f], 0)

np.savetxt("clouds.txt", clouds, fmt='%f', delimiter=' ')