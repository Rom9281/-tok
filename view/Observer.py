from abc import abstractmethod
import json

class Observer(object):
    @abstractmethod
    def _notified(self,string):
        pass
