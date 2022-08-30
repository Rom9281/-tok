from turtle import width
from model.Game import Game
from view.ConsoleView import ConsoleView
from view.TkView import TkView

# Infomation:

## The dimentions of the playing field
width = 50
height = 100

## Number of neighbors to be happy:
neighbors = 3 

#consoleView = ConsoleView(width,height)
tkView = TkView(width,height)
game = Game(width,height,neighbors,tkView)

game.play()