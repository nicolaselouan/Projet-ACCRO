from copy import deepcopy

class SimulationContext():
    ## Création d'une copie des données afin d'y appliquer les différentes stratégies indépendamment
    def __init__(self,name,data):
        self.strategy_name=name
        self.modified_data=deepcopy(data)
        self.execution_time=None
        