import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#Entrées de la fenêtre pour tester l'algorithme
colis_placer = [["Bloc 1", 50, 25, "A", (10,20)], ["Bloc 2", 60, 50, "B", (10,20)], 
["Bloc 3", 45, 35, "B", (100,20)], ["Bloc 4", 15, 10, "A", (50,50)], ["Bloc 5", 25, 20, "A", (90,15)],
["Bloc 11", 40, 30, "C", (50,20)], ["Bloc 12", 30, 20, "A", (150,50)], ["Bloc 13", 25, 20, "A", (300,120)],
["Bloc 14", 60, 30, "A", (200,160)], ["Bloc 15", 50, 40, "B", (200,100)], ["Bloc 16", 75, 35, "A", (80,80)]]

colis_pas_placer = [["Bloc 6", 90, 45, 0, (0,0)], ["Bloc 7", 150, 150, 0, (0,0)],
["Bloc 8", 120, 120, 0, (0,0)], ["Bloc 9", 65, 100, 0, (0,0)], ["Bloc 10", 80, 75, 0, (0,0)]]

dico_graphs_1 = {15 : [0.3,2], 25 : [0.8, 4], 100 : [1.7, 17], 85 : [1.5, 14], 50 : [1, 6], 5 : [0.2, 0], 35 : [0.6, 7], 65 : [1.1, 12], 110 : [1.9, 23], 70 : [1.1, 16], 40 : [0.6, 5]}
dico_graphs_2 = {15 : [0.2,4], 25 : [0.7, 7], 100 : [1.3, 24], 85 : [1.2, 17], 50 : [0.8, 8], 5 : [0.05, 2], 35 : [0.3, 9], 65 : [0.8, 18], 110 : [1.4, 30], 70 : [0.9, 20], 40 : [0.2, 6]}
dico_graphs_3 = {15 : [0.4,0], 25 : [1.0, 3], 100 : [1.6, 14], 85 : [1.6, 10], 50 : [1.3, 4], 5 : [0.5, 0], 35 : [0.9, 4], 65 : [1.5, 8], 110 : [3.0, 12], 70 : [1.7, 9], 40 : [0.9, 4]}

#Graphiques 

# Trier les dictionnaires selon la clé 'nombre_de_blocs'
dico_graphs_1 = dict(sorted(dico_graphs_1.items()))
dico_graphs_2 = dict(sorted(dico_graphs_2.items()))
dico_graphs_3 = dict(sorted(dico_graphs_3.items()))


nombre_de_blocs_1 = list(dico_graphs_1.keys())
nombre_de_blocs_2 = list(dico_graphs_2.keys())
nombre_de_blocs_3 = list(dico_graphs_3.keys())

temps_execution_1 = [value[0] for value in dico_graphs_1.values()]
temps_execution_2 = [value[0] for value in dico_graphs_2.values()]
temps_execution_3 = [value[0] for value in dico_graphs_3.values()]

nombre_echecs_1 = [value[1] for value in dico_graphs_1.values()]
nombre_echecs_2 = [value[1] for value in dico_graphs_2.values()]
nombre_echecs_3 = [value[1] for value in dico_graphs_3.values()]

# Variables globales pour la zone A
DETECTION_CLIC_SUR_OBJET_A = False

# Gestionnaire d'événements pour la zone A
def drag_A(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET_A

    # position du pointeur de la souris
    x = event.x
    y = event.y
    print("Position du clic -> ", x, y)

    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_A : 
            coords = values[2].coords(values[0])
            #print("Les coordonnées sont ->", coords)
            x_min, y_min, x_max, y_max = coords

            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_A = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_A)
            else:
                DETECTION_CLIC_SUR_OBJET_A = False
            
            if DETECTION_CLIC_SUR_OBJET_A:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]
                print("Largeur bloc = ", LargeurBloc)
                print("Hauteur bloc = ", HauteurBloc)

                print("x =", x)
                # Position du pointeur de la souris
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                print("x =", x)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()
                
                print("Largeur cadre = ", cadre_width)
                print("Hauteur cadre = ", cadre_height)
                # Limitez le bloc à l'intérieur de la zone graphique
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                # Mettez à jour la position du bloc
                cadre_A.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                # Mettez à jour la position du texte
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_A.coords(values[1], x_texte, y_texte)    


# Variables globales pour la zone B
DETECTION_CLIC_SUR_OBJET_B = False

# Gestionnaire d'événements pour la zone B
def drag_B(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET_B

    # position du pointeur de la souris
    x = event.x
    y = event.y
    #print("Position du clic -> ", x, y)

    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_B : 
            coords = values[2].coords(values[0])
            #print("Les coordonnées sont ->", coords)
            x_min, y_min, x_max, y_max = coords

            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_B = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_B)
            else:
                DETECTION_CLIC_SUR_OBJET_B = False
            
            if DETECTION_CLIC_SUR_OBJET_B:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]

                # Position du pointeur de la souris
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()
                
                # Limitez le bloc à l'intérieur de la zone graphique
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                # Mettez à jour la position du bloc
                cadre_B.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                # Mettez à jour la position du texte
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_B.coords(values[1], x_texte, y_texte)   

# Variables globales pour la zone C
DETECTION_CLIC_SUR_OBJET_C = False

# Gestionnaire d'événements pour la zone C
def drag_C(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET_C

    # position du pointeur de la souris
    x = event.x
    y = event.y
    #print("Position du clic -> ", x, y)

    for bloc_counter, values in dico_blocs.items():
        if values[2] == cadre_C : 
            coords = values[2].coords(values[0])
            #print("Les coordonnées sont ->", coords)
            x_min, y_min, x_max, y_max = coords

            if x_min <= x <= x_max and y_min <= y <= y_max:
                DETECTION_CLIC_SUR_OBJET_C = True
                print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET_C)
            else:
                DETECTION_CLIC_SUR_OBJET_C = False
            
            if DETECTION_CLIC_SUR_OBJET_C:
                LargeurBloc = coords[2]-coords[0]
                HauteurBloc = coords[3]-coords[1]

                # Position du pointeur de la souris
                x = event.x + (LargeurBloc / 2)
                y = event.y + (HauteurBloc / 2)

                cadre_width = values[2].winfo_width()
                cadre_height = values[2].winfo_height()
                
                # Limitez le bloc à l'intérieur de la zone graphique
                if x < LargeurBloc:
                    x = LargeurBloc
                if x > cadre_width:
                    x = cadre_width 
                if y < HauteurBloc:
                    y = HauteurBloc
                if y > cadre_height:
                    y = cadre_height

                # Mettez à jour la position du bloc
                cadre_C.coords(values[0], [x - LargeurBloc, y - HauteurBloc, x, y])

                # Mettez à jour la position du texte
                x_texte = (x - LargeurBloc + x) / 2
                y_texte = (y - HauteurBloc + y) / 2
                cadre_C.coords(values[1], x_texte, y_texte)   
        
#Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Interface")

Largeur = 1200
Hauteur = 1000

# Ajustement de la taille de la fenêtre
fenetre.geometry(f"{Largeur}x{Hauteur}")

# Cadre principal
cadre_principal = tk.Canvas(fenetre, width=Largeur, height=Hauteur)
cadre_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
cadre_principal.focus_set()

# Cadre à droite pour "Échecs de placement"
cadre_droite = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_droite.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=False)

# Libellé pour "Échecs de placement"
label_dechargement = tk.Label(cadre_droite, text="Échecs de placement", bg="white", font=("Helvetica", 10, "bold"))
label_dechargement.pack()

# Canvas pour "Échecs de placement"
zone_echecs = tk.Canvas(cadre_droite, bg='white', relief="solid", bd=2)
zone_echecs.pack(fill=tk.BOTH, expand=True)

# Création du menu déroulant avec le texte et les options spécifiées
options = ["Solution_1", "Solution_2", "Solution_3"]
var = tk.StringVar(cadre_droite)
var.set(options[0])  # Valeur par défaut

# Configuration du menu déroulant avec la bibliothèque ttk
menu_deroulant = ttk.Combobox(cadre_droite, textvariable=var, values=options, state="readonly", font=("Helvetica", 10, "bold"))
menu_deroulant.pack(pady=10)

# Ajout du compteur
nombre_blocs_restants = len(colis_placer)  # nombre initial de blocs
label_compteur = tk.Label(cadre_droite, text=f"Nombre de blocs restants à placer : {nombre_blocs_restants}", fg = "black", bg = "white", font=("Helvetica", 10, "bold"), borderwidth=2, relief="raised")
label_compteur.pack(pady=10)

# On dessine la fenêtre avant
fenetre.update()

# Cadre pour "A", "B" et "C" superposées verticalement à gauche
cadre_zones = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_zones.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Libellé pour "A" au-dessus
label_a = tk.Label(cadre_zones, text="A", bg="white", font=("Helvetica", 14, "bold"))
label_a.pack()

# Cadre pour "A"
cadre_A = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_A.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "B" au-dessus
label_b = tk.Label(cadre_zones, text="B", bg="white", font=("Helvetica", 14, "bold"))
label_b.pack()

# Cadre pour "B"
cadre_B = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_B.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "C" au-dessus
label_c = tk.Label(cadre_zones, text="C", bg="white", font=("Helvetica", 14, "bold"))
label_c.pack()

# Cadre pour "C"
cadre_C = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_C.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

liste_y = []
x1, x2, y1, y2 = 0, 0, 0, 0

# Ajouter les blocs non placés dans la zone Échecs de placement
for i in range(len(colis_pas_placer)):
    
    x2 = colis_pas_placer[i][1] + x2
    y2 = y1 + colis_pas_placer[i][2]

    if x2 > cadre_droite.winfo_width() :
        x1, x2, y1, y2 = 0, colis_pas_placer[i][1], max(liste_y), max(liste_y) + colis_pas_placer[i][2] 
        liste_y = []

    # Dessiner un rectangle avec les caractéristiques souhaitées
    bloc_rectangle = zone_echecs.create_rectangle(x1, y1, x2, y2, fill="lightgrey", outline="black", width=2)

    # Ajouter du texte au milieu du rectangle
    texte = "{}".format(colis_pas_placer[i][0])
    x_texte = (x1 + x2) / 2
    y_texte = (y1 + y2) / 2
    texte_id = zone_echecs.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 8, "bold"))
    
    liste_y.append(y2)
    x1 = x2

# Un dictionnaire pour stocker les paires d'IDs de rectangle (clé) et de texte (valeur)
dico_blocs = {}  

# Liste des tâches à effectuer
taches = []

# Variable globale pour compter les identifiants des blocs
bloc_counter = 0

# Fonction pour placer un bloc
def placer_bloc(bloc):
    global bloc_counter 

    if bloc[3] == "A":
        canvas = cadre_A
    elif bloc[3] == "B":
        canvas = cadre_B
    elif bloc[3] == "C":
        canvas = cadre_C

    x1, y1 = bloc[4]
    x2 = x1 + bloc[1]
    y2 = y1 + bloc[2]
    
    # Dessiner un rectangle avec les caractéristiques souhaitées
    bloc_rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="lightgrey", outline="black", width=2)

    # Ajouter du texte au milieu du rectangle
    texte = "{}".format(bloc[0])
    x_texte = (x1 + x2) / 2
    y_texte = (y1 + y2) / 2
    texte_id = canvas.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 8, "bold"))
    
     # Stocker l'ID du texte dans le dictionnaire (valeur) avec l'ID du rectangle correspondant (clé)
    dico_blocs[bloc_counter] = (bloc_rectangle, texte_id, canvas)
    print(dico_blocs)

    # Incrémenter le compteur d'identifiant de bloc
    bloc_counter += 1

# Fonction pour afficher les courbes d'analyse
def afficher_courbes_analyse():
    # Créer les graphiques
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Tracer les courbes pour les temps d'exécution
    ax1.plot(nombre_de_blocs_1, temps_execution_1, label='Temps d\'exécution solution_1', marker='o', linestyle='-.', color='b')
    ax1.plot(nombre_de_blocs_2, temps_execution_2, label='Temps d\'exécution solution_2', marker='o', linestyle='-.', color='g')
    ax1.plot(nombre_de_blocs_3, temps_execution_3, label='Temps d\'exécution solution_3', marker='o', linestyle='-.', color='r')

    # Configurer les détails du graphique 1
    ax1.set_xlabel('Nombre de blocs')
    ax1.set_ylabel('Temps d\'exécution (s)')
    ax1.set_title('Comparaison des solutions - Temps d\'exécution')
    ax1.legend()
    ax1.grid(True)

    # Tracer les courbes pour le nombre d'échecs
    ax2.plot(nombre_de_blocs_1, nombre_echecs_1, label='Nombre d\'échecs solution_1', marker='o', linestyle='--', color='b')
    ax2.plot(nombre_de_blocs_2, nombre_echecs_2, label='Nombre d\'échecs solution_2', marker='o', linestyle='--', color='g')
    ax2.plot(nombre_de_blocs_3, nombre_echecs_3, label='Nombre d\'échecs solution_3', marker='o', linestyle='--', color='r')

    # Configurer les détails du graphique 2
    ax2.set_xlabel('Nombre de blocs')
    ax2.set_ylabel('Nombre d\'échecs')
    ax2.set_title('Comparaison des solutions - Nombre d\'échecs')
    ax2.legend()
    ax2.grid(True)

    # Créer une nouvelle fenêtre Tkinter pour afficher les graphiques
    new_window = tk.Toplevel(fenetre)
    new_window.title('Courbes d\'analyse')

    # Incorporer les graphiques dans la fenêtre Tkinter
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Créer la liste des tâches à effectuer
for bloc in colis_placer:
    taches.append(bloc)

curseur_avancement = tk.Scale(cadre_droite, from_= 0, to=len(colis_placer), orient="horizontal", label="     Curseur", borderwidth=2, relief="raised", fg = "black", bg = "white", activebackground = "black", font=("Helvetica", 10, "bold"))
curseur_avancement.set(0)  # Initialiser avec la valeur maximale
curseur_avancement.pack()

# Fonction de mise à jour de l'affichage en fonction de la position du curseur
def ajuster_avancement(*args):
    index = curseur_avancement.get()
    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    dico_blocs.clear()
    for i in range(index):
        placer_bloc(colis_placer[i])
    label_compteur.config(text=f"Nombre de blocs restants à placer : {len(colis_placer)-index}")    
# Lier le curseur à la fonction de mise à jour
curseur_avancement.bind("<ButtonRelease-1>", ajuster_avancement)

# Définir une variable pour stocker l'ID de la tâche en cours
current_task_id = None

# Dans votre gestionnaire d'événements pour le menu déroulant
def on_select_solution(event):
    global current_task_id, dico_blocs
    if current_task_id:
        fenetre.after_cancel(current_task_id)
        current_task_id = None
    
    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    dico_blocs = {}  

    # Annuler les tâches en cours
    taches.clear()
    index = curseur_avancement.get()
    for i in range(index):
        placer_bloc(colis_placer[i])
    label_compteur.config(text=f"Nombre de blocs restants à placer : {len(colis_placer)-index}")     

# Fonction pour exécuter les tâches
def executer_taches():
    global current_task_id
    if taches:
        bloc = taches.pop(0)
        placer_bloc(bloc)
        label_compteur.config(text=f"Nombre de blocs restants à placer : {len(taches)}")
        current_task_id = fenetre.after(1500, executer_taches)
    else:
        current_task_id = None

def supprimer_blocs(canvas):
    for item in canvas.find_all():
        canvas.delete(item)

# Fonction bouton reset
def reset_solution():
    global current_task_id, dico_blocs, en_pause
    index = curseur_avancement.get()
    en_pause = False
    if current_task_id:
        fenetre.after_cancel(current_task_id)
        current_task_id = None

    supprimer_blocs(cadre_A)
    supprimer_blocs(cadre_B)
    supprimer_blocs(cadre_C)
    dico_blocs = {}

    for bloc in colis_placer:
        taches.append(bloc)
    label_compteur.config(text=f"Nombre de blocs restants à placer : {index}")

en_pause = False

# Fonction bouton PLay/Pause
def mettre_en_pause():
    global current_task_id, en_pause
    if en_pause:
        en_pause = False
        executer_taches()
    else:
        if current_task_id:
            fenetre.after_cancel(current_task_id)
            current_task_id = None
        en_pause = True

def lancer_placement_blocs():
    global current_task_id
    if current_task_id is None:
        index = curseur_avancement.get()
        supprimer_blocs(cadre_A)
        supprimer_blocs(cadre_B)
        supprimer_blocs(cadre_C)
        dico_blocs = {}
        taches.clear()
        for i in range(index):
            taches.append(colis_placer[i])
        label_compteur.config(text=f"Nombre de blocs restants à placer : {len(colis_placer)-index}")
        executer_taches()

# Créer le bouton "Courbes d'analyse"
bouton_courbes_analyse = tk.Button(cadre_droite, text="Courbes d'analyse", bg="yellow", fg="black", relief="raised", command=afficher_courbes_analyse)
bouton_courbes_analyse.pack(side="top", padx=10, pady=10)

# Création du bouton Reset
bouton_reset = tk.Button(cadre_droite, text="Reset", bg="red", fg="white", relief="raised", command=reset_solution)
bouton_reset.pack(side="bottom", padx=10, pady=10)

# Création du bouton Launch
bouton_launch = tk.Button(cadre_droite, text="Launch", bg="blue", fg="white", relief="raised", command=lancer_placement_blocs)
bouton_launch.pack(padx=10, pady=10)

# Création du bouton Pause/Play
bouton_pause_play = tk.Button(cadre_droite, text="Pause/Play", bg="green", fg="white", relief="raised", command=mettre_en_pause)
bouton_pause_play.pack(padx=10, pady=10)

menu_deroulant.bind("<<ComboboxSelected>>", on_select_solution)

# Associer les fonctions d'événements à vos cadres respectifs
cadre_A.bind("<B1-Motion>", drag_A)
cadre_B.bind("<B1-Motion>", drag_B)
cadre_C.bind("<B1-Motion>", drag_C)

fenetre.mainloop()
