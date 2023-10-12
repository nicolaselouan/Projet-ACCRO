import tkinter as tk
def clic(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET, bloc_courant_id

    # position du pointeur de la souris
    x = event.x
    y = event.y
    #print("Position du clic -> ", x, y)

    for bloc_id, texte_id in dico_blocs.items():
        coords = cadre_blocs_a_placer.coords(bloc_id)
        #print("Les coordonnées sont ->", coords)
        x_min, y_min, x_max, y_max = coords

        if x_min <= x <= x_max and y_min <= y <= y_max:
            DETECTION_CLIC_SUR_OBJET = True
            bloc_courant_id = bloc_id
            print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET)
        else:
            DETECTION_CLIC_SUR_OBJET = False
 
def drag(event):
    # Position du pointeur de la souris
    x = event.x + (LargeurBloc / 2)
    y = event.y + (HauteurBloc / 2)

    cadre_width = cadre_blocs_a_placer.winfo_width()
    cadre_height = cadre_blocs_a_placer.winfo_height()

    for bloc_id in dico_blocs.values():
            # limite de l'objet dans la zone graphique
            if x < LargeurBloc:
                x = LargeurBloc
            if x > cadre_width - LargeurBloc:
                x = cadre_width
            if y < HauteurBloc:
                y = HauteurBloc
            if y > cadre_height - HauteurBloc:
                y = cadre_height  
            # mise à jour de la position du bloc
            cadre_blocs_a_placer.coords(bloc_courant_id, [x - LargeurBloc, y - HauteurBloc, x, y])

            # mise à jour de la position du texte
            x_texte = (x - LargeurBloc + x) / 2
            y_texte = (y - HauteurBloc + y) / 2
            cadre_blocs_a_placer.coords(dico_blocs[bloc_courant_id], x_texte, y_texte)


def init_positions_blocs():
    for bloc_id in dico_blocs.values():
        # Récupérez les coordonnées initiales de chaque bloc et stockez-les dans le dictionnaire
        positions_blocs[bloc_id] = cadre_blocs_a_placer.coords(bloc_id)

#Variables globales
DETECTION_CLIC_SUR_OBJET = False
bloc_courant_id = None

# Dictionnaire pour stocker les positions des blocs
positions_blocs = {}

#Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Interface avec des blocs")

Largeur = 1300
Hauteur = 800
LargeurBloc = 50
HauteurBloc = 25

# Cadre principal pour aligner les zones horizontalement
cadre_principal = tk.Canvas(fenetre, width=Largeur, height=Hauteur)
cadre_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
cadre_principal.focus_set()

# Cadre pour "Déchargement" et "Bloc à placer"
cadre_droite = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_droite.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=False)

# Libellé pour "Déchargement" à l'extérieur
label_dechargement = tk.Label(cadre_droite, text="Déchargement", bg="white", font=("Helvetica", 10, "bold"))
label_dechargement.pack()

# Zone de texte pour "Déchargement"
zone_dechargement = tk.Canvas(cadre_droite, bg='white', relief="solid", bd=2)
zone_dechargement.pack(fill=tk.BOTH, expand=True)

# Libellé pour "Bloc à placer" à l'extérieur
label_blocs_a_placer = tk.Label(cadre_droite, text="Bloc à placer", bg="white", font=("Helvetica", 10, "bold"))
label_blocs_a_placer.pack()

# Cadre pour les blocs à placer (dans la zone "Bloc à placer") avec fond blanc
cadre_blocs_a_placer = tk.Canvas(cadre_droite, bg='white', relief="solid", bd=2)
cadre_blocs_a_placer.pack(fill=tk.BOTH, expand=True)

# On dessine la fenêtre avant pour récupérer les coordonnées du cadre "Bloc à placer"
fenetre.update()

# Nombre de blocs par ligne dans le cadre bloc_a_placer
blocs_par_ligne = 7

# Un dictionnaire pour stocker les paires d'IDs de rectangle (clé) et de texte (valeur)
dico_blocs = {}  

# Ajouter des petits blocs maniables dans la zone "Bloc à placer"
for i in range(1, 10):
    x1 = (i - 1) % blocs_par_ligne * LargeurBloc
    y1 = (i - 1) // blocs_par_ligne * HauteurBloc
    x2 = x1 + LargeurBloc
    y2 = y1 + HauteurBloc
    
    # Dessiner un rectangle avec les caractéristiques souhaitées
    bloc_rectangle = cadre_blocs_a_placer.create_rectangle(x1, y1, x2, y2, fill="lightgrey", outline="black", width=2)

    # Ajouter du texte au milieu du rectangle
    texte = f"Bloc {i}"
    x_texte = (x1 + x2) / 2
    y_texte = (y1 + y2) / 2
    texte_id = cadre_blocs_a_placer.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 10, "bold"))
    
    # Stocker l'ID du texte dans le dictionnaire (valeur) avec l'ID du rectangle correspondant (clé)
    dico_blocs[bloc_rectangle] = texte_id

# Initialise les positions des blocs au démarrage
init_positions_blocs()
print("Coordonnées blocs ->", positions_blocs)

# Cadre pour "A", "B" et "C" superposées verticalement à gauche
cadre_zones = tk.Canvas(cadre_principal, bg='lightgrey', relief="solid", bd=2)
cadre_zones.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Libellé pour "A" au-dessus
label_a = tk.Label(cadre_zones, text="A", bg="white", font=("Helvetica", 14, "bold"))
label_a.pack()

# Cadre pour "A"
cadre_a = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_a.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "B" au-dessus
label_b = tk.Label(cadre_zones, text="B", bg="white", font=("Helvetica", 14, "bold"))
label_b.pack()

# Cadre pour "B"
cadre_b = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_b.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "C" au-dessus
label_c = tk.Label(cadre_zones, text="C", bg="white", font=("Helvetica", 14, "bold"))
label_c.pack()

# Cadre pour "C"
cadre_c = tk.Canvas(cadre_zones, bg="white", borderwidth=2, relief="solid")
cadre_c.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# La méthode bind() permet de lier un événement avec une fonction
cadre_blocs_a_placer.bind('<Button-1>', clic)  # événement clic gauche (press)
cadre_blocs_a_placer.bind('<B1-Motion>', drag)  # événement bouton gauche enfoncé (hold down)

fenetre.mainloop()







