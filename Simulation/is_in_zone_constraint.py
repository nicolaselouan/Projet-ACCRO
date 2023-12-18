from Simulation.constraints_interface import ConstraintsInterface

# A chaque fois qu'on ajoute un bloc dans une zone, on vérifie qu'il est compris entièrement dans la zone
class IsInZoneConstraint(ConstraintsInterface):
        
    def is_valid(self,bloc,position):
        k=1
        if (position.x < 0) or (position.y< 0) or (position.y + bloc.width> position.zone.width) or (position.x + bloc.length > position.zone.length):
            k=0
        return k