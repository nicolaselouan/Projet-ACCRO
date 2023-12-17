from Simulation.constraints_interface import ConstraintsInterface

## à chaque fois qu'on ajoute un bloc dans une zone, on vérifie qu'il n'y a pas de superpostion à la fois spatiale et temporelle avec l'ensemble des blocs compris dans cette zone
class SuperpositionConstraint(ConstraintsInterface):
    def __init__(self,blocs):
        self.blocs=blocs

        
    def temporal_superposition(self, bloc_1, bloc_2):
        return (bloc_2.arrival_date <= bloc_1.arrival_date <= bloc_2.departure_date) or (bloc_2.arrival_date <= bloc_1.departure_date <= bloc_2.departure_date) or (bloc_1.arrival_date <= bloc_2.arrival_date <= bloc_1.departure_date)
    

    def x_superposition(self, placed_bloc, bloc_to_place, position):
        return placed_bloc.position.x + placed_bloc.length + position.zone.distance >= position.x >= placed_bloc.position.x + position.zone.distance \
            or placed_bloc.position.x + placed_bloc.length + position.zone.distance >= position.x + bloc_to_place.length >= placed_bloc.position.x + position.zone.distance \
                or position.x + bloc_to_place.length + position.zone.distance >= placed_bloc.position.x >= position.x - position.zone.distance
        
    def y_superposition(self, placed_bloc, bloc_to_place, position):
        return placed_bloc.position.y + position.zone.distance >= position.y >= placed_bloc.position.y - placed_bloc.width - position.zone.distance \
            or placed_bloc.position.y + position.zone.distance >= position.y - bloc_to_place.width  >= placed_bloc.position.y - placed_bloc.width - position.zone.distance \
                or position.y + position.zone.distance >= placed_bloc.position.y >= position.y - bloc_to_place.width - position.zone.distance
        
    def is_valid(self,current_bloc,position):
        superposition=False
        for bloc in self.blocs:
            if bloc.isPlaced() and bloc.position.zone==position.zone and bloc.name!=current_bloc.name :
                if self.temporal_superposition(bloc, current_bloc):
                    #print(bloc.arrival_date,bloc.departure_date)
                    #print(self.current_bloc.arrival_date,self.current_bloc.departure_date)
                    if self.x_superposition(bloc, current_bloc,position):
                        if self.y_superposition(bloc, current_bloc,position):
                            superposition=True
        return not superposition