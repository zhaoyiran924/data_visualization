import numpy as np
#import h5py
import scipy.io as sio

from PerSec import PerSec
from getList import getList

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

myFile = sio.loadmat('/Users/macbook/Desktop/实验室/dataset/yqviewpoint.mat')
#myFile = h5py.File('yproject.mat','r')

print(myFile.keys())
#print([key for key in myFile.keys()])
'''
X = np.linspace(-90,90,8)
YX = np.linspace(-180,180,8)
Y = np.linspace(-180,180,12)
XY = np.linspace(-90,90,12)
for i in X:
    y = np.zeros((1,8))
    y[0] = np.array([i]*8)
    y = np.array(y).reshape(8,1)
    plt.plot(YX,y,color = 'black',linewidth=0.4)
for k in Y:
    x = np.zeros((1,12))
    x[0] = np.array([k]*12)
    x = np.array(x).reshape(12,1)
    plt.plot(x,XY,color = 'black',linewidth=0.4)

plt.savefig('zt.jpg', dpi=200)
'''

'''
#一个人每两秒的每个视频
Person = 1
Second = 2
PerSec = PerSec(Person, Second, myFile)
'''

#一个人三十秒的每个视频
Person = 1
Second = 30
PerSec = PerSec(Person, Second, myFile)


'''
#所有人每两秒的每个视频
Person = 259
Second = 2
PerSec = PerSec(Person, Second, myFile)
'''

'''
#所有人三十秒的每个视频
Person = 259
Second = 30
PerSec = PerSec(Person, Second, myFile)
'''
