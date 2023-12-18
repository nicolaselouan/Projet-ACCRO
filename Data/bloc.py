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
                               ## tester la date en externe (dans les algorithmes de résolution)
        
    # place un bloc à une position dans une zone
    def place(self, position):
        self.is_placed = True
        self.position = position
        
    # Renseigne si le bloc est placé ou non
    def isPlaced(self):
        return self.position!= None

        