from model.Identifiable import Identifiable
from model.Box import Box

class Field(Identifiable):
    def __init__(self, width = 1, height = 1):
        self.__id = Identifiable.__getId()
        self.__width = width
        self.__height = height
        self.__boxField = {}

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