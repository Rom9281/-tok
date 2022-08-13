from model.Identifiable import Identifiable
from model.Team import Team 

class Field(Identifiable):
    def __init__(self, width = 1, height = 1):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def 