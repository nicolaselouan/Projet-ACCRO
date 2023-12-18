from Simulation.strategy import Strategy
from Simulation.simulation_context import SimulationContext
from Data.position import Position
from Simulation.constraints_motor import ConstraintsMotor
import time


#à la date de début de construction d'un bloc,  on vérifie qu'il est placé dans une des zones (y compris la zonne d'échec). Un bloc ne peut pas changer de position donc on vérie cette condition que lors du placement du bloc.
class StrategyExemple(Strategy):
    def __init__(self,data):
        self.name=self.__class__.__name__
        self.simu : SimulationContext = SimulationContext(self.name,data)
    
    
    def launch_strategy(self):
        ti=time.time()
        data=self.simu.modified_data

        
        ###### COMPLETER AVEC VOTRE ALGORITHME #######
        
        # accéder à une zone: data.zones[i]
        # atrributs zone: name,length, width, distance, height_portique, unavaibilities
        # accéder à la valeur d'un attribut d'une zone: data.zones[i].name
        
        # accéder à un bloc: data.blocs[i]
        # atrributs blocs: name,length, width, max_height,type, arrival_date, departure_date, half_height_date, final_height_date, position, is_placed (booleen)
        # accéder à ma valeur d'un attribut d'un bloc: data.blocs[i].name
        # modifier un attribut de bloc: data.blocs[i].name="new name"
        
        # data.blocs[i].position est un objet avec 3 attributs: zone, x, y
        
        # définir une position (x,y) pour le bloc i dans la zone j:
            # 1) Instancier un objet position
            # pos=Position(data.zones[i],x,y)
            # 2) Vérifier que les contraintes sont respectées 
            # constraints_motor=ConstraintsMotor(data.blocs)
            # if constraints_motor.verify_constraints(data.blocs[i],pos)==True:
            # 3) Si elles sont vérifiées, placer le bloc
            #data.blocs[-1].place(pos)
            #    Sinon le mettre dans la zone d'échec (ici, il est placé dans le coin inférieur gauche)
            # else:
            #     data.blocs[i].place(Postion(data.zones[0],0,data.blocs[i].width))
        # /!\ toujours vérifier que les contraintes sont respectées avant de placer un bloc
        
        ####################################
        
        
        self.simu.modified_data=data
        tf=time.time()
        self.simu.execution_time=tf-ti
        pass