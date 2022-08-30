import math,json,tkinter as tk
from view.Observer import Observer

class TkView(Observer):
    def __init__(self,width,height):
        self.__root = tk.Tk()
        self.__px_width = 500
        self.__px_height = 1500
        
        width = math.floor(self.__px_width/width)
        height = math.floor(self.__px_height/height)

        self.__box_size = min(width,height)
        
        self.__canvas = tk.Canvas(self.__root,bg="BLACK",height=self.__px_height,width=self.__px_width)
    
    def notified(self, string):
        self.__canvas.delete("rect")

        for dict in json.loads(string):
            p0 = (int(dict["x"])*self.__box_size,int(dict["y"])*self.__box_size)
            p1 = (self.__box_size*(int(dict["x"])+1),self.__box_size*(int(dict["y"])+1))
            self.__canvas.create_rectangle(p0[0],p0[1],p1[0],p1[1],fill=dict["color"][6:],outline=dict["color"][6:],tags="rect")
        
        self.__canvas.pack()
        self.__root.update()
            

            


    