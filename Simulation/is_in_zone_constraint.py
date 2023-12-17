from Simulation.constraints_interface import ConstraintsInterface

# à chaque fois qu'on ajoute un bloc dans une zone, on vérifie qu'il est compris entièrement dans la zone. Un bloc ne peut pas changer de position donc on vérie cette condition que lors du placement du bloc.
class IsInZoneConstraint(ConstraintsInterface):
        
    def is_valid(self,bloc,position):
        return (position.x >= 0) and (position.y - bloc.width >= 0) and (position.y <= position.zone.width) and (position.x + bloc.length < position.zone.length)