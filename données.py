from operator import attrgetter
import pandas as pd

class Bloc:
    def __init__(self,longueur, largeur,hauteur, categorie, arrivee, depart, date_mi_hauteur, date_hauteur_finale):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur= 0
        self.hauteur_max= hauteur
        self.categorie= categorie
        self.date_arrivee= arrivee
        self.date_depart= depart
        self.date_mi_hauteur=date_mi_hauteur
        self.date_hauteur_finale=date_hauteur_finale
    
    def mi_hauteur(self): ## on test en externe si la date actuelle est égale à la date de mi-hauteur puis on applique la fonction mi_hauteur()  
        self.hauteur=self.hauteur_max/2
        
    def hauteur_finale(self):  ## on test en externe si la date actuelle est égale à la date de hauteur finale puis on applique la fonction hauteur_finale()
        self.hauteur=self.hauteur_max
    
    pass
        
class Zone:
    def __init__(self, longueur, largeur, distance, hauteur):
        self.longueur = longueur
        self.largeur=largeur
        self.distance_inter_bloque=distance
        self.hauteur_portique=hauteur
        self.indisponibilites=[]
    
    def ajouter_indisponibilite(self, date_debut, date_fin):
        self.indisponibilites.append((date_debut, date_fin))
        
    pass

  

read_file_blocs = pd.read_excel ("donnees_entree.xlsx",sheet_name='Données Colis',skiprows=1)
read_file_zones = pd.read_excel ("donnees_entree.xlsx",sheet_name='Zones')
read_file_indisponibilites_zones = pd.read_excel ("donnees_entree.xlsx",sheet_name='Indisponibilités zones')  


# Write the dataframe object
# into csv file
read_file_blocs.to_csv ("blocs.csv", index = None, header=True)
read_file_zones.to_csv ("zones.csv", index = None, header=True)
read_file_indisponibilites_zones.to_csv ("indisponibilites_zones.csv", index = None, header=True)
    
# read csv file and convert 
# into a dataframe object
blocs = pd.DataFrame(pd.read_csv("blocs.csv"))
zones = pd.DataFrame(pd.read_csv("zones.csv"))
indisponibilites_zones = pd.DataFrame(pd.read_csv("indisponibilites_zones.csv"))


### création de l'ensemble des bjets blocs à placer
nb_blocs=len(blocs['Désignation'])

liste_blocs=[]
for i in range(nb_blocs):
    liste_blocs.append(Bloc(blocs['Longueur (x)'][i], blocs['Largeur (y)'][i], blocs['Hauteur (z)'][i], blocs['Type'][i], blocs['Arrivée'][i], blocs['Départ'][i],blocs['Date hauteur intermédaire'][i], blocs ['Date hauteur finale'][i]))

# rangement des colis par date d'arrivée
liste_blocs=sorted(liste_blocs,key=attrgetter('date_arrivee'))

### création des zones de construction
nb_zones=len(zones['Désignation'])
liste_zones=[]
for i in range(nb_zones):
    liste_zones.append(Zone(zones['Longueur x'][i], zones['Largeur y '][i], zones['Distance inter Bloque'][i], zones['hauteur utile portique'][i]))

# Ajout des indisponibilites pour chaque zones
nb_indisponibilites=len(indisponibilites_zones['zone'])
for j in range(nb_indisponibilites):
    liste_zones[indisponibilites_zones['zone'][j]-1].ajouter_indisponibilite(indisponibilites_zones['Début '][j],indisponibilites_zones['fin '][j])


