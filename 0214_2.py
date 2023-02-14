import numpy as np

f = open("/home/chang/project_new/7eng_135_cloud.txt", "r")
t = open("/home/chang/project_new/engfactory_135_cloud.txt", "r")
l = open("/home/chang/project_new/135.txt", "w")
flines = f.readlines()
tlines = t.readlines()

clouds_xyz = np.empty((0,3),float)

for fline in flines:
  aa = fline.split()
  r = int(aa[3])
  g = int(aa[4])
  b = int(aa[5])
  for tline in tlines:
    bb = tline.split()
    if r == int(bb[3]) and g == int(bb[4]) and b == int(bb[5]):
      x = float(aa[0]) - float(bb[0])
      y = float(aa[1]) - float(bb[1])
      z = float(aa[2]) - float(bb[2])
      if x<5 and x>-5 and y<5 and y>-5 and z<5 and z>-5:
        clouds_xyz = np.append(clouds_xyz, np.array([[x, y, z]]), axis = 0)

mean = clouds_xyz.mean(axis=0)
print(mean)
with open("/home/chang/project_new/135_f.txt", "w") as j:
  for fline in flines:
    cc = fline.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    cloud_xyz = [x,y,z]
    save_line = cloud_xyz + cc[3:]
    for k in save_line:
      j.write(str(k)+" ")
    j.write("\n")
  for tline in tlines:
    cc = tline.split()
    x = float(cc[0]) + mean[0]
    y = float(cc[1]) + mean[1]
    z = float(cc[2]) + mean[2]
    # x = float(cc[0])
    # y = float(cc[1])
    # z = float(cc[2])
    cloud_xyz = [x,y,z]
    save_line = cloud_xyz + cc[3:]
    for k in save_line:
      j.write(str(k)+" ")
    j.write("\n")