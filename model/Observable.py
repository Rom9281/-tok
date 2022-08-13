from abc import abstractmethod


class Observable(object):
    def __init__(self,*args) -> None:
        self.__observers= args
    
    def _notifyObserver(self):
        for o in self.__observers:
            o(self._convertData())  
    
    @abstractmethod
    def _convertData(self)->str:
        """Method that converts the data to a readable json"""
        pass