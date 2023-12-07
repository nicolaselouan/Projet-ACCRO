from Simulation.constraints_interface import ConstraintsInterface
from Simulation.superposition_constraint import SuperpositionConstraint
from Simulation.is_in_zone_constraint import IsInZoneConstraint

class ConstraintsMotor():
    

    def __init__(self,blocs):
        self.C=[IsInZoneConstraint(),SuperpositionConstraint(blocs)]
        
    # def instantiate_constraints(self,blocs):
    #     subclasses=ConstraintsInterface.__subclasses__()
    #     print(subclasses)
    #     self.C.append(subclasses[0]())
    #     self.C.append(subclasses[1](blocs))
    
    
    def verify_constraints(self,bloc,position):
        score=True
        for c in self.C:
            score=score and c.is_valid(bloc,position)
        return score