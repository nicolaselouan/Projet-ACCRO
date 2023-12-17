Projet ACCRO
==========================================================
Ce programme a été conçu par Maxime Chanssat, Florian Desplanques, Elouan Nicolas, Hamidou Kane et Lucie Berger dans le cadre d'un projet de l'UE Projet Commande Entreprise de IMT Atlantique.
Décembre 2023

INSTALLATION PREALABLE
==========================================================
Sur le Git Projet-ACCRO, vous devez récupérer l'ensemble des fichiers les dossiers Simulation et Data avec l'ensemble des fichiers .py qu'ils contiennent et les enregistrer dans un même dossier sur votre ordinateur.
Vous récupérerez également le fichier interface.py et le placerez dans le même dossier.

LANCEMENT ET COMPARAISON DES DIFFERENTES STRATEGIES
==========================================================
Pour lancer le programme, il suffit d'exécuter le fichier main.py contenu dans le dossier Simulation.
Pour différents noms de stratégies "strategy_name", les variables Simu.contexts[strategy_name].modified_data  contiennent les résultats de la simulation lors de l'application de cette stratégie.
Ces objets contiennent notament un attribu blocs cotenant l'ensembles des blocs du problème dont la zone et la position (x,y) du bloc i sont repectivement définies par:
		-Simu.contexts[strategy_name].modified_data.blocs[i].position.zone
		-(Simu.contexts[strategy_name].modified_data.blocs[i].position.x, Simu.contexts[strategy_name].modified_data.blocs[i].position.y)
Le dictionnaire Simu.metrics contient pour chaque stratégies le temps d'exécution, le nombre d'échec de placement sur le nombre de blocs total et la surface des blocs non placés sur la somme 
de a surface de l'ensemble des blocs. Sa structure est la suivante: {strategy_name: execution_time, unplaced_blocs, surface_unplaced_blocs}


LANCEMENT DE L'INTERFACE (VISUALISATION D'UNE STRATEGIES)
===========================================================



MODIFICATIONS DES DONNEES D'ENTREES
===========================================================
Afin de modifier les données d'entrées, il suffit de mofifier ou remplacer le fichier donnees_entree.xlsx contenu dans le dossier Simulation. 
Il est nécessaire d'utiliser la même structure de données et d'utiliser un fichier .xlsx.

AJOUT D'UN ALGORITME
===========================================================
Afin d'ajouter un algorithme de résolution du problème d'optimisation traité, il est d'abord nécessaire de créer une copie du fichier strategy_exemple.py situé dans le dossier Simulation et de
le renommer le fichier et la la classe implémentées dans ce fichier avec le nom de votre strategie en respectant les formats suivant:
		-strategy_name pour le nom du fichier;
		-StrategyName pour le nom de la claase.
Vous implémenterez ensuite votre algorithme de résolution en complétant la fonction launch_simulation().Pour cela, vous utiliserez les instructions vis-à-vis des noms des variables et des fonctions
contenu dans le fichier copié.
Dans le fichier simulation_manager.py du dossier Simulation, vous ajouterez la ligne "from Simulation.strategy_name import StrategyName" au début du fichier.
Il suffit ensuite de rajouter le nom de la de la classe (StrategyName) dans la liste strategies_name et d'éxecuter le fichier main. 