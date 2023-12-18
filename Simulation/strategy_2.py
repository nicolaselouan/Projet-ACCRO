from Simulation.strategy import Strategy
from Simulation.simulation_context import SimulationContext
from Data.position import Position
import time
from Simulation.constraints_motor import ConstraintsMotor


#à la date de début de construction d'un bloc,  on vérifie qu'il est placé dans une des zones (y compris la zonne d'échec). Un bloc ne peut pas changer de position donc on vérie cette condition que lors du placement du bloc.
class Strategy2(Strategy):
    def __init__(self,data):
        self.name=self.__class__.__name__
        self.simu : SimulationContext = SimulationContext(self.name,data)
    
    
    # Stratégie non optimale permettant de comparer les résultats
    def launch_strategy(self):
        
        ti=time.time()
        data=self.simu.modified_data
        constraints_motor=ConstraintsMotor(data.blocs)
        
        # On essaye de placer tous les blocs dans la zone 1, si contrantes non respectées, on les mets dans la zone d'échecs
        for i in range(len(data.blocs)-1):
            pos=Position(data.zones[1],5,data.blocs[i].width)
            if constraints_motor.verify_constraints(data.blocs[i],pos)==True:
                data.blocs[i].place(pos)
            else:
                data.blocs[i].place(Position(data.zones[0],0,data.blocs[i].width))
                
        # On met le dernier bloc dans la zone 2
        pos=Position(data.zones[2],5,data.blocs[i].width)
        if constraints_motor.verify_constraints(data.blocs[-1],pos)==True:
            data.blocs[-1].place(pos)
        else:
            data.blocs[-1].place(Position(data.zones[0],0,data.blocs[i].width))

            
            
        self.simu.modified_data=data
        tf=time.time()
        self.simu.execution_time=tf-ti
        pass