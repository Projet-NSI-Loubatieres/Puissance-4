# Créé par Louis et Thibaud le 06/04/2022

# - dessine la grille graphiquement dans une fenêtre de la tortue (module turtle)
# - demande aux joueurs à tour de role dans quelle colonne ils veulent jouer

# boucle:

    # - filtre la saisie de l'utilisateur et envoie un message sur la sortie standard si la saisie est erronée
    # - détecte une colonne pleine
    # - détecte la grille pleine
    # - détecte 4 pions alignés verticalement
    # - détecte 4 pions (ou plus) alignés horizontalement
    # - détecte 4 pions (ou plus) alignés en diagonale croissante
    # - détecte 4 pions (ou plus) alignés en diagonale décroissante

from Class_Grille import *
from Class_Jouer import *

grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant = Jouer(1, 0)              # désignation du premier joueur (rouge)

#..............................................................................#
#                            CORPS DU PROGRAMME                                #
#..............................................................................#

grille = Grille([7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]])
hideturtle()
speed(0)
Grille.dessiner(-200, -200, 60)

class puissance4(Grille, Jouer):

    def __init__(self, gagnant, joueur_courant):
        self.gagnant = 0
        self.joueur_courant = Jouer(1, 0)

    def partie(self):

        while not(Grille.est_pleine(grille)) and self.gagnant==0:
            Jouer.jouer(self.joueur_courant)
            self.joueur_courant=3-self.joueur_courant
            self.gagnant=Jouer.pions_alignes()
            if self.gagnant==1:
                print('Bravo ! Le joueur ROUGE a gagné !')
            elif self.gagnant==2:
                print('Bravo ! Le joueur BLEU a gagné !')

jeu = puissance4(Grille, Jouer)
jeu.partie()