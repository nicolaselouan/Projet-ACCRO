from abc import ABC, abstractmethod


class Strategy(ABC):
        
    @abstractmethod
    def launch_strategy(self,data):
        pass
    


