from model.Enums import COLOR
from model.Identifiable import Identifiable

class Box(Identifiable):
    """Model for one of the boxes of the solitary"""

    def __init__(self, color=COLOR.GREY, coord=(0,0)):
        self.__id = Identifiable.__getId()
        self.__color = color
        self.__coord = coord

    def __str__(self) -> str:
        return "BOX {}: COLOR = {} | COORD = {}".format(self.__id,self.__color,self.__coord)
    
    def __hash__(self) -> int:
        return hash(self.__coord)
        
    @property
    def color(self):
        return self.__color

    @property
    def coord(self):
        return self.__coord
    
    @color.setter
    def color(self,c):
        if(isinstance(c,COLOR)):
            self.__color=c
        else:
            raise TypeError("Not the right type")
    
