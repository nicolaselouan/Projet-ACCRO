from copy import deepcopy

class SimulationContext():
    def __init__(self,name,data):
        self.strategy_name=name
        self.modified_data=deepcopy(data)
        self.execution_time=None
        