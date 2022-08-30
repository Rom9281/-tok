from view.Observer import Observer
import json
import numpy as np

class ConsoleView(Observer):
    def __init__(self,width,height) -> None:
        self.__array = np.zeros((width,height))

        
    def _notified(self, string):
        """Converts the json string to a dictionary and then displays it"""
        for dict in json.loads(string):
            num = 0

            if(dict["color"]=="WHITE"):num=1
            elif(dict["color"]=="BLACK"):num=2

            # Changing the value of the array
            self.__array[int(dict["x"]),int(dict["y"])] = num

        

    