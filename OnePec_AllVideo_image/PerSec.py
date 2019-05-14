import h5py
import numpy as np
import pandas as pd
from getList import getList
import matplotlib
matplotlib.use('TkAgg')
from math import log
from math import e

import matplotlib.pyplot as plt
import seaborn as sns

class PerSec():
    def __init__(self, Per, Sec, myFile):
        self.Person = 154
        self.Video = 16
        self.Per = Per
        self.Sec = Sec
        #self.Vid = Vid
        #self.Length = Length
        #self.Width = Width
        #self.myFile = myFile
        self.getList = getList(myFile).NowList

    #根据不同的情况采取不同的生成表格的方式
        if Sec==2:
            self.TwoSec(self.Per)
        else:
            self.ThirtySec(self.Per)

    def TwoSec(self, Per):
        if Per == 1:
            self.OneTwo()
        else:
            self.AllTwo()

    def ThirtySec(self, Per):
        if Per == 1:
            self.OneThirty()
        else:
            self.AllThirty()

    def OneTwo(self):
        #每隔20s提取一次所有位置
        self.TimeStep = 20
        self.cycle = 0
        self.List = [[]]
        #print(self.getList[1129],self.getList[1149])
        #print(self.getList.shape)

        for m in range(self.Person):
            for k in range(self.Video):
                self.cycle = 0
                while(self.cycle * self.TimeStep < 280):
                    for n in range(self.TimeStep):
                        #print(m, k, n)
                        #print(m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n)
                        #print(self.getList[m*self.Video*290 + k*290 + n])
                        #self.List.append(self.List[self.cycle * self.TimeStep + self.Person * 4640 + self.Video * 290 + n])
                        self.List = np.append(self.List, self.getList[m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n])
                    #print(self.List)
                    self.List = np.array(self.List).reshape(20,3)
                    #print(self.List)
                    ch = str('person'+str(m+1)+'_'+'Video'+str(k+1)+'_'+'segment'+str(self.cycle+1))
                    print(ch)

                    data_df = pd.DataFrame(self.List)
                    data_df.columns = ['Y','X','Z']
                    data_df.index = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
                    ch = str('person'+str(m+1)+'_'+'Video'+str(k+1)+'_'+'segment'+str(self.cycle+1))
                    print(ch)
                    writer = pd.ExcelWriter(ch+'.xlsx')
                    data_df.to_excel(writer,'page_1')
                    writer.save()

                    self.List.flatten()
                    self.List = np.delete(self.List,0,0)
                    self.cycle = self.cycle + 1

                    self.List = [[]]
        #print(self.getList[1129],self.getList[1149])


    def AllTwo(self):
        self.TimeStep = 20
        self.cycle = 0
        self.List = [[]]

        for k in range(self.Video):
            self.cycle = 0
            while(self.cycle * self.TimeStep < 280):
                for n in range(self.TimeStep):
                    #print(m, k, n)
                    #print(m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n)
                    #print(self.getList[m*self.Video*290 + k*290 + n])
                    #self.List.append(self.List[self.cycle * self.TimeStep + self.Person * 4640 + self.Video * 290 + n])
                    for m in range(self.Person):
                        self.List = np.append(self.List, self.getList[m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n])
                #print(self.List)
                self.List = np.array(self.List).reshape(3080,3)
                #print(self.List)
                data_df = pd.DataFrame(self.List)
                data_df.columns = ['Y','X','Z']
                data_df.index = [str(i) for i in range(3080)]
                ch = str('all'+'_'+'Video'+str(k+1)+'_'+'segment'+str(self.cycle+1))
                print(ch)
                writer = pd.ExcelWriter(ch+'.xlsx')
                data_df.to_excel(writer,'page_1')
                writer.save()
                self.List.flatten()
                self.List = np.delete(self.List,0,0)
                self.cycle = self.cycle + 1
                self.List = [[]]


    def OneThirty(self):
        self.List = [[]]

        for m in range(self.Person):
            for k in range(self.Video):
                for l in range(290):
                    print(m, k, l)
                    self.List = np.append(self.List, self.getList[m*self.Video*290 + k*290 + l ])

            ch = str('person'+str(m+1)+'_'+'all'+'_'+'all')
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.set_title(ch)
            DrawMat = np.zeros((8,12))
            print(self.List.shape)
            self.List = np.array(self.List).reshape(4640,3)

            DrawY = np.zeros((4640,1))
            DrawX = np.zeros((4640,1))
            DrawY.fill(0)
            DrawX.fill(0)
            DrawY = self.List[:,0:1]
            DrawX = self.List[:,1:2]
            print(DrawX.shape)
            print(DrawY.shape)
            DrawY = np.ravel(DrawY)
            DrawX = np.ravel(DrawX)

            p = 0
            while  p<4640:
                if(not DrawX[p]==0):
                    pointY = int((DrawY[p] + 180) / 30)
                    pointX = 7 - int((DrawX[p] + 90) / 22.5)
                    #howmuch = howmuch + 1
                    if(DrawY[p]==180):
                        pointY = int((DrawY[p] + 180) / 30) - 1
                    if(DrawX[p]==90):
                        pointX = 7 - int((DrawX[p] + 90) / 22.5) + 1
                #print(pointX, pointY)
                p = p + 1
                DrawMat[pointX][pointY] = DrawMat[pointX][pointY] + 1

            for aa in range(8):
                for bb in range(12):
                    if( not DrawMat[aa][bb]==0):
                        DrawMat[aa][bb] = int(log(DrawMat[aa][bb]))

            plt.matshow(DrawMat, cmap=plt.cm.jet)
            plt.colorbar()
            plt.savefig(ch+'.jpg', dpi=200)
            print(ch)

            data_df = pd.DataFrame(self.List)
            data_df.columns = ['Y','X','Z']
            data_df.index = [str(i) for i in range(4640)]
            writer = pd.ExcelWriter(ch+'.xlsx')
            data_df.to_excel(writer,'page_1')
            writer.save()
            self.List.flatten()
            self.List = np.delete(self.List,0,0)
            self.List = [[]]


    def AllThirty(self):

        self.List = [[]]

        for k in range(self.Video):
            for l in range(290):
                for m in range(self.Person):
                    #print(m, k, n)
                    #print(m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n)
                    #print(self.getList[m*self.Video*290 + k*290 + n])
                    #self.List.append(self.List[self.cycle * self.TimeStep + self.Person * 4640 + self.Video * 290 + n])
                    self.List = np.append(self.List, self.getList[m*self.Video*290 + k*290 + l])
            #print(self.List)
            self.List = np.array(self.List).reshape(44660,3)
            #print(self.List)
            data_df = pd.DataFrame(self.List)
            data_df.columns = ['Y','X','Z']
            data_df.index = [str(i) for i in range(44660)]
            ch = str('all'+'_'+'Video'+str(k+1)+'_'+'all')
            print(ch)
            writer = pd.ExcelWriter(ch+'.xlsx')
            data_df.to_excel(writer,'page_1')
            writer.save()
            self.List.flatten()
            self.List = np.delete(self.List,0,0)
            self.List = [[]]
