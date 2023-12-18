from Simulation.constraints_interface import ConstraintsInterface
from Simulation.superposition_constraint import SuperpositionConstraint
from Simulation.is_in_zone_constraint import IsInZoneConstraint

class ConstraintsMotor():
    

    def __init__(self,blocs):
        self.C=[IsInZoneConstraint(),SuperpositionConstraint(blocs)]
        
    # Si une des contraintes n'est pas respectée, renvoie 0. Sinon, renvoie 1.
    def verify_constraints(self,bloc,position):
        score=1
        for c in self.C:
            score=score*c.is_valid(bloc,position)
        return score