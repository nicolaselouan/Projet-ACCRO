from Simulation.strategy import Strategy
from Simulation.simulation_context import SimulationContext
from Data.position import Position
from Simulation.is_in_zone_constraint import IsInZoneConstraint
import time


#à la date de début de construction d'un bloc,  on vérifie qu'il est placé dans une des zones (y compris la zonne d'échec). Un bloc ne peut pas changer de position donc on vérie cette condition que lors du placement du bloc.
class Strategy1(Strategy):
    def __init__(self,data):
        self.name="stratégie 1"
        self.simu : SimulationContext = SimulationContext(self.name,data)
    
    
    def launch_strategy(self):
        ti=time.time()
        data=self.simu.modified_data
        
        for i in range(len(data.blocs)):
            data.blocs[i].place(data.zones[0],5,7)

            
        
        self.simu.modified_data=data
        tf=time.time()
        self.simu.execution_time=tf-ti
        pass