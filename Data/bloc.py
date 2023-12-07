from Data.position import Position

class Bloc:
    def __init__(self, name, length, width,height, type, arrival_date, departure_date,
                 half_height_date, final_height_date):
        self.name : str =name
        self.length : float = length
        self.width : float = width
        self.height : float = 0
        self.max_height : float = height
        self.type : str = type
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.half_height_date : float = half_height_date
        self.final_height_date : float = final_height_date
        self.position : Position=None
        self.is_placed : bool = False
    
    def update_height(self, new_height):
        self.height=new_height ## date=half_height_date : height <- final_height/2
                               ## date=final_height_date : height <- final_height
                               ## on test la date en externe (dans les algorithmes de résolution)
        
    def place(self, position):
        assert not self.is_placed ## avant de placer un bloc, on vérifie qu'il n'a pas déjà été placé. Cela garantit que les blocs ne sont pas déplacés (changement position et zone) sur leur période de construction
        self.is_placed = True
        self.position = position
        
    def isPlaced(self):
        return self.position!= None

        