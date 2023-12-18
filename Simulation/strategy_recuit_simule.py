from Simulation.strategy import Strategy
from Simulation.simulation_context import SimulationContext
from Data.position import Position
from Simulation.constraints_motor import ConstraintsMotor
import time
import math
import random
import copy


class StrategyRecuitSimule(Strategy):
    def __init__(self,data):
        self.name=self.__class__.__name__
        self.simu : SimulationContext = SimulationContext(self.name,data)
    
    
    def launch_strategy(self):
        ti=time.time()
        data=self.simu.modified_data
        
        temp_initiale = 1000
        refroidissement = 0.95
        temp_finale = 1

        self.recuit_simule(data, temp_initiale, refroidissement, temp_finale)
        
        self.simu.modified_data=data
        tf=time.time()
        self.simu.execution_time=tf-ti
        pass
    
    def recuit_simule(self, data_set, temp_initiale, refroidissement, temp_finale):
        
        # Initialiser la solution actuelle et la meilleure solution

        self.initialiser_solution(data_set)
        data_actuelle=copy.deepcopy(data_set)
        data_voisine=copy.deepcopy(data_set)
        temperature = temp_initiale

        # Boucle principale de l'algorithme
        while temperature > temp_finale:
            self.generer_solution_voisine(data_voisine)


            # Évaluer les solutions
            cout_actuel = self.evaluer_solution(data_actuelle)
            cout_voisin = self.evaluer_solution(data_voisine)

            # Calculer le delta de coût
            delta = cout_voisin - cout_actuel

            # Décider d'accepter ou non la nouvelle solution
            if delta < 0 or self.accepter_solution(delta, temperature):
                data_actuelle=copy.deepcopy(data_voisine)
                print("nouvelle solution acceptable")


                # Mise à jour de la meilleure solution si nécessaire
                if cout_voisin < self.evaluer_solution(data_set):
                    data_set = copy.deepcopy(data_voisine)
                    print("nouvelle meilleure solution")


            # Diminuer la température
            temperature *= refroidissement
        




    def initialiser_solution(self, data_set):
        # Essayer de placer les blocs par ordre de surface décroissante
        blocs_tries = sorted(data_set.blocs, key=lambda bloc: ( (bloc.width)*(-bloc.length),bloc.arrival_date))
        k=0
        
        # On essaye de placer chaque blocs à chaque coordonnées entières de chaque zones
        for bloc in blocs_tries:
            position_trouvee = False
            for zone in data_set.zones[1:4]:
                for y in range(int(zone.width )):
                    for x in range(int(zone.length )):
                        pos=Position(zone,x,y)
                        constraints_motor=ConstraintsMotor(data_set.blocs)
                        if constraints_motor.verify_constraints(bloc,pos)==1:
                            bloc.place(pos)
                            position_trouvee = True
                        if position_trouvee:
                            break
                        
                    if position_trouvee:
                        break

                if position_trouvee:
                    break

            k+=1
            print(k)
            
            
            # Si aucune position possible n'est trouvée pour un bloc, on les place dans la zone d'échecs
            if not position_trouvee:
                pos=Position(data_set.zones[0],0,bloc.width)
                bloc.place(pos)






    def generer_solution_voisine(self,data_set):
        """
        Génère une solution voisine en modifiant légèrement la solution actuelle.
        """
        # Déplacer un bloc aléatoire vers une autre zone aléatoire à une position aléatoire dans cette zone
       
        bloc_a_deplacer = random.choice(data_set.blocs)
        zone_cible = random.choice(data_set.zones[1:4])
        x=random.uniform(0,zone_cible.length-bloc_a_deplacer.length)
        y=random.uniform(0,zone_cible.width-bloc_a_deplacer.width)
        pos=Position(zone_cible,x,y)
        constraints_motor=ConstraintsMotor(data_set.blocs)
        
        # Vérification des contraintes avant de déplacer le bloc
        if constraints_motor.verify_constraints(bloc_a_deplacer,pos)==1:
            bloc_a_deplacer.place(pos)
            print(bloc_a_deplacer.name, "a été déplacé")
            
            # Si le bloc est déplacé, on essaye de placer les blocs de la zone d'échecs
            echecs=[]
            for bloc in data_set.blocs:
                if bloc.position.zone.name==data_set.zones[0].name:
                    echecs.append(bloc)
                        
             
            for bloc in echecs:
                position_trouvee = False
                for zone in data_set.zones[1:4]:
                    for y in range(int(zone.width )):
                        for x in range(int(zone.length )):
                            pos=Position(zone,x,y)
                            constraints_motor=ConstraintsMotor(data_set.blocs)
                            if constraints_motor.verify_constraints(bloc,pos)==1:
                                bloc.place(pos)
                                position_trouvee = True
                                print("un bloc de la zone d'échecs a pu être placé")
                            if position_trouvee:
                                break
                                
                        if position_trouvee:
                            break
    
                    if position_trouvee:
                         break




    def evaluer_solution(self,data_set):
        """
        Évalue la qualité d'une solution.
        """
        # compter le nombre de blocs placés dans les zones autres que la zone d'échecs
        qualite = sum(1 for bloc in data_set.blocs if bloc.position.zone.name!= data_set.zones[0].name)
        return qualite

    def accepter_solution(self, delta, temperature):
        """
        Décide si une nouvelle solution doit être acceptée ou non.
        """

        proba = math.exp(delta / temperature)
        return random.random() < proba