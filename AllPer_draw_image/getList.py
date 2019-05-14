import numpy as np
import h5py

class getList():
    def __init__(self, myFile):
        self.myFile = myFile
        self.element = self.myFile['allvalues']
        #print(self.element.shape)
        #结果是 16*154 的list
        #data 代表从当前目录里读出一个cell储存为list
        #self.Dict = {}
        self.NowList = [[]]
        self.Person = 154
        self.Video = 16

        '''
        #得到总的dict忽略是否为空，每个key对应为一个矩阵
        for i in self.Person:
            for f in self.Video:
                self.Dict['Per'+i]['Vid'+f] = [self.myFile[self.element]]
        '''


        '''
        #print(tempdata)
        tempdata2 = np.zeros((289,3))
        tempdata2.fill(1)
        tempdata2 = tempdata[:,1:4]
        #print(tempdata2)
        #print(tempdata[:,0])
        tempdata2 = np.append(tempdata2, [tempdata2[288]])
        tempdata2 = np.array(tempdata2).reshape(290,3)
        #print(tempdata2)

        #self.NowList.append(tempdata2)
        #print(self.NowList)
        '''


        for i in range(self.Person):
            #逐段取出20截的视频
            for f in range(self.Video):
                #tempdata = Dict['Per'+i]['Vid'+f].shape[0]
                print(i,f)
                tempdata = self.element[f][i]
                #print(tempdata)
                if tempdata.shape[0]==0:
                    tempdata2 = np.zeros((290,3))
                    tempdata2.fill(0)
                else:
                    tempdata2 = np.zeros((289,3))
                    tempdata2.fill(1)
                    tempdata2 = tempdata[:,1:4]
                    tempdata2 = np.append(tempdata2, [tempdata2[288]])
                    tempdata2 = np.array(tempdata2).reshape(290,3)
                #print(tempdata2)

                #self.NowList.append(tempdata2)
                #print(self.NowList)
                #不需要考虑为读取的情况
                #while Dict['Per'+i]['Vid'+f].shape[0] == 0:
                    #tempdata = Dict['Per'+i]['Vid'+f].shape[0]
                #i = i + 1
                #将tempdata的行和列转置得到的是 %*3的list已经过滤了空的cell
                #del tempdata[0]

                self.NowList = np.append(self.NowList,tempdata2)
                #self.NowList = np.array(self.NowList).reshape(16 * 290 * i + (f+1) * 290, 3)
                #print(self.NowList)

        self.NowList = np.array(self.NowList).reshape(self.Video * 290 * self.Person , 3)

        #print(self.NowList.shape)
        #返回的已经处理好的List，顺序是 人/视频/时间
        #print(self.NowList)
        #此时的self.NowList是290 * 154 * 16的array，且保存顺序为 人/视频/时间



'''
a = np.zeros((10,4))
b = np.zeros((10,3))
a.fill(1)
b = a[:,1:4]
'''
