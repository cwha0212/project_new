import numpy as np

f = open("/home/chang/project_new/7eng_chain_cloud.txt", "r")
t = open("/home/chang/project_new/engfactory_chain_cloud.txt", "r")
l = open("/home/chang/project_new/7eng_chain.txt", "w")
q = open("/home/chang/project_new/engfactory_chain.txt", "w")
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
        l.write((aa[0])+" "+(aa[1])+" "+(aa[2])+"\n")
        q.write((bb[0])+" "+(bb[1])+" "+(bb[2])+"\n")