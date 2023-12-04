from abc import ABC, abstractmethod

class ConstraintsInterface(ABC):
    def __init__(self):
        C=[]
    
    # def instantiate_constraints(self):
    #     constraints_subclasses=ConstraintsInterface.__subclasses__()
    #     for subclass in constraints_subclasses:
    #         C.append(subclass())
    
    @abstractmethod
    def isValid(self):
        pass
    
    
