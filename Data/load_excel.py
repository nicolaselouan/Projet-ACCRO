import pandas as pd

class LoadExcel:
    def __init__(self, file):
        self.excelFile=file
        
    def convert_file_blocs(self):
        # Lecture des dichiers CSV et conversion en DataFrame. Le fichier doit avoir un format précis afin d'être lu
        return pd.DataFrame(pd.read_excel (self.excelFile, 
                                           sheet_name='Données Colis',skiprows=1))
        
    def convert_file_zones(self):
        return pd.DataFrame(pd.read_excel ( self.excelFile, 
                                           sheet_name='Zones'))
        
    def convert_file_unavaibilities(self):
        return pd.DataFrame(pd.read_excel (self.excelFile, 
                                           sheet_name='Indisponibilités zones'))

