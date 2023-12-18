from Simulation.constraints_interface import ConstraintsInterface

## à chaque fois qu'on ajoute un bloc dans une zone, on vérifie qu'il n'y a pas de superpostion à la fois spatiale et temporelle avec l'ensemble des blocs compris dans cette zone
class SuperpositionConstraint(ConstraintsInterface):
    def __init__(self,blocs):
        self.blocs=blocs

        
    def is_valid(self,current_bloc,position):
        k=1
        for bloc in self.blocs:
              if bloc.isPlaced() and bloc.position.zone==position.zone and bloc.name!=current_bloc.name :
                blocs=[bloc,current_bloc]
                bloc1=blocs[0]
                bloc2=blocs[1]
                x1, y1 = bloc1.position.x, bloc1.position.y
                x2, y2 = position.x,position.y
                
                ## Superposition temporelle
                date=(bloc2.arrival_date <= bloc1.arrival_date <= bloc2.departure_date or bloc1.arrival_date <= bloc2.arrival_date <= bloc1.departure_date)
                
                ## Superposition spatiale
                intersection=(min(x1,x2) + blocs[[x1,x2].index(min(x1,x2))].length >= max(x1,x2) and min(y1,y2) + blocs[[y1,y2].index(min(y1,y2))].width >= max(y1,y2))
                
                ## Si superposition spatiale et temporelle, condition non respectée
                if date and intersection:
                    k=0
        
        return k
