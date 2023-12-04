from Data.zone import Zone

class Position:
    def __init__(self,zone,x,y):
        self.zone : Zone = zone;
        self.x : float =x
        self.y : float =y