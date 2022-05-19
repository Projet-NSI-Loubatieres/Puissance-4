from turtle import *

class Grille:

# intitialisation de la grille vide (0 = vide, 1 = rouge, 2 = bleu)

    def __init__(self, grille):
        self.grille = grille

# Pour les classes il faut redéfinir la fonction print avec le __repr__

    def __repr__(self):
        return repr(self.grille)

# Il faut également régler les problèmes d'indexage avec le __getitem__

    def __getitem__(self, i):
        return self.grille[i]

#..............................................................................#
# La fonction dessiner() dessine une grille vide dans la fenêtre
# de la tortue
# Entrées : coordonnées du point de départ
# Sortie : affichage turtle de la grille vide
#..............................................................................#

    def dessiner(x_base, y_base, largeur):
        up()
        goto(x_base,y_base)
        down()
        for i in range(8):                        # traits horizontaux
            forward(7*largeur)
            up()
            goto(x_base,y_base+i*largeur)
            down()
        up()                                      # traits verticaux
        goto(x_base,y_base)
        setheading(90)
        down()
        for i in range(9):
            forward(6*largeur)
            up()
            goto(x_base+i*largeur,y_base)
            down()
        for i in range(7):                  # affiche le numéro des colonnes sous la grille :
            up()
            goto(x_base+i*largeur+largeur//2,y_base-largeur//2) # se met au milieu de la case
            down()
            write(str(i))

#..............................................................................#
# La fonction est_pleine() vérifie si la grille est pleine
# Entrées : grille
# Sortie : True ou False
#..............................................................................#

    def est_pleine(grille):
        est_pleine = True
        for i in range(6):
            for j in range(7):
                if grille[i][j]==0:
                    est_pleine=False
        return est_pleine

#..............................................................................#
# La fonction afficher() affiche la grille
# Entrées : grille
# Sortie : grille
#..............................................................................#

    def afficher(grille):
        for i in range(6):
            print(grille[i])

#..............................................................................#
# La fonction dessiner_pion(x,y,couleur) ajoute un pion dans la case (x,y))
# Entrées : colonne (x de 0 à 6) et ligne (y de 0 à 5)
# Sortie : afficheage turtle du pion dans la case
#..............................................................................#

    def dessiner_pion(x,y,couleur):
        up()
        goto(x_base + (x+1)*largeur - largeur//8 , y_base+(y+1)*largeur-largeur//2)
        down()
        if couleur==1:
            # pion ROUGE si couleur=1 :
            color('red')
        else:
            # pion BLEU si couleur=2 :
            color('blue')
        begin_fill()
        circle(largeur/2.5)
        end_fill()