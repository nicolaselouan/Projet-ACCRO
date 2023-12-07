from Simulation.simulation_context import SimulationContext

class SolutionComparateur:
    def __init__(self):
        self.comparaison_results={}
    
    def compare_solutions(self,contexts,strategies_name):
        for strategy in strategies_name:
            context=contexts[strategy]

            
            #calcul de l'exactitude
            nb_echecs=0
            total_superficy=0
            unplaced_superficy=0
            
            for bloc in context.modified_data.blocs:
                
                total_superficy+=bloc.width*bloc.length
                
                if bloc.position.zone==context.modified_data.zones[0]:
                    nb_echecs+=1
                    unplaced_superficy+=bloc.width*bloc.length

           

            self.comparaison_results[context.strategy_name]=(context.execution_time, 1-nb_echecs/len(context.modified_data.blocs), 1-unplaced_superficy/total_superficy)
            
        return self.comparaison_results