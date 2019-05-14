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
                        #print(m, k, n)
                        #print(m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n)
                        #print(self.getList[m*self.Video*290 + k*290 + n])
                        #self.List.append(self.List[self.cycle * self.TimeStep + self.Person * 4640 + self.Video * 290 + n])
                        self.List = np.append(self.List, self.getList[(m)*self.Video*290 + k*290 + l ])
                #print(self.List)
                self.List = np.array(self.List).reshape(290,3)
                #print(self.List)
                #print(m, k, l)
                ch = str('person'+str(m+1)+'_'+'Video'+str(k+1)+'_'+'all')
                DrawY = np.zeros((290,1))
                DrawX = np.zeros((290,1))
                DrawY.fill(0)
                DrawX.fill(0)
                DrawY = self.List[:,1:2]
                DrawX = self.List[:,0:1]
                DrawY = np.ravel(DrawY)
                DrawX = np.ravel(DrawX)
                #print(DrawY)
                #print(DrawX)
                fig = plt.figure()
                ax1 = fig.add_subplot(111)
                ax1.set_title(ch)
                plt.xlabel('Y')
                plt.ylabel('X')
                ax1.scatter(DrawX, DrawY, c='r', marker='o')

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

                plt.savefig(ch+'.jpg', dpi=200)



                data_df = pd.DataFrame(self.List)
                data_df.columns = ['Y','X','Z']
                data_df.index = [str(i) for i in range(290)]
                #ch = str('person'+str(m+1)+'_'+'Video'+str(k+1)+'_'+'all')
                print(ch)
                writer = pd.ExcelWriter(ch+'.xlsx')
                data_df.to_excel(writer,'page_1')
                writer.save()

                self.List.flatten()
                self.List = np.delete(self.List,0,0)
                self.List = [[]]


    def AllThirty(self):

        self.List = [[]]
        NewList = [[]]

        for k in range(self.Video):
            ch = str('all'+'_'+'Video'+str(k+1)+'_'+'all')
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.set_title(ch)
            howmuch = 0
            DrawMat = np.zeros((8,12))
            for l in range(290):
                for m in range(self.Person):
                    #print(k, l, m)
                    #print(m*self.Video*290 + k*290 + self.cycle*self.TimeStep + n)
                    #print(self.getList[m*self.Video*290 + k*290 + n])
                    #self.List.append(self.List[self.cycle * self.TimeStep + self.Person * 4640 + self.Video * 290 + n])
                    self.List = np.append(self.List, self.getList[m*self.Video*290 + k*290 + l])
                    NewList = np.append(NewList, self.getList[m*self.Video*290 + k*290 + l])
                NewList = np.array(NewList).reshape(154,3)
                #print(NewList.shape)
                DrawY = np.zeros((154,1))
                DrawX = np.zeros((154,1))
                DrawY.fill(0)
                DrawX.fill(0)
                DrawY = NewList[:,0:1]
                DrawX = NewList[:,1:2]
                NewList = [[]]
                DrawY = np.ravel(DrawY)
                DrawX = np.ravel(DrawX)
                p = 0
                while  p<154:
                    if(not DrawX[p]==0):
                        pointY = int((DrawY[p] + 180) / 30)
                        pointX = 7 - int((DrawX[p] + 90) / 22.5)
                        howmuch = howmuch + 1
                        if(DrawY[p]==180):
                            pointY = int((DrawY[p] + 180) / 30) - 1
                        if(DrawX[p]==90):
                            pointX = 7 - int((DrawX[p] + 90) / 22.5) + 1
                    p = p + 1
                    DrawMat[pointX][pointY] = DrawMat[pointX][pointY] + 1
            print(DrawMat)
            #DrawArray = np.array(DrawMat).T
            for aa in range(8):
                for bb in range(12):
                    if( not DrawMat[aa][bb]==0):
                        DrawMat[aa][bb] = int(log(DrawMat[aa][bb]))
            plt.matshow(DrawMat, cmap=plt.cm.jet)
            plt.colorbar()
            plt.savefig(ch+'.jpg', dpi=200)
            '''
            f, (ax1, ax2) = plt.subplots(figsize=(6,6),nrows=2)
            sns.heatmap(oo, annot=True, ax=ax1)
            sns.heatmap(oo, annot=True, ax=ax2, annot_kws={'size':9,'weight':'bold', 'color':'blue'})
            plt.show()
            '''
            #print('do1')
            #plt.savefig(ch+'.jpg', dpi=200)
            #print('do2')
            print(ch)

            '''
            self.List = np.array(self.List).reshape(44660,3)
            #print(self.List)
            data_df = pd.DataFrame(self.List)
            data_df.columns = ['Y','X','Z']
            data_df.index = [str(i) for i in range(44660)]
            #ch = str('all'+'_'+'Video'+str(k+1)+'_'+'all')
            writer = pd.ExcelWriter(ch+'.xlsx')
            data_df.to_excel(writer,'page_1')
            writer.save()

            self.List.flatten()
            self.List = np.delete(self.List,0,0)
            '''

            self.List = [[]]
