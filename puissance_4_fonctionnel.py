# Créé par Louis et Thibaud le 06/04/2022

from turtle import *

# boucle:

    # - filtre la saisie de l'utilisateur et envoie un message sur la sortie standard si la saisie est erronée
    # - détecte une colonne pleine
    # - détecte la grille pleine
    # - détecte 4 pions alignés verticalement
    # - détecte 4 pions (ou plus) alignés horizontalement
    # - détecte 4 pions (ou plus) alignés en diagonale croissante
    # - détecte 4 pions (ou plus) alignés en diagonale décroissante

#..............................................................................#
# La fonction est_pleine() vérifie si la grille est pleine
# Entrées : grille
# Sortie : True ou False
#..............................................................................#

def grille_pleine(grille):
    est_pleine = True
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                est_pleine=False
    return est_pleine

#..............................................................................#
# La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
# Entrées : grille
# Sortie : 0 ou 1
#..............................................................................#

def pions_alignes():
    trouve=0
    for i in range(6):            # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
        rouge=0
        bleu=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    for j in range(7):            # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
        rouge=0
        bleu=0
        for i in range(6):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    # teste les 6 diagonales croissantes possibles (allant d'en bas à gauche à en haut à droite):

    # test des 2 diagonales croissantes à 4 cases :
    rouge=[0,0]   # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(4):
        i=3-j
        k=i+2
        l=j+3
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 5 cases :
    rouge=[0,0]   # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(5):
        i=4-j
        k=i+1
        l=j+2
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 6 cases :
    rouge=[0,0] # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(6):
        i=5-j
        k=i
        l=j+1
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # teste les 6 diagonales décroissantes (d'en haut à gauche à en bas à droite) :

    # test des 2 diagonales décroissantes à 4 cases :
    rouge=[0,0]    # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(3,7):
        i=j-3
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 5 cases :
    rouge=[0,0] # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(2,7):
        i=j-2
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 6 cases :
    rouge=[0,0] # on réinitialise les compteurs des pions alignés pour le joueur 'ROUGE' et 'BLEU'
    bleu=[0,0]

    for j in range(1,7):
        i=j-1
        k=i
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # si on n'a rien trouvé on retourne 0, la partie est un match nul
    return trouve

#..............................................................................#
# La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6 #
# et réitère la demande tant que la valeur saisie n'est pas un entier dans cet #
# intervale. Ne provoque pas d'erreurs pour que le programme se poursuive.     #
# Elle renvoie la colonne dans laquelle jouer                                  #
#..............................................................................#

def tester_saisie(joueur_courant):
    if joueur_courant == 1:
        joueur = 'ROUGE'
    else:
        joueur = 'BLEU'
    saisie_correct = False
    while not saisie_correct:
        s_colonne = input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)
        # teste si s_colonne est un entier :
        if not s_colonne.isdigit():
            print("Erreur de saise : la valeur entrée par le joueur",joueur,"n'est pas un nombre entier. Recommencez.")
                # teste si s_colonne est comprise entre 0 et 6 :
        elif int(s_colonne) < 0 or int(s_colonne) > 6:
            print("Erreur de saise : la valeur numérique entrée par le joueur",joueur,"n'est pas comprise entre 0 et 6. Recommencez.")
        else:
            saisie_correct = True
        # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
    return int(s_colonne)


#..............................................................................#
# La fonction jouer() demande au joueur courant dans quelle colonne il veut jouer
#
#..............................................................................#

def jouer(joueur_courant):
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
        # La fonction tester_saisie renvoie la colonne dans laquelle jouer
    colonne = tester_saisie(joueur_courant)
    while tab_colonne[colonne]==6:
        print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur))
        colonne = tester_saisie(joueur_courant)
        # dessine le pion sur la grille graphique :
    grille[5-tab_colonne[colonne]][colonne]=joueur_courant
    dessiner_pion(colonne,tab_colonne[colonne],joueur_courant)
    tab_colonne[colonne] += 1

#..............................................................................#
# La fonction dessiner_grille() dessine une grille vide dans la fenêtre
# de la tortue
# Entrées : coordonnées du point de départ
# Sortie : affichage turtle de la grille vide
#..............................................................................#

def dessiner_grille(x_base, y_base, largeur):
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

#..............................................................................#
# La fonction afficher_grille() affiche la grille
# Entrées : grille
# Sortie : grille
#..............................................................................#

def afficher_grille(grille):
    for i in range(6):
        print(grille[i])

#..............................................................................#
#                            CORPS DU PROGRAMME                                #
#..............................................................................#


grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant=1          # le premier joueur est 'ROUGE'

largeur=60              # taille d'une case
x_base=-200             # coordonnées du point le plus en bas à gauche (départ)
y_base=-200             # coordonnées du point le plus en bas à gauche (départ)
speed(0)                # vitesse du tracé
hideturtle()            # cache le curseur
dessiner_grille(x_base, y_base, largeur)
gagnant=0               # la partie est un match nul tant que personne n'a gagné

while not grille_pleine(grille) and gagnant==0: # tant que la grille n'est pas pleine et qu'il n'y a pas de gagnant
    jouer(joueur_courant)                      # la partie continue
    joueur_courant=3-joueur_courant            # indique le joueur suivant
    gagnant=pions_alignes()                    # gagnant peut prendre comme valeur 0 (match nul), 1 ('ROUGE') et 2 ('BLEU')
    if gagnant==1:
        print('Bravo ! Le joueur ROUGE a gagné !')
    elif gagnant==2:
        print('Bravo ! Le joueur BLEU a gagné !')

if gagnant==0:
    print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
done()