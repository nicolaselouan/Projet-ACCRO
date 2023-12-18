from Data.data_manager import DataManager
from pathlib import Path
from Simulation.strategy import Strategy
from Simulation.strategy_recuit_simule import StrategyRecuitSimule
from Simulation.strategy_2 import Strategy2
from Simulation.solution_comparateur  import SolutionComparateur

class SimulationManager():
    ## Instanciation d'un jeu de données
    def __init__(self):
        self.data=DataManager(Path(__file__).parent/ "donnees_entree.xlsx")
        self.contexts={}
        self.metrics={}

    ## Initialisation des zones
    def set_zones(self,length_failure_zone,width_failure_zone):    
        self.data.create_failure_zone(length_failure_zone,width_failure_zone)
        self.data.create_construction_zones()
        self.data.add_unavaibilities()
        self.data.set_construction_period()
    
    ## Initialisation des blocs
    def set_blocs(self):
        self.data.create_blocs()
      
    ## Lancement d'une stratégie
    def launch_strategy(self,strategy_name):
        strategies_subclasses=Strategy.__subclasses__()
        exists=False
        for subclass in strategies_subclasses:
            if subclass.__name__==strategy_name:
                strategy=subclass(self.data)
                exists=True
        if exists==False:
            return "Cette stratégie n'est pas implémentées"
        else:
            strategy.launch_strategy()
            self.contexts[strategy.name]=strategy.simu
            return strategy.simu
    
    ## Comparaison des solutions testées
    def compare_solutions(self,strategies_name ):
        self.metrics=SolutionComparateur().compare_solutions(self.contexts,strategies_name)
        
        
        