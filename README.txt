Projet ACCRO
==========================================================
Ce programme a été conçu par Maxime Chanssat, Florian Desplanques, Elouan Nicolas, Hamidou Kane et Lucie Berger dans le cadre d'un projet de l'UE Projet Commande Entreprise de IMT Atlantique.
Décembre 2023

INSTALLATION PREALABLE
==========================================================
Sur le Git Projet-ACCRO, vous devez récupérer l'ensemble des fichiers les dossiers Simulation et Data avec l'ensemble des fichiers .py qu'ils contiennent et les enregistrer dans un même dossier sur votre ordinateur.
Vous récupérerez également le fichier Interface.py et le placerez dans le même dossier.

LANCEMENT ET COMPARAISON DES DIFFERENTES STRATEGIES
==========================================================
Pour lancer le programme, il suffit d'exécuter le fichier main.py contenu dans le dossier Simulation.
Pour différents noms de stratégies "strategy_name", les variables Simu.contexts[strategy_name].modified_data  contiennent les résultats de la simulation lors de l'application de cette stratégie.
Ces objets contiennent notament un attribu blocs cotenant l'ensembles des blocs du problème dont la zone et la position (x,y) du bloc i sont repectivement définies par:
		-Simu.contexts[strategy_name].modified_data.blocs[i].position.zone
		-(Simu.contexts[strategy_name].modified_data.blocs[i].position.x, Simu.contexts[strategy_name].modified_data.blocs[i].position.y)
Le dictionnaire Simu.metrics contient pour chaque stratégies le temps d'exécution, le nombre d'échec de placement sur le nombre de blocs total et la surface des blocs non placés sur la somme 
de a surface de l'ensemble des blocs. Sa structure est la suivante: {strategy_name: execution_time, unplaced_blocs, surface_unplaced_blocs}

LANCEMENT DE L'INTERFACE (VISUALISATION D'UNE STRATEGIE)
===========================================================
Pour lancer l'interface avec une méthode de son choix, il faut enregistrer à la fin de chaque programme d'optimisation vos deux listes de résultats "blocs_placés" et de "blocs_non_placés" de telle façon : 

import pickle

with open('nom_méthode_placés.pkl', 'wb') as fichier:
    pickle.dump(bloc_placés, fichier)

with open('noù_méthode_non_placés.pkl', 'wb') as fichier:
    pickle.dump(blocs_non_placés, fichier)    

Ces lignes de code vont enregistrer, dans le même répertoire de votre code d'optimisation, deux fichiers .pkl que vous devez placer dans le même répertoire où se trouve Interface.py. Ces deux fichiers ont comme nom "nom_méthode_placés.pkl" et "non_méthode_non_placés.pkl", vous remplacez cet exemple avec le nom de votre méthode par exemple. Puis dans le fichier Interface.py, vous allez à la ligne 102 du code où l'on trouve :

with open('nom_méthode_placés.pkl', 'rb') as fichier:
    colis_placer_pas_corrigé = pickle.load(fichier)

with open('non_méthode_non_placés.pkl', 'rb') as fichier:
    colis_pas_placer_pas_corrigé = pickle.load(fichier)

Là vous remplacez les noms des fichiers préécrits par les noms que vous avez choisi. Puis il vous suffit d'exécuter le programme pour voir s'afficher l'interface.

UTILISATION DE L'INTERFACE (VISUALISATION D'UNE STRATEGIE)
===========================================================
La partie gauche de l’interface décline les trois zones de placement (“A”, “B” et “C”). On y voit les blocs placés qui sont différenciés par leur nom “Bloc n”.
La partie haut-droite de l’interface est une zone d’échecs de placement qui regroupe successivement les blocs que l’algorithme d’optimisation en question n’a pu placer.
La partie bas-droite de l’interface contient les éléments interactifs de cette fenêtre :  
	Tout d’abord, en commençant par le haut, on retrouve un menu déroulant qui permet de sélectionner avec quelle solution d’optimisation nous souhaitons que l’interface affiche le placement des blocs. Cette fonctionnalité n'est pas effective dans cette version de l'interface. En effet, le menu déroulant avait pour objectif de mettre en place cette fonctionnalité mais, par manque de temps, nous n'avons pas pu mettre en œuvre la “logique algorithmique” derrière. En d’autres termes, le menu déroulant est présent sur l’interface mais changer de solution, par exemple passer de la “Solution_1” à “Solution_2” ou “Solution_3”, ne change pas la solution. C’est la même solution qui est présente sous ces 3 dénominations. De fait, ce qu’il faudrait faire, c’est réussir à entrer tous les résultats (les deux listes de blocs placés et de blocs non placés) de chacun des algorithmes implémentés pour ensuite les “affecter” à chacune des variables du menu déroulant. De sorte que lorsque que l’on change de solution sur le menu déroulant, ce soit bien une méthode différente qui place les blocs.
	Ensuite est affichée la date à laquelle est rendue la simulation ; la première date affichée étant celle du premier placement de bloc et la dernière, la dernier départ de bloc. Est affiché aussi le nombre d’actions à accomplir avant la fin de la simulation ; une action étant soit un placement de bloc soit un départ de bloc.
	A la suite de cela, on retrouve un curseur dont les valeurs correspondent aux actions à accomplir. Placer le curseur à la nième action affiche automatiquement le placement des blocs jusqu’à cette nième action. Appuyer sur le bouton “Launch”, avec le curseur placé à la nième action, affiche le placement successif des blocs jusqu’à cette nième action. Ainsi pour afficher le placement successif de tous les blocs, il suffit de mettre le curseur le plus à droite possible et de cliquer sur le bouton "Launch"
	Enfin, nous avons placé 4 boutons. Le premier bouton “Courbes d’analyse” affiche des graphiques permettant de comparer les algorithmes. Les données des graphiques sont à changer manuellement dans la partie "Dictionnaires de résultats statistiques" du code de l'interface.
	Les trois autres boutons “Launch”, “Pause/Play” et “Reset” permettent respectivement de lancer la simulation d’agencement des blocs, mettre en pause ou relancer cette simulation, et remettre au point de départ la simulation.
Dans une volonté de rendre plus interactive notre interface, nous avons aussi codé des fonctions de “drag” dans chacune des trois zones de placement de blocs qui permettent, avec un clic gauche maintenu sur la souris, de déplacer les blocs au sein de leur zone attitrée. Cette fonctionnalité avait pour but de nous permettre de questionner la stratégie de placement des blocs de nos algorithmes en déplaçant manuellement les blocs pour savoir si on ne pouvait pas les placer autre part. Elle nous a aussi permis, dans certaines situations ambiguës, d’apprécier le respect de la contrainte du placement des blocs à l’intérieur des zones sans chevauchement sur leurs frontières. En effet, il nous suffisait pour cela de légèrement mouvoir le bloc en question pour lever tout doute.

PISTES D'AMÉLIORATIONS DE L'INTERFACE
===========================================================
	La fonction de drag ne permet, actuellement, de mouvoir les blocs qu’au sein de la zone à laquelle ils appartiennent. Il pourrait être intéressant de pouvoir mouvoir les blocs entre les zones et notamment depuis la zone “Échecs de placement” afin de mieux apprécier si oui ou non un bloc étant effectivement impossible à placer à un instant donné ou si l'algorithme de placement n’a pas “vu” un espace pourtant disponible.
	Un ajout qui pourrait rendre plus réaliste ou “industrialisable” notre interface serait de rajouter un bouton “Fichier excel” qui renvoie sur le répertoire de l’utilisateur afin de pouvoir changer l’excel en entrée et donc les données entrantes.
	Il faudrait aussi revoir les façons de dimensionner la fenêtre. En effet, on a décidé de ne pas utiliser de valeurs numériques mais d'utiliser une fonction tkinter qui adapte la fenêtre aux dimensions du PC de chaque utilisateur car avec des valeurs numériques l'entièreté de la fenêtre ne s'affichait pas selon le PC. Néanmoins, ces fonctions ont réglé partiellement le problème étant donné que pour certains d'entre nous, toute la fenêtre s'affiche mais la zone “C” est plus ou moins "ratatinée". Sur un PC 17 pouces en revanche, toute la fenêtre s’affiche avec des zones bien dimensionnées. 
	En découvrant notre interface, notre client nous avait aussi donné quelques pistes d’amélioration possibles à implémenter si nous en avions le temps. De fait, cela donne des idées d’amélioration pour un prochain groupe : - Ajouter un bouton “+” et un bouton “-” à côté de la date de la partie en bas à droite de l’interface pour naviguer dans la simulation avec un pas journalier.
	 - Ajouter un label “Nombre de blocs” qui permet de définir directement sur l’interface combien de blocs on souhaite placer.

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