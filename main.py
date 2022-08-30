from turtle import width
from model.Game import Game
from view.ConsoleView import ConsoleView

#Infomation:

width = 10
height = 10

view = ConsoleView(width,height)
game = Game(width,height,view)
game.play()