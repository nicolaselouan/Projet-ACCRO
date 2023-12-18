from Data.zone import Zone

class Position:
    # Instancie une position dans une zone pour un bloc
    def __init__(self,zone,x,y):
        self.zone : Zone = zone;
        self.x : float =x
        self.y : float =y