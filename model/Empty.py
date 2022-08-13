from model.Enums import COLOR
from model.Box import Box
from model.Identifiable import Identifiable
from model.Group import Group
from hashlib import _Hash


class Team(Group):
    def __init__(self):
        super().__init__()
        self.__color = COLOR.GREY
    
    def _isValid(self,box):
        return (box.getColor()==self.__color)