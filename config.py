import tkinter as tk

def charger_bloc(event, zone):
    bloc = canvas.itemcget(event.widget, "text")
    canvas.itemconfig(event.widget, fill="white", text="")
    canvas.itemconfig(zone, text=bloc, fill="blue")

fenetre = tk.Tk()
fenetre.title("Interface avec des blocs")

# Ajuster la taille initiale de la fenêtre
fenetre.geometry("800x400")  # Largeur x Hauteur

# Cadre principal pour aligner les zones horizontalement
cadre_principal = tk.Frame(fenetre)
cadre_principal.pack(fill=tk.BOTH, expand=True)

# Cadre pour "Déchargement" et "Bloc à placer"
cadre_droite = tk.Frame(cadre_principal)
cadre_droite.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=False)

# Libellé pour "Déchargement" à l'extérieur
label_dechargement = tk.Label(cadre_droite, text="Déchargement")
label_dechargement.pack()

# Zone de texte pour "Déchargement"
zone_dechargement = tk.Label(cadre_droite, text="", bg="white", relief="solid")
zone_dechargement.pack(fill=tk.BOTH, expand=True)

# Libellé pour "Bloc à placer" à l'extérieur
label_blocs_a_placer = tk.Label(cadre_droite, text="Bloc à placer")
label_blocs_a_placer.pack()

# Cadre pour les blocs à placer (dans la zone "Bloc à placer") avec fond blanc
cadre_blocs_a_placer = tk.Frame(cadre_droite, bg="white", borderwidth=2, relief="solid")
cadre_blocs_a_placer.pack(fill=tk.BOTH, expand=True)

# Ajouter des petits blocs maniables dans la zone "Bloc à placer"
for i in range(1, 6):
    bloc_label = tk.Label(cadre_blocs_a_placer, text=f"Bloc {i}", padx=5, pady=5, borderwidth=2, relief="solid")
    bloc_label.pack(side=tk.LEFT, padx=5, pady=5)

# Cadre pour "A", "B" et "C" superposées verticalement à gauche
cadre_zones = tk.Frame(cadre_principal)
cadre_zones.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Libellé pour "A" au-dessus
label_a = tk.Label(cadre_zones, text="A")
label_a.pack()

# Cadre pour "A"
cadre_a = tk.Frame(cadre_zones, borderwidth=2, relief="solid")
cadre_a.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "B" au-dessus
label_b = tk.Label(cadre_zones, text="B")
label_b.pack()

# Cadre pour "B"
cadre_b = tk.Frame(cadre_zones, borderwidth=2, relief="solid")
cadre_b.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

# Libellé pour "C" au-dessus
label_c = tk.Label(cadre_zones, text="C")
label_c.pack()

# Cadre pour "C"
cadre_c = tk.Frame(cadre_zones, borderwidth=2, relief="solid")
cadre_c.pack(fill=tk.BOTH, expand=True, padx=(0, 10), pady=(0, 10))

fenetre.mainloop()
