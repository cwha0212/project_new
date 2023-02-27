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

t = open("/home/chang/project_new/engfactory_chain_cloud.txt", "w")
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
      measurements_num = int(cc[6])
      cloud_xyz = np.array([[x],[y],[z],[1]])
      cloud_xyz = np.dot(np.linalg.inv(Mat), cloud_xyz)
      cloud_xyz = np.delete(cloud_xyz.T, 3, axis = 1)
      cloud_xyz = cloud_xyz.reshape(-1,)
      cloud_xyz = cloud_xyz.tolist()
      for j in range(measurements_num):
        if int(cc[7+4*j]) == 132 or int(cc[7+4*j]) == 133 or int(cc[7+4*j]) == 134 or int(cc[7+4*j]) == 135 or int(cc[7+4*j]) == 136 or int(cc[7+4*j]) == 137 or int(cc[7+4*j]) == 138 or int(cc[7+4*j]) == 139 or int(cc[7+4*j]) == 140 or int(cc[7+4*j]) == 141:
          # save_line = cloud_xyz
          save_line = cloud_xyz + cc[3:]
          print(save_line)
          for k in save_line:
            t.write(str(k)+" ")
          t.write("\n")
          break
t.close()


i = 0
use_pose = 0
use_cloud = 0
t = open("/home/chang/project_new/7eng_chain_cloud.txt", "w")
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
      measurements_num = int(cc[6])
      cloud_xyz = [x,y,z]
      for j in range(measurements_num):
        if int(cc[7+4*j]) == 83 or int(cc[7+4*j]) == 84 or int(cc[7+4*j]) == 85 or int(cc[7+4*j]) == 86 or int(cc[7+4*j]) == 87 or int(cc[7+4*j]) == 92 or int(cc[7+4*j]) == 91 or int(cc[7+4*j]) == 90 or int(cc[7+4*j]) == 89 or int(cc[7+4*j]) == 88:
          # save_line = cloud_xyz
          save_line = cloud_xyz + cc[3:]
          print(save_line)
          for k in save_line:
            t.write(str(k)+" ")
          t.write("\n")
          break
t.close()