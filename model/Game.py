from model.Field import Field
from model.Box import Box
from model.Enums import COLOR

class Game():
    def __init__(self, width = 0, heigth = 0,*observers):
        self.__field = Field(width,heigth,*observers)