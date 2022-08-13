from model.Identifiable import Identifiable
from model.Observable import Observable
from model.Box import Box
from random import randint
from Enums import COLOR

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