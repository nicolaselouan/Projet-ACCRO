from Simulation.constraints_interface import ConstraintsInterface

## à chaque fois qu'on ajoute un bloc dans une zone, on vérifie qu'il n'y a pas de superpostion à la fois spatiale et temporelle avec l'ensemble des blocs compris dans cette zone
class SuperpositionConstraint(ConstraintsInterface):
    def __init__(self ,bloc,blocs):
        self.blocs=blocs
        self.zone=bloc.position.zone #zone à laquelle appartient le bloc
        self.current_bloc=bloc
        
    def temporal_superposition(self, bloc_1, bloc_2):
        return (bloc_2.arrival_date <= bloc_1.arrival_date <= bloc_2.departure_date) or (bloc_2.arrival_date <= bloc_1.departure_date <= bloc_2.departure_date) or (bloc_1.arrival_date <= bloc_2.arrival_date <= bloc_1.departure_date)
    

    def x_superposition(self, bloc_1, bloc_2):
        return bloc_1.position.x + bloc_1.length + self.zone.distance >= bloc_2.position.x >= bloc_1.position.x + self.zone.distance \
            or bloc_1.position.x + bloc_1.length + self.zone.distance >= bloc_2.position.x + bloc_2.length >= bloc_1.position.x + self.zone.distance \
                or bloc_2.position.x + bloc_2.length + self.zone.distance >= bloc_1.position.x >= bloc_2.position.x - self.zone.distance
        
    def y_superposition(self, bloc_1, bloc_2):
        return bloc_1.position.y + self.zone.distance >= bloc_2.position.y >= bloc_1.position.y - bloc_1.width - self.zone.distance \
            or bloc_1.position.y + self.zone.distance >= bloc_2.position.y  >= bloc_1.position.y - bloc_1.width - self.zone.distance \
                or bloc_2.position.y + self.zone.distance >= bloc_1.position.y >= bloc_2.position.y - bloc_2.width - self.zone.distance
        
    def isValid(self):
        superposition=False
        for bloc in self.blocs:
            if bloc.isPlaced() and bloc.position.zone==self.zone and bloc.name!=self.current_bloc.name :
                if self.temporal_superposition(bloc, self.current_bloc):
                    #print(bloc.arrival_date,bloc.departure_date)
                    #print(self.current_bloc.arrival_date,self.current_bloc.departure_date)
                    if self.x_superposition(bloc, self.current_bloc):
                        if self.x_superposition(bloc, self.current_bloc):
                            superposition=True
        return not superposition