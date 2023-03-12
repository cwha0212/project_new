import numpy as np

f = open("/home/chang/project_new/135.txt", "r")
flines = f.readlines()
num = 1
train = np.empty((0,3),float)
target = np.empty((0,3),float)

for fline in flines:
  aa = fline.split()
  x = float(aa[0])
  y = float(aa[1])
  z = float(aa[2])
  if num % 2 == 1:
    train = np.append(train, np.array([[x,y,z]]), axis = 0)
    print("train")
  else :
    target = np.append(target, np.array([[x,y,z]]), axis = 0)
    print("target")
  num += 1

num = (num-1)/2
print(num)
lr = 0.00001
epochs = 100

h11=1
h12=0
h13=0
h21=0
h22=1
h23=0
h31=0
h32=0
h33=1
h14=1
h24=1
h34=1
W = np.array([[h11,h12,h13],[h21,h22,h23],[h31,h32,h33]])
B = np.array([[h14],[h24],[h34]])

for i in range(5000):
  for k in range(int(num)):
    train1 = train[k]
    train1 = np.expand_dims(train1, axis=0)
    train1 = train1.T
    target1 = target[k]
    target1 = np.expand_dims(target1, axis=0)
    target1 = target1.T
    W = np.array([[h11,h12,h13],[h21,h22,h23],[h31,h32,h33]])
    B = np.array([[h14],[h24],[h34]])
    data = np.dot(W,train1)+B
    loss1 = -target1[0]+data[0]
    loss2 = -target1[1]+data[1]
    loss3 = -target1[2]+data[2]
    h11 = h11-float(lr*loss1*train1[0])
    h12 = h12-float(lr*loss1*train1[1])
    h13 = h13-float(lr*loss1*train1[2])
    h21 = h21-float(lr*loss2*train1[0])
    h22 = h22-float(lr*loss2*train1[1])
    h23 = h23-float(lr*loss2*train1[2])
    h31 = h31-float(lr*loss3*train1[0])
    h32 = h32-float(lr*loss3*train1[1])
    h33 = h33-float(lr*loss3*train1[2])
    h14 = h14-float(lr*loss1)
    h24 = h24-float(lr*loss2)
    h34 = h34-float(lr*loss3)
print(loss1)
print(loss2)
print(loss3)
print(W)
print(B)