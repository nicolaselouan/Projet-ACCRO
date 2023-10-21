from operator import attrgetter
import pandas as pd


class Bloc:
    def __init__(self, id, longueur, largeur,hauteur, categorie, arrivee, depart, date_mi_hauteur, date_hauteur_finale, zone):
        self.id=id
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur= 0
        self.hauteur_max= hauteur
        self.categorie= categorie
        self.date_arrivee= arrivee
        self.date_depart= depart
        self.date_mi_hauteur=date_mi_hauteur
        self.date_hauteur_finale=date_hauteur_finale
        self.zone=zone
        self.position=(0,0)
    
    def mi_hauteur(self): ## on test en externe si la date actuelle est égale à la date de mi-hauteur puis on applique la fonction mi_hauteur()  
        self.hauteur=self.hauteur_max/2
        
    def hauteur_finale(self):  ## on test en externe si la date actuelle est égale à la date de hauteur finale puis on applique la fonction hauteur_finale()
        self.hauteur=self.hauteur_max
        
    def changer_postion(self,x,y):
        self.position=(x,y)
        
    def attribuer_zone (self,zone):
        self.zone=zone
        
    pass


        
class Zone:
    def __init__(self,id, longueur, largeur):
        self.id=id
        self.longueur = longueur
        self.largeur=largeur
        self.blocsContenus=[]

    pass



class ZoneEchecs(Zone):
    
    pass



class ZoneConstruction(Zone):
    def __init__(self, id, distance, hauteur, longueur, largeur):
        super().__init__(id,longueur,largeur)
        self.hauteur_portique=hauteur
        self.indisponibilites=[]
        self.blocsContenus=[]
        
    def ajouter_indisponibilite(self, date_debut, date_fin):
        self.indisponibilites.append((date_debut, date_fin))
            
        pass
    
    
    
class JeuDeDonnees:
    def __init__(self, fichier):
        self.fichierExcel=fichier
        self.fichierBlocs=pd.DataFrame()
        self.fichierZones=pd.DataFrame()
        self.fichierIndisponibilites=pd.DataFrame()
        self.zones=[]
        self.blocs=[]
        
    def excelToDataFrame(self):
        # Lecture des dichiers CSV et conversion en DataFrame. Le fichier doit avoir un format précis afin d'être lu
        self.fichierBlocs = pd.DataFrame(pd.read_excel (self.fichierExcel, sheet_name='Données Colis',skiprows=1))
        self.fichierZones = pd.DataFrame(pd.read_excel ( self.fichierExcel, sheet_name='Zones'))
        self.fichierIndisponibilites = pd.DataFrame(pd.read_excel (self.fichierExcel, sheet_name='Indisponibilités zones'))
    
    def creerZonesConstruction(self):
        # Création des zones de construction à partir des DataFrame contenat les données nécessaires
        nb_zones=len(self.fichierZones['Désignation'])
        for i in range(nb_zones):
            self.zones.append(ZoneConstruction(self.fichierZones['Désignation'],self.fichierZones['Longueur x'][i], self.fichierZones['Largeur y '][i], self.fichierZones['Distance inter Bloque'][i], self.fichierZones['hauteur utile portique'][i]))

    def creerZoneEchecs(self,longueur,largeur):
        # Création d'une zone de dimension à définir où seront stocker les blocs n'ayant pas pu être placés
        self.zones.append(ZoneEchecs("Zone Echecs",longueur,largeur))
            
    def creerBlocs(self):
        # Création des blocs à partir des DataFrame contenat les données nécessaires
        nb_blocs=len(self.fichierBlocs['Désignation'])

        for i in range(nb_blocs):
            self.blocs.append(Bloc(self.fichierBlocs['Désignation'][i], self.fichierBlocs['Longueur (x)'][i], self.fichierBlocs['Largeur (y)'][i], self.fichierBlocs['Hauteur (z)'][i], self.fichierBlocs['Type'][i], self.fichierBlocs['Arrivée'][i], self.fichierBlocs['Départ'][i], self.fichierBlocs['Date hauteur intermédaire'][i], self.fichierBlocs['Date hauteur finale'][i], self.zones[0]))
            ## Tous les blocs sont initialement dans la zone contenant les échecs de placement. Il est donc nécessaire d'appeler la méthode creerZoneEchec avant
            
    def ajouterIndisponibilites(self):
        # Ajout des éventuelles indisponibiltés des zones de construuction
        nb_indisponibilites=len(self.fichierIndisponibilites['zone'])
        for j in range(nb_indisponibilites):
            self.zones[self.fichierIndisponibilites['zone'][j]].ajouter_indisponibilite(self.fichierIndisponibilites['Début '][j],self.fichierIndisponibilites['fin '][j])
            
            
            
    pass
    

  

Data=JeuDeDonnees("donnees_entree.xlsx")
Data.excelToDataFrame()
Data.creerZoneEchecs(20,80)
Data.creerZonesConstruction()
Data.creerBlocs()
Data.ajouterIndisponibilites()


sorted(Data.blocs, key=attrgetter('date_arrivee'))
print(Data.blocs[50].zone)



