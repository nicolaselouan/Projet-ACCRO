from Data.data_manager_interface import DataManagerInterface
from Data.bloc import Bloc
from Data.zone import Zone
from Data.load_excel import LoadExcel
from operator import attrgetter


class DataManager(DataManagerInterface):
    def __init__(self, file):
        self.zones : list[Zone] = []
        self.blocs : list[Bloc] = []
        self.excel=LoadExcel(file)
        self.construction_period=()

    def create_failure_zone(self,longueur,largeur):
        # Création d'une zone de dimension à définir où seront stocker les blocs n'ayant pas pu être placés
        self.zones.append(Zone("Zone Echecs",longueur,largeur,None,None))


    def create_construction_zones(self):
        # Création des zones de construction à partir des DataFrame contenant les données nécessaires
        df_zones=self.excel.convert_file_zones()
        nb_zones=len(df_zones['Désignation'])
        for i in range(nb_zones):
            
            self.zones.append(Zone(df_zones['Désignation'][i],
                                   df_zones['Longueur x'][i], 
                                   df_zones['Largeur y '][i], 
                                   df_zones['Distance inter Bloque'][i], 
                                   df_zones['hauteur utile portique'][i]))
        
            
    def create_blocs(self):
        # Création des blocs à partir des DataFrame contenat les données nécessaires
        df_blocs=self.excel.convert_file_blocs()
        nb_blocs=len(df_blocs['Désignation'])
        for i in range(nb_blocs):
            self.blocs.append(Bloc(df_blocs['Désignation'][i], 
                                   df_blocs['Longueur (x)'][i], 
                                   df_blocs['Largeur (y)'][i], 
                                   df_blocs['Hauteur (z)'][i], 
                                   df_blocs['Type'][i], 
                                   df_blocs['Arrivée'][i], 
                                   df_blocs['Départ'][i], 
                                   df_blocs['Date hauteur intermédaire'][i], 
                                   df_blocs['Date hauteur finale'][i]))
        
            
           
    def add_unavaibilities(self):
        # Ajout des éventuelles indisponibiltés des zones de construction
        df_unavaibilities=self.excel.convert_file_unavaibilities()
        nb_unaivabilities=len(df_unavaibilities['zone'])
        for j in range(nb_unaivabilities):
            self.zones[df_unavaibilities['zone'][j]].add_unavaibilities(df_unavaibilities['Début '][j],
                                                                                df_unavaibilities['fin '][j])
    def set_construction_period(self):
        # Calcul de la durée totale de construction des blocs
        min_date=sorted(self.blocs, key=attrgetter('arrival_date'))[0].arrival_date
        max_date=sorted(self.blocs, key=attrgetter('departure_date'))[-1].departure_date
        self.construction_period=(min_date,max_date)