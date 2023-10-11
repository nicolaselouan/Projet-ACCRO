import tkinter as tk   

fenetre = tk.Tk()
fenetre.title("Interface des zones avec des blocs")

# Ajuster la taille initiale de la fenêtre
fenetre.geometry("1300x1000")  # Largeur x Hauteur

Largeur = 1300
Hauteur = 800
LargeurBloc = 50
HauteurBloc = 25

# Cadre principal pour aligner les zones horizontalement
cadre_principal = tk.Frame(fenetre)
cadre_principal.pack(fill=tk.BOTH, expand=True)

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

# Nombre de blocs par ligne
blocs_par_ligne = 5

# Ajouter des petits blocs maniables dans la zone "Bloc à placer"
for i in range(1, 25):
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
    cadre_blocs_a_placer.create_text(x_texte, y_texte, text=texte, font=("Helvetica", 10, "bold"))
    
    #Obtenir coordonées
    x_cadre, y_cadre = cadre_blocs_a_placer.winfo_rootx(), cadre_blocs_a_placer.winfo_rooty()
    print("Position cadre par rapport à fenêtre ->", x_cadre, y_cadre)
    coords = cadre_blocs_a_placer.coords(bloc_rectangle)
    x_min, y_min, x_max, y_max = coords

    x_min_fenetre = x_cadre + x_min
    y_min_fenetre = y_cadre + y_min
    x_max_fenetre = x_cadre + x_max
    y_max_fenetre = y_cadre + y_max

    print("Position objet par rapport à la fenêtre ->", x_min_fenetre, y_min_fenetre, x_max_fenetre, y_max_fenetre)

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

fenetre.mainloop()





