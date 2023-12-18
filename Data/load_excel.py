import pandas as pd

class LoadExcel:
    def __init__(self, file):
        self.excel_file=file
        
    def convert_file_blocs(self):
        # Lecture de la page "Données Colis" de l'excel "donnees_entree" et conversion en DataFrame. Le fichier doit avoir un format précis afin d'être lu
        return pd.DataFrame(pd.read_excel (self.excel_file, 
                                           sheet_name='Données Colis',skiprows=1))
        
    def convert_file_zones(self):
        # Lecture de la page "Zones" de l'excel "donnees_entree" et conversion en DataFrame. Le fichier doit avoir un format précis afin d'être lu
        return pd.DataFrame(pd.read_excel ( self.excel_file, 
                                           sheet_name='Zones'))
        
    def convert_file_unavaibilities(self):
        # Lecture de la page "Indisponibilités zones" de l'excel "donnees_entree" et conversion en DataFrame. Le fichier doit avoir un format précis afin d'être lu
        return pd.DataFrame(pd.read_excel (self.excel_file, 
                                           sheet_name='Indisponibilités zones'))

