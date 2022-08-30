from model.Field import Field
from model.Box import Box
from model.Enums import COLOR

from time import sleep
import numpy as np
from random import randint

class Game(object):
    def __init__(self, width = 1, heigth = 1,neighbors = 4,*observers):
        self.__width =width
        self.__heigth =heigth
        self.__neighbors = neighbors
        self.__field = Field(width,heigth,*observers)

        # Matrix displaying happiness:
        self.__statusMatrix = np.ones((width,heigth))
        self.__flag = True
    
    def play(self):
        while self.__flag:
            self._checkHappiness()
            self._moveRandUnhappy()
            self.__field.notifyObserver()
    
    def _checkHappiness(self):
        for i in range(self.__width):
            for j in range(self.__heigth):
                color = self.__field.getBoxColor(i,j)
                self.__statusMatrix[i,j]=1
                if (color != COLOR(0)) and (self._countSameColorNeighbor(i,j,color)<self.__neighbors):
                        self.__statusMatrix[i,j]=0

    def _countSameColorNeighbor(self,i,j,color)->int:
        """Counts the number of neighbors with the same color"""
        ret = 0

        for k in [-1,0,1]:
            for l in [-1,0,1]:
                if k!=l and (color==self.__field.getBoxColor(i+k,j+l)):
                    ret +=1
        
        return ret
    
    def _moveRandUnhappy(self):
        listUnhappy = self._findUnhappy()
        if(len(listUnhappy)!=0):
            rand = randint(0,len(listUnhappy)-1)
            tupleCoord = listUnhappy[rand]
            self.__field._moveColor(tupleCoord[0],tupleCoord[1])
        else:
            input("End of game")
    
    def _findUnhappy(self)->list:
        ret = []
        for i in range(self.__width):
            for j in range(self.__heigth):
                if self.__statusMatrix[i,j] == 0:
                    ret.append((i,j))
        return ret



