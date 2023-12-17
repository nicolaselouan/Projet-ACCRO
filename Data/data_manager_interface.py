from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
    @abstractmethod
    def create_failure_zone(self,longueur,largeur):
        pass

    @abstractmethod
    def create_construction_zones(self):
        pass
    
    @abstractmethod
    def create_blocs(self):
        pass
        
    @abstractmethod
    def add_unavaibilities(self):
       pass