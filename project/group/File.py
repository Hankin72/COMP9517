import os
import cv2
import pandas as pd


class File(object):
    def __init__(self, rootFolder=''):
        self.__rootFolder = rootFolder
        self.name2RGB = {}
        self.index2RGB = []
        self.name2fg = {}
        self.index2fg = []
        self.name2label = {}
        self.index2label = []
        self.name2bbox = {}
        self.index2bbox = []

        self.__imageNameList = []
        self.__csvNameList = []

    def readImage(self, folderName=''):
        if folderName == '':
            fn = self.__rootFolder
        else:
            fn = self.__rootFolder + '/' + folderName
        if self.__folderNotExist(fn):
            raise Exception("Target Folder (%s) not exist. Check or Create it firstly."%fn)
        self.__imageNameList = self.__getPNG(fn)
        for name in self.__imageNameList:
            img = cv2.imread(fn+'/'+name)
            if name[-7:-4] == 'rgb':
                self.name2RGB[name[:-4]] = img
                self.index2RGB.append(img)
            elif name[-9:-4] == 'label':
                self.name2label[name[:-4]] = img
                self.index2label.append(img)
            elif name[-6:-4] == 'fg':
                self.name2fg[name[:-4]] = img
                self.index2fg.append(img)

    def readCSV(self, folderName=''):
        if folderName == '':
            fn = self.__rootFolder
        else:
            fn = self.__rootFolder + '/' + folderName
        if self.__folderNotExist(fn):
            raise Exception("Target Folder (%s) not exist. Check or Create it firstly."%fn)
        self.__csvNameList = self.__getCSV(fn)
        for name in self.__csvNameList:
            file = pd.read_csv(fn+'/'+name)
            if name[-8:-4] == "bbox":
                self.name2bbox[name[:-4]] = file
                self.index2bbox.append(file)

    @staticmethod
    def createFolder(folderName):
        if not os.path.exists(folderName):
            os.mkdir(folderName)
            print("Successfully create. (%s)"%folderName)
        else:
            print("Existed.")

    def __getCSV(self, folderName):
        return [file for file in os.listdir(folderName) if file[-3:]=='csv']

    def __getPNG(self, folderName):
        return [file for file in os.listdir(folderName) if file[-7:]=='rgb.png']

    def __folderNotExist(self, folderName):
        if os.path.exists(folderName):
            return False
        return True



if __name__=='__main__':
    ara2012 = File("Task1")
    ara2012.readImage("Ara2012")
    # print(ara2012.name2RGB)
    print(list(ara2012.name2RGB.keys()))
    ara2012.readCSV("Ara2012")
    # print(ara2012.name2bbox)
    print(list(ara2012.name2bbox.keys()))
