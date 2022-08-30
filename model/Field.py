from model.Identifiable import Identifiable
from model.Observable import Observable
from model.Box import Box
from model.Enums import COLOR

from random import randint
import json

class Field(Identifiable,Observable):
    def __init__(self, width = 1, height = 1,*observers):
        super(Observable).__init__(*observers)
        self.__id = Identifiable.__getId()
        self.__width = width
        self.__height = height
        self.__boxField = self._generateBoxes()
    
    def _generateBoxes(self):
        ret = {}
        for i in range(self.__width):
            for j in range(self.__height):
                rand = randint(0,2)
                ret[hash((i,j))]=Box(COLOR(rand),(i,j))
    
    def _getEmptyBoxes(self)->list:
        ret = []
        for box in self.__boxField.keys:
            if box.color == COLOR.GREY:
                ret.append(box)
        return ret
    
    def _getRandomEmpty(self)->tuple:
        listEmpty = self._getEmptyBoxes()
        rand = randint(0,len(listEmpty)-1)
        return listEmpty[rand].coord()
    
    def _moveColor(self,i,j):
        color = self.__boxField[hash((i,j))].color() # get the color of the moved citizen
        self.__boxField[hash((i,j))].color(COLOR.GREY) # color the old box to grey
        self.__boxField[hash(self._getRandomEmpty())].color(color) # color the new box with the right color
    
    def getBoxColor(self,i,j):
        """The Field class sanitises the input and then returns the right box"""
        i = self.__sanitize(i,self.__height-1)
        j = self.__sanitize(j,self.__width-1)

        return self.__boxField[hash((i,j))].color()

    def __sanitize(self,i,max):
        """Verifies that the input is correct: if -1 give max, and if max+1 give 0"""
        if i<-1 or i>max+1:
            raise ValueError("Invalid input: the input must be between -1 and {}".format(max))
            i=0
        elif i==-1:
            i=max
        elif i==max+1:
            i=0
        
        return i

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def addBox(self,box)->bool:
        """"Verifies that the objected added is a box the same color of the team"""
        ret = False

        if self.__isValid(box):
            self.__boxField[hash(box)]=box
            ret = True
        
        return ret
    
    def __isValid(self,box):
        """Verifies that the box is in the field and is a box"""
        ret = False
        if (isinstance(box,Box)):
            ret = (
                (0<=box.coord[0]<self.__field.getWidth()) and
                (0<=box.coord[1]<self.__field.getHeight())
            )
        
        return ret
    
    def __str__(self):
        ret = "Boxes: \n"
        for box in self.__boxField.keys():
            ret += " - " + str(box) +"\n"
    
    def _convertData(self) -> str:
        """Gets the data and makes it understandable to the notifier"""
        ret = []

        for b in self.__boxField.keys:
            dict = {}
            dict["x"]=str(b.coord[0])
            dict["y"]=str(b.coord[1])
            dict["color"]=b.color.value
            ret.append(dict)
        
        return json.dump(ret)