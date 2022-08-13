class Identifiable(object):
    """Methode used to give an id to each object"""
    __id = -1

    @classmethod
    def __getId():
        # Creates a 
        Identifiable.__id = Identifiable.__id + 1
        return Identifiable.__id