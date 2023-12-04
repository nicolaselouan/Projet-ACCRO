from data_manager import DataManager
from pathlib import Path


Data=DataManager(Path(__file__).parent / "donnees_entree.xlsx")
Data.create_failure_zone(20,80)
Data.create_construction_zones()
Data.create_blocs()
Data.add_unavaibilities()
Data.set_construction_period()


Data.blocs[6].place(5,7,Data.zones[1])
print(Data.zones[1].blocs[0].name)
