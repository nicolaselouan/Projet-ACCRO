from Simulation.strategy import Strategy
from Simulation.simulation_context import SimulationContext
from Data.position import Position
from Simulation.is_in_zone_constraint import IsInZoneConstraint
from Simulation.superposition_constraint import SuperpositionConstraint
import time


#à la date de début de construction d'un bloc,  on vérifie qu'il est placé dans une des zones (y compris la zonne d'échec). Un bloc ne peut pas changer de position donc on vérie cette condition que lors du placement du bloc.
class Strategy2(Strategy):
    def __init__(self,data):
        self.name="stratégie 2"
        self.simu : SimulationContext = SimulationContext(self.name,data)
    
    
    def launch_strategy(self):
        ti=time.time()
        data=self.simu.modified_data

        for i in range(len(data.blocs)-1):
            data.blocs[i].place(data.zones[1],5,data.blocs[i].width)
            if not SuperpositionConstraint(data.blocs[i],data.blocs).isValid():
                print("le bloc", i+1 , "ne peut être placé ici")
            if not IsInZoneConstraint().isValid(data.blocs[i],data.blocs[i].position.zone):
                print("le bloc", i+1 , "n'est pas entièrement compris dans sa zone")
        data.blocs[-1].place(data.zones[2],5,data.blocs[-1].width)
        if not SuperpositionConstraint(data.blocs[-1],data.blocs).isValid():
                print("le bloc 144 ne peut être placé ici")
        if not IsInZoneConstraint().isValid(data.blocs[-1],data.blocs[-1].position.zone):
                print("le bloc 144 n'est pas entièrement compris dans sa zone")
            
        

            
        self.simu.modified_data=data
        tf=time.time()
        self.simu.execution_time=tf-ti
        pass