from abc import abstractmethod
from model.Enums import COLOR
from model.Box import Box
from model.Identifiable import Identifiable
from model.Field import Field
from hashlib import _Hash


class Group(Identifiable):
    """Regroupement d'objets"""
    def __init__(self,field):
        self.__id = Identifiable.__getId()
        self.__boxMap = {}
        self.__field = field
    
    def addBox(self,box)->bool:
        """"Verifies that the objected added is a box the same color of the team"""
        ret = False

        if self.__isValidGroup(box):
            if self._isValidSpecific():
                self.__boxMap[hash(box)]=box
                ret = True
        
        return ret

    @abstractmethod
    def _isValidSpecific(self,box):
        """abstract method to verify if the inserted element is valid"""
        pass

    def __isValidGroup(self,box):
        """Verifies that the box is in the field and is a box"""
        ret = False
        if (isinstance(box,Box)):
            ret = (
                (0<=box.coord[0]<self.__field.getWidth()) and
                (0<=box.coord[1]<self.__field.getHeight())
            )
        
        return ret
    
    def printElements(self):
        print("")
        for element in self.__boxMap.keys:
            prin


    

        
    
