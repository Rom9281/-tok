from abc import abstractmethod
import json

class Observer(object):
    @abstractmethod
    def notified(self,string):
        pass

