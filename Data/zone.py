from Data.unavaibility import Unavaibility

class Zone:
    def __init__(self,name , length, width, distance, height):
        self.name : str = name
        self.length : float = length
        self.width : float =width
        self.distance : float =distance
        self.height_portique : float =height
        self.unavaibilities: list[Unavaibility]=[]

    # Ajout d'une indisponibilités pour cette zone
    def add_unavaibilities(self, beginning, end):
        self.unavaibilities.append(Unavaibility(beginning, end))
        