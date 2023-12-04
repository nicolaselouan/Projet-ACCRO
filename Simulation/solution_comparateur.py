from Simulation.simulation_context import SimulationContext

class SolutionComparateur:
    def __init__(self):
        self.comparaison_results={}
    
    def compare_solutions(self,contexts,strategies_name):
        for strategy in strategies_name:
            context=contexts[strategy]

            
            #calcul de l'exactitude
            nb_echecs=0
            accuracy=0
            for i in range(len(context.modified_data.blocs)):
                if context.modified_data.blocs[i].position.zone==context.modified_data.zones[0]:
                    nb_echecs+=1
            accuracy=1-nb_echecs/len(context.modified_data.blocs)
           

            self.comparaison_results[context.strategy_name]=(context.execution_time, accuracy)
            
        return self.comparaison_results