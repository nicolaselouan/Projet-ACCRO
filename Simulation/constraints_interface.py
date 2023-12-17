from abc import ABC, abstractmethod

class ConstraintsInterface(ABC):
                
    @abstractmethod
    def is_valid(self,bloc,position):
        pass
    
    
