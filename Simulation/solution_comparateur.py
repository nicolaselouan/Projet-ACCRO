from Simulation.simulation_context import SimulationContext

class SolutionComparateur:
    def __init__(self):
        self.comparaison_results={}
    
    def compare_solutions(self,contexts,strategies_name):
        # Pour chaque stratégies dont le nom est dans la liste strategies_name,
        # renvoie un dictionnaire {strategy_name: (execution_time, nb_failures, nb_failures/nb_blocs, surface_failures_blocs/surface_blocs)}
        for strategy in strategies_name:
            context=contexts[strategy]

            
            #calcul de l'exactitude selon différents paramètres
            nb_echecs=0
            total_superficy=0
            unplaced_superficy=0
            
            for bloc in context.modified_data.blocs:
                
                total_superficy+=bloc.width*bloc.length
                
                if bloc.is_placed and bloc.position.zone==context.modified_data.zones[0]:
                    nb_echecs+=1
                    unplaced_superficy+=bloc.width*bloc.length

           

            self.comparaison_results[context.strategy_name]=(context.execution_time, nb_echecs, 1-nb_echecs/len(context.modified_data.blocs), 1-unplaced_superficy/total_superficy)
            
        return self.comparaison_results