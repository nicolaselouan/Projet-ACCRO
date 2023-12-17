import tkinter as tk
import datetime
from operator import itemgetter
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pickle

#########################################
#####################################################################################
#Fenêtre principale
#####################################################################################        
#########################################

#Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Interface")

#En termes de dimensions de la fenêtre, on a décidé de ne pas utiliser de valeurs numériques mais d'utiliser une fonction tkinter qui adapte la fenêtre aux dimensions du PC de chaque utilisateur. En effet, avec 
#des valeurs numériques l'entièreté de la fenêtre ne s'affichait pas. Néanmoins, ces fonctions ont réglé partiellement le problème étant donné que pour certains d'entre nous, toute la fenêtre s'affiche mais 
#la zone C est plus ou moins "ratatinée". Sur un PC 17 pouces, aucun souci a priori.
Largeur = fenetre.winfo_screenwidth()
Hauteur = fenetre.winfo_screenheight()

#Ajustement de la taille de la fenêtre
fenetre.geometry(f"{Largeur}x{Hauteur}")

#Cadre principal qui remplit la fenêtre et contiendra tous nos cadres
cadre_principal = tk.Canvas(fenetre, width=Largeur, height=Hauteur)
cadre_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
cadre_principal.focus_set()

#Cadre de droite contenant la cadre des échecs et les outils interactifs
cadre_droite = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_droite.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=False)

#Titre du cadre des échecs
label_dechargement = tk.Label(cadre_droite, text="Échecs de placement", bg="white", font=("Helvetica", 10, "bold"))
label_dechargement.pack()

#Création du cadre "Échecs de placement"
zone_echecs = tk.Canvas(cadre_droite, bg='white', relief="solid", bd=2)
zone_echecs.pack(fill=tk.BOTH, expand=True)

#Création du menu déroulant contenant les différentes solutions créées
options = ["Solution_1", "Solution_2", "Solution_3"]
var = tk.StringVar(cadre_droite)
var.set(options[0])
menu_deroulant = ttk.Combobox(cadre_droite, textvariable=var, values=options, state="readonly", font=("Helvetica", 10, "bold"))
menu_deroulant.pack(pady=10)

#Cadre de gauche contenant les cadres A, B et C
cadre_zones = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_zones.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

#Titre du cadre A
label_a = tk.Label(cadre_zones, text="A", bg="white", font=("Helvetica", 14, "bold"))
label_a.pack()

#Création du cadre A
cadre_A = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_A.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(0, 10))

#Titre du cadre B
label_b = tk.Label(cadre_zones, text="B", bg="white", font=("Helvetica", 14, "bold"))
label_b.pack()

#Création du cadre B
cadre_B = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_B.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(0, 10))

#Titre du cadre C
label_c = tk.Label(cadre_zones, text="C", bg="white", font=("Helvetica", 14, "bold"))
label_c.pack()

#Création du cadre C
cadre_C = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_C.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(0, 10))

#########################################
#####################################################################################
#Redimensionnement proportionnel des blocs par rapport aux dimensions de la fenêtre 
#####################################################################################        
#########################################

#On met à jour la fenêtre pour récupérer ses dimensions réelles
fenetre.update()

#On récupère les dimensions des cadres A, B et C qui ne sont pas les mêmes que celles spécifiées sur l'excel du client d'où le redimensionnement
longueur_cadre_A = cadre_A.winfo_width()
largeur_cadre_A = cadre_A.winfo_height()

longueur_cadre_B = cadre_B.winfo_width()
largeur_cadre_B = cadre_B.winfo_height()

longueur_cadre_C = cadre_C.winfo_width()
largeur_cadre_C = cadre_C.winfo_height()

#Nos listes contenant le placement des blocs sont stockées à la fin de nos algorithmes dans des fichiers pkl. Nous les récupérons ici. Il faut pour cela que les fichiers pkl soient dans le même répertoire que
#le code de l'interface
with open('placés.pkl', 'rb') as fichier:
    colis_placer_pas_corrigé = pickle.load(fichier)

with open('non_placés.pkl', 'rb') as fichier:
    colis_pas_placer_pas_corrigé = pickle.load(fichier)

#Les blocs des listes que nous avons récupéré ont des coordonnées de placement en rapport aux dimensions réelles des zones de l'excel. On va corriger ces dimensions pour les adapter aux dimensions des zones de 
#de la fenêtre. On initialise donc deux nouvelles listes qui vont contenir les coordonnées redimensionnées des blocs.    
colis_placer = []
colis_pas_placer = []

#Pour ce faire, on itère sur tous les blocs et on applique une simple règle de trois sur les dimensions et coordonnées des blocs en fonction de la zone dans laquelle ils sont placés.
for bloc in colis_placer_pas_corrigé :
    if bloc[3] == "A" :
        x,y = bloc[4]
        bon_x, bon_y = x*longueur_cadre_A/200, y*largeur_cadre_A/100
        premier_bloc = [bloc[0], bloc[1]*longueur_cadre_A/200, bloc[2]*largeur_cadre_A/100, bloc[3], (bon_x, bon_y), bloc[5], bloc[6]]
        colis_placer.append(premier_bloc)

    if bloc[3] == "B" :
        x,y = bloc[4]
        bon_x, bon_y = x*longueur_cadre_B/200, y*largeur_cadre_B /50
        premier_bloc = [bloc[0], bloc[1]*longueur_cadre_B/200, bloc[2]*largeur_cadre_B/50, bloc[3], (bon_x, bon_y), bloc[5], bloc[6]]
        colis_placer.append(premier_bloc)

    if bloc[3] == "C" :
        x,y = bloc[4]
        bon_x, bon_y = x*longueur_cadre_C/200, y*largeur_cadre_C/70
        premier_bloc = [bloc[0], bloc[1]*longueur_cadre_C/200, bloc[2]*largeur_cadre_C/70, bloc[3], (bon_x, bon_y), bloc[5], bloc[6]]
        colis_placer.append(premier_bloc)

#Pour les blocs non placés, on a décidé de ne pas appliquer de redimensionnement pour les voir tous s'afficher, même à la fin de la simulation, dans la zone d'échecs de placement. Leurs tailles affichées dans 
#sur l'interface n'ont donc pas de sens. Si on souhaite avoir leurs tailles réelles, pour un PC 17 pouces, faire bloc[1]*longueur_cadre_A/200 et bloc[2]*largeur_cadre_A/100.
for bloc in colis_pas_placer_pas_corrigé :
    premier_bloc = [bloc[0], bloc[1], bloc[2], bloc[3], bloc[4], bloc[5]]
    colis_pas_placer.append(premier_bloc)

#Le format des deux listes sont les suivants : 
    
#Liste de blocs placés avec succès : [nom du bloc (str), longueur du bloc (float), largeur du bloc (float), cadre du bloc (str), position du bloc (tuple), date d’arrivée (datetime), date de départ (datetime)]

#Liste de blocs dont le placement par la solution a été un échec : [nom du bloc (str), longueur du bloc (float), largeur du bloc (float), cadre du bloc (int affecté à 0 pour désigner le cadre des échecs), 
# position du bloc (tuple affecté à (0,0) car pas positionné dans un cadre), date d’arrivée (datetime)]    

#########################################
#####################################################################################
#Dictionnaires de résultats statistiques
#####################################################################################
#########################################

#Dictionnaires de résultats de performances des solutions : {nombre de blocs essai 1 : [temps d’exécution de la méthode essai 1, nombre d’échecs essai 1], 
# nombre de blocs essai 2 : [temps d’exécution de la méthode essai 2, nombre d’échecs essai 2]...}
dico_graphs_1 = {10 : [0.1933281421661377, 0], 20 : [0.1986069679260254, 0], 30 : [0.1997363567352295, 1], 40 : [0.2014472484588623, 8], 50 : [0.2020094394683838, 11], 
60 : [0.21062731742858887, 13], 70 : [0.21291136741638184, 15], 80 : [0.21526145935058594, 19], 90 : [0.22150564193725586, 20], 100 : [0.22606587409973145, 25], 110 : [0.22754406929016113, 29],
120 : [0.2287590503692627, 33], 130 : [0.23115205764770508, 36], 140 : [0.23501968383789062, 36], 144 : [0.23964333534240723, 36]}
dico_graphs_2 = {10 : [0.9792091846466064, 0], 20 : [4.881898641586304, 0], 30 : [11.584029912948608, 0], 40 : [23.66120409965515, 0], 50 : [36.18730425834656, 0], 
60 : [45.44558262825012, 0], 70 : [60.2792067527771, 0], 80 : [177.81695818901062, 4], 90 : [253.44459700584412, 5], 100 : [567.0963599681854, 7], 110 : [225.0635588169098, 6],
120 : [511.2513632774353, 12], 130 : [585.7637026309967, 17], 140 : [964.1056299209595, 18], 144 : [812.6922860145569, 18]}
dico_graphs_3 = {10 : [1.5, 0], 20 : [3.676, 0], 30 : [9.93, 0], 40 : [16.3, 0], 50 : [106, 0], 
60 : [154, 0], 70 : [205, 0], 80 : [562, 3], 90 : [710, 3], 100 : [877, 5], 110 : [1121, 5],
120 : [1166, 7], 130 : [1300, 16], 140 : [1525, 17], 144 : [1644, 18]}
dico_graphs_4 = {10 : [0.06623077392578125, 0], 20 : [0.15211153030395508, 0], 30 : [0.37021970748901367, 0], 40 : [0.6754333972930908, 0], 50 : [1.0357334613800049, 2], 
60 : [1.38037109375, 2], 70 : [1.9455807209014893, 0], 80 : [2.262704849243164, 7], 90 : [3.179025888442993, 10], 100 : [3.6743712425231934, 11], 110 : [4.654669284820557, 12],
120 : [5.677810907363892, 15], 130 : [6.264504909515381, 21], 140 : [7.259113073348999, 21], 144 : [7.978237628936768, 25]}
dico_graphs_5 = {10 : [0.1779487133026123, 0], 20 : [0.9560625553131104, 0], 30 : [2.418804168701172, 0], 40 : [6.548795938491821, 0], 50 : [11.539744138717651, 1], 
60 : [20.442336559295654, 0], 70 : [31.656405210494995, 0], 80 : [42.97293472290039, 6], 90 : [58.7303900718689, 8], 100 : [71.90343284606934, 9], 110 : [114.66914939880371, 10],
120 : [127.9127402305603, 16], 130 : [170.86997961997986, 26], 140 : [199.96358799934387, 27], 144 : [223.78487062454224, 28]}
dico_graphs_6 = {10 : [0.19920587539672852, 0], 20 : [1.0290002822875977, 0], 30 : [2.651641368865967, 0], 40 : [7.341662645339966, 0], 50 : [26.174131631851196, 0], 
60 : [22.020224571228027, 0], 70 : [38.091978549957275, 0], 80 : [97.47574400901794, 6], 90 : [118.2109317779541, 8], 100 : [143.52417707443237, 9], 110 : [203.65474152565002, 10],
120 : [268.36929631233215, 15], 130 : [307.8017511367798, 22], 140 : [403.9320890903473, 23], 144 : [401.95777225494385, 25]}

#########################################
#####################################################################################
#Graphiques 
#####################################################################################
#########################################

#Tri des dictionnaires par ordre croissant de nombre de blocs qui vont être nos abscisses de courbes
dico_graphs_1 = dict(sorted(dico_graphs_1.items()))
dico_graphs_2 = dict(sorted(dico_graphs_2.items()))
dico_graphs_3 = dict(sorted(dico_graphs_3.items()))
dico_graphs_4 = dict(sorted(dico_graphs_4.items()))
dico_graphs_5 = dict(sorted(dico_graphs_5.items()))
dico_graphs_6 = dict(sorted(dico_graphs_6.items()))

#On liste l'ensemble des nombre de blocs testés lors des essais des solutions
nombre_de_blocs_1 = list(dico_graphs_1.keys())
nombre_de_blocs_2 = list(dico_graphs_2.keys())
nombre_de_blocs_3 = list(dico_graphs_3.keys())
nombre_de_blocs_4 = list(dico_graphs_4.keys())
nombre_de_blocs_5= list(dico_graphs_5.keys())
nombre_de_blocs_6 = list(dico_graphs_6.keys())

#On liste les temps d'exécution relevés lors des essais des solutions
temps_execution_1 = [value[0] for value in dico_graphs_1.values()]
temps_execution_2 = [value[0] for value in dico_graphs_2.values()]
temps_execution_3 = [value[0] for value in dico_graphs_3.values()]
temps_execution_4 = [value[0] for value in dico_graphs_4.values()]
temps_execution_5 = [value[0] for value in dico_graphs_5.values()]
temps_execution_6 = [value[0] for value in dico_graphs_6.values()]

#On liste le nombre d'échecs de placement relevés lors des essais des solutions
nombre_echecs_1 = [value[1] for value in dico_graphs_1.values()]
nombre_echecs_2 = [value[1] for value in dico_graphs_2.values()]
nombre_echecs_3 = [value[1] for value in dico_graphs_3.values()]
nombre_echecs_4 = [value[1] for value in dico_graphs_4.values()]
nombre_echecs_5 = [value[1] for value in dico_graphs_5.values()]
nombre_echecs_6 = [value[1] for value in dico_graphs_6.values()]

#####################################################################################
#FONCTION: afficher_courbes_analyse
#OBJECTIF : Analyser les différentes solutions d'optimisation des ressources
#ENTRÉES : /
#NOTES  : /
#SORTIES : Affiche trois courbes analytiques. La première est le temps d'exécution de la solution en fonction du nombre de blocs à placer.
#          La seconde est le nombre d'échecs de placement de blocs en fonction du nombre de blocs à placer. 
#          La troisième est un scatter montrant quelle méthode est la plus performante sur le placement de l'ensemble des blocs.
#####################################################################################
def afficher_courbes_analyse():
    #On crée un subplot pour afficher nos deux graphiques sur la même fenêtre
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(22, 6))

    #Trace les courbes pour les temps d'exécution
    ax1.plot(nombre_de_blocs_1, temps_execution_1, label='Temps d\'exécution High-Left V1', marker='o', linestyle='-.', color='b')
    ax1.plot(nombre_de_blocs_2, temps_execution_2, label='Temps d\'exécution Recuit simulé', marker='o', linestyle='-.', color='g')
    ax1.plot(nombre_de_blocs_3, temps_execution_3, label='Temps d\'exécution Algorithme génétique V1', marker='o', linestyle='-.', color='r')
    ax1.plot(nombre_de_blocs_4, temps_execution_4, label='Temps d\'exécution High-Left V2', marker='o', linestyle='-.', color='y')
    ax1.plot(nombre_de_blocs_5, temps_execution_5, label='Temps d\'exécution Client', marker='o', linestyle='-.', color='k')
    ax1.plot(nombre_de_blocs_6, temps_execution_6, label='Temps d\'exécution Algorithme génétique V2', marker='o', linestyle='-.', color='m')

    #Configure les détails du graphique 1
    ax1.set_xlabel('Nombre de blocs')
    ax1.set_ylabel('Temps d\'exécution (s)')
    ax1.set_title('Comparaison des solutions - Temps d\'exécution')
    ax1.legend()
    ax1.grid(True)

    #Trace les courbes pour le nombre d'échecs
    ax2.plot(nombre_de_blocs_1, nombre_echecs_1, label='Nombre d\'échecs High-Left V1', marker='o', linestyle='--', color='b')
    ax2.plot(nombre_de_blocs_2, nombre_echecs_2, label='Nombre d\'échecs Recuit simulé', marker='o', linestyle='--', color='g')
    ax2.plot(nombre_de_blocs_3, nombre_echecs_3, label='Nombre d\'échecs Algorithme génétique V1', marker='o', linestyle='--', color='r')
    ax2.plot(nombre_de_blocs_4, nombre_echecs_4, label='Nombre d\'échecs High-Left V2', marker='o', linestyle='--', color='y')
    ax2.plot(nombre_de_blocs_5, nombre_echecs_5, label='Nombre d\'échecs Client', marker='o', linestyle='--', color='k')
    ax2.plot(nombre_de_blocs_6, nombre_echecs_6, label='Nombre d\'échecs Algorithme génétique V2', marker='o', linestyle='--', color='m')

    #Configure les détails du graphique 2
    ax2.set_xlabel('Nombre de blocs')
    ax2.set_ylabel('Nombre d\'échecs')
    ax2.set_title('Comparaison des solutions - Nombre d\'échecs')
    ax2.legend()
    ax2.grid(True)

    #Trace les courbes pour la précision
    ax3.scatter(temps_execution_1[-1], (145 - nombre_echecs_1[-1]) / 145, label='Précision High-Left V1', marker='o', color='b')
    ax3.scatter(temps_execution_2[-1], (145 - nombre_echecs_2[-1]) / 145, label='Précision Recuit simulé', marker='o', color='g')
    ax3.scatter(temps_execution_3[-1], (145 - nombre_echecs_3[-1]) / 145, label='Précision Algorithme génétique V1', marker='o', color='r')
    ax3.scatter(temps_execution_4[-1], (145 - nombre_echecs_4[-1]) / 145, label='Précision High-Left V2', marker='o', color='y')
    ax3.scatter(temps_execution_5[-1], (145 - nombre_echecs_5[-1]) / 145, label='Précision Client', marker='o', color='k')
    ax3.scatter(temps_execution_6[-1], (145 - nombre_echecs_6[-1]) / 145, label='Précision Algorithme génétique V2', marker='o', color='m')


    #Configure les détails du graphique 3
    ax3.set_xlabel('Temps d\'exécution (s)')
    ax3.set_ylabel('Précision du modèle (blocs placés/blocs totaux)')
    ax3.set_title('Comparaison des solutions - Scatter de précision')
    ax3.legend()
    ax3.grid(True)

    #Crée une fenêtre pour afficher les graphiques
    new_window = tk.Toplevel(fenetre)
    new_window.title('Courbes d\'analyse')

    #Incorpore les graphiques dans la fenêtre
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

#########################################
#####################################################################################
#Déplacement par drag (souris maintenue) des blocs dans les cadres A, B et C pour discuter manuellement des choix faits par les solutions
#####################################################################################
#########################################

# Variable de détection du clic souris pour la zone A
DETECTION_CLIC_SUR_OBJET_A = False

#####################################################################################
#FONCTION: drag_A
#OBJECTIF : Déplacer les blocs du cadre A
#ENTRÉES : event - clic gauche de la souris
#NOTES  : 1) Le déplacement du bloc se limite aux frontières du cadre A.
#         2) Eviter de "drager" un bloc et passer la souris sur un autre. En effet, en "dragant" un bloc et en passant sur un autre bloc, l'un et l'autre peuvent s'attirer indépendamment de la volonté de 
#            l'utilisateur. Dans un tel cas, faire des mouvements de souris rapides de droite à gauche tout en maintenant le drag peut séparer ces blocs.
#SORTIES : Le bloc sur lequel on clique dans le cadre A va se mouvoir en suivant notre souris
#####################################################################################
def drag_A(event):
    global DETECTION_CLIC_SUR_OBJET_A

    #Position du pointeur de la souris
    x = event.x
    y = event.y
    print("Position du clic -> ", x, y)

    #On récupère l'ensemble des blocs créés dans placer_bloc
    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_A : 
            coords = values[2].coords(values[0])
            x_min, y_min, x_max, y_max = coords

            #On vérifie que le clic est compris dans le bloc
            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_A = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_A)
            else:
                DETECTION_CLIC_SUR_OBJET_A = False
            
            #Dans ce cas...
            if DETECTION_CLIC_SUR_OBJET_A:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]
                print("Largeur bloc = ", LargeurBloc)
                print("Hauteur bloc = ", HauteurBloc)

                print("x =", x)
                #...on redirige la souris au centre du bloc pour que le drag soit plus facile 
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                print("x =", x)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()
                
                print("Largeur cadre = ", cadre_width)
                print("Hauteur cadre = ", cadre_height)
                #Limite le bloc à l'intérieur du cadre A
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                #Met à jour la position du bloc dans le cadre A
                cadre_A.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                #Met à jour la position du titre du bloc dans le cadre A
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_A.coords(values[1], x_texte, y_texte)    


# Variable de détection du clic souris pour la zone B
DETECTION_CLIC_SUR_OBJET_B = False

#####################################################################################
#FONCTION: drag_B
#OBJECTIF : Déplacer les blocs du cadre B
#ENTRÉES : event - clic gauche de la souris
#NOTES  : 1) Le déplacement du bloc se limite aux frontières du cadre B.
#         2) Eviter de "drager" un bloc et passer la souris sur un autre. En effet, en "dragant" un bloc et en passant sur un autre bloc, l'un et l'autre peuvent s'attirer indépendamment de la volonté de 
#            l'utilisateur. Dans un tel cas, faire des mouvements de souris rapides de droite à gauche tout en maintenant le drag peut séparer ces blocs.
#SORTIES : Le bloc sur lequel on clique dans le cadre B va se mouvoir en suivant notre souris
#####################################################################################
def drag_B(event):
    global DETECTION_CLIC_SUR_OBJET_B

    #Position du pointeur de la souris
    x = event.x
    y = event.y

    #On récupère l'ensemble des blocs créés dans placer_bloc
    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_B : 
            coords = values[2].coords(values[0])
            x_min, y_min, x_max, y_max = coords
            
            #On vérifie que le clic est compris dans le bloc
            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_B = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_B)
            else:
                DETECTION_CLIC_SUR_OBJET_B = False
            
            #Dans ce cas...
            if DETECTION_CLIC_SUR_OBJET_B:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]

                #...on redirige la souris au centre du bloc pour que le drag soit plus facile
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()

                print("Largeur cadre = ", cadre_width)
                print("Hauteur cadre = ", cadre_height)
                
                #Limite le bloc à l'intérieur du cadre B
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                #Met à jour la position du bloc dans le cadre B
                cadre_B.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                #Met à jour la position du titre du bloc dans le cadre B
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_B.coords(values[1], x_texte, y_texte)   

# Variable de détection du clic souris pour la zone C
DETECTION_CLIC_SUR_OBJET_C = False

#####################################################################################
#FONCTION: drag_C
#OBJECTIF : Déplacer les blocs du cadre C
#ENTRÉES : event - clic gauche de la souris
#NOTES  : 1) Le déplacement du bloc se limite aux frontières du cadre C.
#         2) Eviter de "drager" un bloc et passer la souris sur un autre. En effet, en "dragant" un bloc et en passant sur un autre bloc, l'un et l'autre peuvent s'attirer indépendamment de la volonté de 
#            l'utilisateur. Dans un tel cas, faire des mouvements de souris rapides de droite à gauche tout en maintenant le drag peut séparer ces blocs.
#SORTIES : Le bloc sur lequel on clique dans le cadre C va se mouvoir en suivant notre souris
#####################################################################################
def drag_C(event):
    global DETECTION_CLIC_SUR_OBJET_C

    #Position du pointeur de la souris
    x = event.x
    y = event.y
    
    #On récupère l'ensemble des blocs créés dans placer_bloc
    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_C : 
            coords = values[2].coords(values[0])
            x_min, y_min, x_max, y_max = coords
            
            #On vérifie que le clic est compris dans le bloc
            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_C = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_C)
            else:
                DETECTION_CLIC_SUR_OBJET_C = False
            
            #Dans ce cas...
            if DETECTION_CLIC_SUR_OBJET_C:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]

                #...on redirige la souris au centre du bloc pour que le drag soit plus facile
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()

                print("Largeur cadre = ", cadre_width)
                print("Hauteur cadre = ", cadre_height)
                
                #Limite le bloc à l'intérieur du cadre C
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                #Met à jour la position du bloc dans le cadre C
                cadre_C.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                #Met à jour la position du titre du bloc dans le cadre C
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_C.coords(values[1], x_texte, y_texte)   


#########################################
#####################################################################################
#Gestion du temps
#####################################################################################        
#########################################

#On va d'abord procéder à une phase de tri car on veut ordonner chronologiquement les actions des blocs
blocs = colis_placer + colis_pas_placer
liste_bloc_arrivee = []

for bloc in blocs:
    #Si le bloc a une date de départ (cas des blocs placés)...
    if len(bloc) == 7:  
        #...on ajoute le bloc, la date d'arrivée et la date de départ
        liste_bloc_arrivee.append((bloc, bloc[-2], bloc[-1]))
    else:
        #...on ajoute que le bloc et la date d'arrivée
        liste_bloc_arrivee.append((bloc, bloc[-1], None))

#On trie cette liste chronologiquement en fonction de la date d'arrivée des blocs
liste_bloc_arrivee = sorted(liste_bloc_arrivee, key=itemgetter(1))

#On garde de cette liste ce qui nous intéresse : les blocs 
arrivee_trie = [bloc[0] for bloc in liste_bloc_arrivee]

#On trie aussi par ordre chronologique le départ des blocs 
depart_trie = sorted(colis_placer, key=lambda x: x[6])

#On initialise une liste vide dans laquelle...
taches = []

#...on recopie arrive_trie mais en précisant pour chaque bloc la nature de l'action (arrivée) associée
for bloc in arrivee_trie:
    taches.append((bloc, "arrivee"))

#...on recopie depart_trie à la suite mais en précisant pour chaque bloc la nature de l'action (départ) associée
for bloc in depart_trie:
    taches.append((bloc, "disparition"))

#On trie cette liste chronologiquement et on obtient finalement la liste des blocs ordonnée chronologiquement avec leur action associée dans un tuple
taches_triees = sorted(taches, key=lambda x: x[0][5] if x[1] == "arrivee" else x[0][6])

#On récupère la date la plus récente et la plus lointaine de toutes les actions possibles (arrivée ou départ du bloc)
if colis_pas_placer:
    temps_debut = min(min(bloc[5] for bloc in colis_placer), min(bloc[5] for bloc in colis_pas_placer))
    temps_fin = max(max(bloc[6] for bloc in colis_placer), max(bloc[5] for bloc in colis_pas_placer)) 
else:
    temps_debut = min(bloc[5] for bloc in colis_placer)
    temps_fin = max(bloc[6] for bloc in colis_placer)

print("Date début :", temps_debut)
print("Date fin :", temps_fin)

#On va évoluer temporellement avec des secondes. Ce choix a été fait au moment de l'implémentation du code pour utiliser des comparateurs simples sans risquer des erreurs de syntaxe avec d'autres unités.
#La pertinence de ce choix sera à réévaluer lors d'une prochaine version.

#On calcule en secondes la durée totale de la simulation 
duree_simulation = (temps_fin - temps_debut).total_seconds()  # en secondes
print("Durée simulation : ", duree_simulation)

#On va procéder avec une échelle par semaines. On calcule donc le nombre de semaines que sépare la date la plus récente de la plus lointaine...
delta = temps_fin - temps_debut
nombre_semaines = delta.days // 7
reste_jours = delta.days % 7

if reste_jours > 0 :
    nombre_semaines += 1
print(f"Le nombre de semaines entre les deux dates extrêmes est : {nombre_semaines}")

#... puis on calcule le pas de la simulation
pas_simulation = duree_simulation/nombre_semaines
print("Pas simulation :", pas_simulation)

#On initialise en secondes le temps actuel qui évoluera au cours de la simulation
temps_actuel = 0
print("Temps actuel : ", temps_actuel)

#On veut rendre compte sur notre fenêtre de l'évolution temporelle de la simulation donc on crée un label qui affichera la date courante
label_temps = tk.Label(cadre_droite, text=f"Date :", fg="black", bg="white", font=("Helvetica", 10, "bold"), borderwidth=2, relief="raised")
label_temps.pack()

#Variable qui va faire le lien entre toutes les fonctions interactives de la fenêtre en rendant compte si oui ou non, la simulation de placement de blocs est en cours 
current_task_id = None

#####################################################################################
#FONCTION: executer_taches
#OBJECTIF : S'occuper de la gestion temporelle et des actions de la simulation
#ENTRÉES : /
#NOTES  : /
#SORTIES : /
#####################################################################################
def executer_taches():
    global current_task_id, temps_actuel, taches_launch
    
    #Date courante de la simulation évoluant dans le temps par pas d'une semaine toutes les secondes
    date_complete = temps_debut + datetime.timedelta(seconds=temps_actuel)
    print("Jour actuel :", date_complete.strftime("%d-%m-%Y"))

    #Boucle while qui gère toutes les actions (arrivée et départ) des blocs en fonction de la date courante (= temps_actuel en secondes)
    #Le principe est tel que tant qu'il y a des actions à faire et que la date courante est supérieure à la date prévue de n actions, ces n actions se fassent
    while taches_launch and ((temps_actuel >= (taches_launch[0][0][5] - temps_debut).total_seconds() and taches_launch[0][1] == "arrivee") or (taches_launch[0][1] == "disparition" and temps_actuel >= (taches_launch[0][0][6] - temps_debut).total_seconds())):
            
            #On pop les actions concernées de sorte à ne plus les refaire une fois sa date passée.
            tache = taches_launch.pop(0)

            #On récupère le bloc et l'action associée au bloc
            bloc, action = tache[0], tache[1]

            #Si cette action est une arrivée, on place le bloc dans son cadre mais si c'est une disparition, on enlève le bloc du cadre. 
            #On met à jour aussi un compteur d'actions restants à faire au cours de la simulation.
            if action == "arrivee":
                placer_bloc(bloc)
                label_compteur.config(text=f"Nombre d'étapes à accomplir : {len(taches_launch)}")

            elif action == "disparition":
                effacer_bloc(bloc)
                label_compteur.config(text=f"Nombre d'étapes à accomplir : {len(taches_launch)}")

    print(taches_launch) 

    #S'il n'y a plus de tâches ou si la date courante dépasse la date maximale prévue alors on signale que la simulation de placement de blocs s'interrompt aux autres fonctions avec current_task_id
    #puis on stoppe la simulation
    if not taches_launch or temps_actuel > duree_simulation:
        current_task_id = None
        return
    
    #On actualise le label du temps avec la date courante
    label_temps.config(text=f"Date : {date_complete.strftime('%d-%m-%Y')}")

    #On fait avancer le temps de la simulation avec le pas temporel
    temps_actuel += pas_simulation
    print("Temps actuel : ", temps_actuel)

    #On fait avancer la simulation toutes les 1000 millisecondes (= 1 seconde). Aussi 1 seconde réelle correspond à 1 semaine dans la simulation
    current_task_id = fenetre.after(1000, executer_taches) 

#########################################
#####################################################################################
#Gestion des actions
#####################################################################################        
#########################################

#Un dictionnaire stockant les blocs créés, leurs titres et leurs cadres et utile notamment pour les fonctions drag et effacer_bloc
dico_blocs = {}  

#Variable servant à différencier de façon unique chaque bloc
bloc_counter = 0

#Variables de coordonnées des blocs échecs
liste_y = [0]
x1, x2, y1 = 0, 0, 0

#####################################################################################
#FONCTION: placer_bloc
#OBJECTIF : Placer un bloc dans le cadre qui lui est destiné
#ENTRÉES : bloc - un bloc
#NOTES  : /
#SORTIES : /
#####################################################################################
def placer_bloc(bloc):
    global bloc_counter, liste_y, x1, x2, y1

    #Ces premiers if permet de définir le cadre concerné par le placement du bloc
    if bloc[3] == "A":
        canvas = cadre_A
    elif bloc[3] == "B":
        canvas = cadre_B
    elif bloc[3] == "C":
        canvas = cadre_C

    #Ce second if permet de différencier un bloc à placer d'un bloc à échec de placement. Ici, la condition est que le bloc soit à placer dans un cadre A, B ou C     
    if bloc[3] != 0:

        #Pour placer un bloc, on a besoin des coordonnées des 4 coins du bloc. On récupère donc les deux premiers issus des coordonnées en entrées et on calcule
        #les deux derniers en s'aidant de la hauteur et de la largeur du bloc
        a1, b1 = bloc[4]
        a2 = a1 + bloc[1]
        b2 = b1 + bloc[2]

        #On peut créer ce bloc dans le bon cadre
        bloc_rectangle = canvas.create_rectangle(a1, b1, a2, b2, fill="lightgrey", outline="black", width=2)

        #On crée puis on place le titre du bloc au centre du bloc avec l'aide des coordonnées du bloc
        texte = "{}".format(bloc[0])
        x_texte = (a1 + a2) / 2
        y_texte = (b1 + b2) / 2
        texte_id = canvas.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 8, "bold"))

        #On ajoute au bloc, bloc_rectangle, qui, même si dans la fenêtre représente un bloc rectangulaire, est dans l'algorithme un id du bloc.
        #Cela sera utile pour l'effacer à sa date de départ.
        bloc.append(bloc_rectangle)

        #On complète le dictionnaire notamment utile pour les fonctions drag et identifier un bloc pour l'effacer à sa date de départ
        dico_blocs[bloc_counter] = (bloc_rectangle, texte_id, canvas)

        #On incrémente notre clé du dictionnaire pour qu'elle diffère bien tous les blocs de façon unique
        bloc_counter += 1
    
    #Cas où le blocs est un bloc à échec de placement. Ce else est particulier du fait que dans les entrées, tous les blocs de la liste des blocs non-placés ont comme coordonnées (0,0).
    #Seuls nous sont donnés leurs dimensions. Pourtant, il faut bien les placer dans le cadre prévu à cet effet. De ce fait, ce qui suit est un petit algorithme de placement de blocs optimisant "grossièrement" 
    #l'espace alloué par le cadre "Echecs de placement" en plaçant les blocs à échecs de gauche à droite et de haut en bas.
    else:
        #On récupère les 4 coordonnées du bloc en question avec sa largeur et sa hauteur
        x2 = bloc[1] + x2
        y2 = y1 + bloc[2]

        #Cette condition permet d'éviter que le bloc en question ne sorte du cadre "Echecs de placement" si sa largeur dépasse l'abscisse du cadre 
        if x2 > cadre_droite.winfo_width():

            #Dans un tel cas, on revient tout à gauche du cadre en imposant l'abscisse gauche du nouveau bloc à 0 et sa nouvelle ordonnée comme l'ordonnée maximale des blocs de la 1ère rangée complétée pour éviter 
            #que les blocs se superposent
            x1, x2, y1, y2 = 0, bloc[1], max(liste_y), max(liste_y) + bloc[2]

            #On peut réinitialiser la liste stockant les ordonnées des blocs de chaque rangée
            liste_y = []

        ##On peut créer le bloc à échec dans le cadre "Echecs de placement"
        bloc_rectangle = zone_echecs.create_rectangle(x1, y1, x2, y2, fill="lightgrey", outline="black", width=2)

        #On crée puis on place le titre du bloc au centre du bloc avec l'aide des coordonnées du bloc
        texte = "{}".format(bloc[0])
        x_texte = (x1 + x2) / 2
        y_texte = (y1 + y2) / 2
        texte_id = zone_echecs.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 8, "bold"))
        
        #On ajoute l'ordonnée du bloc placé dans la liste stockant les ordonnées de la rangée et on affecte la coordonnée en abscisse gauchedu prochain bloc comme la coordonnée en abscisse droite du bloc précédent
        liste_y.append(y2)
        x1 = x2

#####################################################################################
#FONCTION: effacer_bloc
#OBJECTIF : Effacer un bloc du cadre où il se trouve
#ENTRÉES : bloc - un bloc
#NOTES  : /
#SORTIES : /
#####################################################################################
def effacer_bloc(bloc):
    global dico_blocs

    #On s'assure que le bloc en question est bien dans un des trois cadres A, B ou C car sinon, il se trouve dans le cadre "Echecs de placement" et aucun d'entre eux n'ont de date de départ
    if bloc[3] != 0:

        #On récupère toutes les caractéristiques des blocs placés jusque ici
        for key, value in dico_blocs.items():
            
            #On cherche le bloc en argument de la fonction en comparant les id du bloc avec ceux qu'on a stockés en les plaçant
            if value[0] == bloc[-1]: 
                canvas = value[2]
                
                #On supprime le bloc, son titre du cadre, puis on supprime le bloc en question du dictionnaire et on break la boucle for vu que cette fonction efface un bloc à la fois. On a pas besoin de vérifier 
                #le reste des blocs
                canvas.delete(value[0]) 
                canvas.delete(value[1])
                del dico_blocs[key]
                break

#########################################
#####################################################################################
#Gestion des boutons de l'interface
#####################################################################################        
#########################################

#On va introduire un curseur qui va avoir deux intérêts. D'abord, quand on changera son index à n, la fenêtre affichera les n premières actions de la simulation en image fixe.
#Puis un bouton launch permettra à l'index n, de lancer la simulation des n premières actions.

#On calcule le nombre d'actions total (arrivée et départ) des blocs en entrées pour obtenir l'index maximal du curseur. Etant donné que chaque bloc avec succès de placement a deux actions, une arrivée et un départ, 
#et que les blocs avec échecs de placement ont une seule action, une arrivée, on retrouve cette valeur aisément.
index_curseur = len(colis_placer)*2 + len(colis_pas_placer)

#On crée un label qui affichera le nombre d'actions restantes à accomplir au fur et à mesure qu'on change la valeur de l'index ou que la simulation se déroule
label_compteur = tk.Label(cadre_droite, text=f"Nombre d'actions à accomplir : {index_curseur}", fg = "black", bg = "white", font=("Helvetica", 10, "bold"), borderwidth=2, relief="raised")
label_compteur.pack(pady=10)

#On crée le curseur dont les valeurs iront de 0 à l'index_curseur
curseur_avancement = tk.Scale(cadre_droite, from_=0, to=index_curseur, orient="horizontal", label="                              Curseur", borderwidth=2, relief="raised", 
                              fg="black", bg="white", activebackground="black", font=("Helvetica", 10, "bold"), length=index_curseur+75)
curseur_avancement.set(0)
curseur_avancement.pack()

#####################################################################################
#FONCTION: ajuster_avancement
#OBJECTIF : Afficher les n premières actions de la simulation en changeant l'index du curseur à n
#ENTRÉES : *args - rend compte de l'état du curseur
#NOTES  : /
#SORTIES : /
#####################################################################################
def ajuster_avancement(*args):
    global liste_y, x1, x2, y1

    #On récupère l'index du curseur
    index = curseur_avancement.get()

    #On supprime l'ensemble des éléments de la fenêtre pour la reconstruire
    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    supprimer_blocs(zone_echecs)    
    dico_blocs.clear()
    x1, x2, y1 = 0, 0, 0 
    liste_y = [0] 

    #A l'index n, on effectue les n premières actions en ordre chronologique
    for i in range(len(taches_triees)):
        if i < index:
            tache = taches_triees[i]
            if tache[1] == "arrivee":
                placer_bloc(tache[0])
            else:
                effacer_bloc(tache[0])

    #On met à jour notre compteur nos compteurs de temps et d'actions     
    nb_etapes = index_curseur - index
    label_compteur.config(text=f"Nombre d'actions à accomplir : {nb_etapes}")
    date = taches_triees[index-1]
    temps_action = date[0][5] if date[1] == "arrivee" else date[0][6] 
    label_temps.config(text=f"Date : {temps_action.strftime('%d-%m-%Y')}")
    if index == 0:
        label_temps.config(text=f"Date :")

#On initialise une liste vide qui servira à la fonction du bouton launch
taches_launch = []

#####################################################################################
#FONCTION: lancer_placement_blocs
#OBJECTIF : Lancer la simulation du placement de blocs
#ENTRÉES : /
#NOTES  : /
#SORTIES : /
#####################################################################################
def lancer_placement_blocs():
    global current_task_id, dico_blocs, taches_launch, liste_y, x1, x2, y1, temps_actuel

    #On vérifie d'abord que la simulation n'est pas déjà lancée
    if current_task_id is None:

        #On récupère l'index courant du curseur
        index = curseur_avancement.get()

        #On supprime l'ensemble des éléments de la fenêtre pour la reconstruire
        supprimer_blocs(cadre_A)
        supprimer_blocs(cadre_B)
        supprimer_blocs(cadre_C)
        supprimer_blocs(zone_echecs)
        temps_actuel = 0  
        x1, x2, y1 = 0, 0, 0  
        liste_y = [0]    
        dico_blocs = {}
        taches_launch.clear()

        #On veut faire en sorte que si le curseur est à l'index n, seuls les n premières actions sont réalisées par la simulation. De fait, on complète taches_launch jusqu'à l'indice "index"
        #avec les tâches triées chronologiquement puis on lance executer_taches() avec cette liste
        for i in range(index):
            taches_launch.append(taches_triees[i])
        label_compteur.config(text=f"Nombre d'étapes à accomplir : {len(taches_triees) - index}")
        executer_taches()

#Variable dont le rôle est de renseigner sur l'état (pause ou play) de la simulation
en_pause = False

#####################################################################################
#FONCTION: mettre_en_pause
#OBJECTIF : Mettre en pause la simulation du placement de blocs et enlever la pause si la pause est active
#ENTRÉES : /
#NOTES  : /
#SORTIES : /
#####################################################################################
def mettre_en_pause():
    global current_task_id, en_pause

    #Si on fait appel à cette fonction et que la simulation est en pause, c'est qu'on veut annuler la pause et faire que la simulation reprenne. Alors avec executer_taches(), on continue là où on s'était arrêté
    #car taches_launch contient encore les actions restantes
    if en_pause:
        en_pause = False
        executer_taches()
    
    #A l'inverse, si la simulation est active et qu'on fait appel à cette fonction, c'est qu'on veut mettre en pause cette simulation. On vérifie d'abord qu'une tache est en cours, puis on l'annule et 
    #on met current_task_id à None pour interrompre executer_taches
    else:
        if current_task_id:
            fenetre.after_cancel(current_task_id)
            current_task_id = None
        en_pause = True

#####################################################################################
#FONCTION: reset_solution
#OBJECTIF : Effacer toute la fenêtre et initialiser le redémarrage d'une simulation
#ENTRÉES : /
#NOTES  : /
#SORTIES : /
#####################################################################################
def reset_solution():
    global current_task_id, dico_blocs, en_pause, taches_launch, liste_y, x1, x2, y1

    #On récupère l'index courant du curseur
    index = curseur_avancement.get()
    
    #On remet la variable de pause à sa valeur initiale (False), on annule la tâche en cours et on interrompt executer_taches() en mettant current_task_id à None
    en_pause = False
    if current_task_id:
        fenetre.after_cancel(current_task_id)
        current_task_id = None

    #On supprime l'ensemble des éléments de la fenêtre pour la reconstruire
    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    supprimer_blocs(zone_echecs)    
    dico_blocs.clear()
    x1, x2, y1 = 0, 0, 0
    liste_y = [0]     
    taches_launch.clear()

    #On initialise le futur redémarrage de la simulation en stockant, à l'index n du curseur, toutes les n premières actions dans taches_launch
    for tache in taches_triees[:index]:
        taches_launch.append(tache)
        if tache[1] == "arrivee":
            placer_bloc(tache[0])
        else:
            effacer_bloc(tache[0])        
    label_compteur.config(text=f"Nombre d'étapes à accomplir : {index_curseur - index}")

#####################################################################################
#FONCTION: on_select_solution
#OBJECTIF : Pouvoir basculer d'une solution d'optimisation à une autre à l'aide du menu déroulant créé
#ENTRÉES : /
#NOTES  : Cette fonction sera le principal objet de la prochaine mise à jour de l'interface. En effet, actuellement, c'est la même solution derrière "Solution_1", "Solution_2" et "Solution_3".
#         Il faudra donc pouvoir récupérer plusieurs fois des entrées et les affecter à chacunes des solutions du menu déroulant.
#SORTIES : /
#####################################################################################
def on_select_solution(event):
    global current_task_id, dico_blocs, taches_launch, liste_y, x1, x2, y1

    #Si la simulation est lancée, on annule la tâche en cours et on interrompt executer_taches() en mettant current_task_id à None
    if current_task_id:
        fenetre.after_cancel(current_task_id)
        current_task_id = None
    
    #On supprime l'ensemble des éléments de la fenêtre pour la reconstruire
    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    supprimer_blocs(zone_echecs)    
    dico_blocs.clear()
    x1, x2, y1 = 0, 0, 0 
    liste_y = [0]   
    taches_launch.clear()

    #On récupère l'index courant du curseur
    index = curseur_avancement.get()

    #En changeant de solution, on veut que la fenêtre affiche en image fixe les actions déjà faites à l'index courant du curseur et que soit initialisé le lancement d'une solution
    for i in range(index):
        tache = taches_triees[i]

        #De fait, on remplit taches_launch avec les actions faites jusqu'à l'index courant
        taches_launch.append(tache)

        #Et on complète la fenêtre avec ces actions
        if tache[1] == "arrivee":
            placer_bloc(tache[0])
        else:
            effacer_bloc(tache[0])
    label_compteur.config(text=f"Nombre d'étapes à accomplir : {index_curseur-index}") 

#####################################################################################
#FONCTION: supprimer_blocs
#OBJECTIF : Supprimer tous les blocs d'un cadre
#ENTRÉES : canvas - cadre pour lequel on veut supprimer tous les blocs s'y trouvant
#NOTES  : /
#SORTIES : /
#####################################################################################
def supprimer_blocs(canvas):
    #On parcourt chaque bloc du cadre en question et on les supprime à la suite
    for item in canvas.find_all():
        canvas.delete(item)

#Création du bouton "Courbes d'analyse"
bouton_courbes_analyse = tk.Button(cadre_droite, text="Courbes d'analyse", bg="yellow", fg="black", relief="raised", command=afficher_courbes_analyse)
bouton_courbes_analyse.pack(padx=10, pady=10)

#Création du bouton Launch
bouton_launch = tk.Button(cadre_droite, text="Launch", bg="blue", fg="white", relief="raised", command=lancer_placement_blocs)
bouton_launch.pack(padx=10, pady=10)

#Création du bouton Pause/Play
bouton_pause_play = tk.Button(cadre_droite, text="Pause/Play", bg="green", fg="white", relief="raised", command=mettre_en_pause)
bouton_pause_play.pack(padx=10, pady=10)

#Création du bouton Reset
bouton_reset = tk.Button(cadre_droite, text="Reset", bg="red", fg="white", relief="raised", command=reset_solution)
bouton_reset.pack(padx=10, pady=10)

#Associe les fonctions d'événements aux éléments associés
cadre_A.bind("<B1-Motion>", drag_A)
cadre_B.bind("<B1-Motion>", drag_B)
cadre_C.bind("<B1-Motion>", drag_C)
curseur_avancement.bind("<ButtonRelease-1>", ajuster_avancement)
menu_deroulant.bind("<<ComboboxSelected>>", on_select_solution)

#On affiche la fenêtre
fenetre.mainloop()

