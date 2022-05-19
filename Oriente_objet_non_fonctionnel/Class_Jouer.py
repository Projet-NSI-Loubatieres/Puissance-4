class Jouer():

    def __init__(self, joueur_courant, joueur):
        self.joueur_courant = joueur_courant
        self.joueur = joueur

#..............................................................................#
# La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6 #
# et réitère la demande tant que la valeur saisie n'est pas un entier dans cet #
# intervale. Ne provoque pas d'erreurs pour que le programme se poursuive.     #
# Elle renvoie la colonne dans laquelle jouer                                  #
#..............................................................................#

    def tester_saisie(self, joueur_courant):
        if self.joueur_courant == 1:
            self.joueur = 'ROUGE'
        else:
            self.joueur = 'BLEU'
        saisie_correct = False
        while not saisie_correct:
            s_colonne = input(" : entrez la colonne où jouer (de 0 à 6) :")

            # teste si s_colonne est un entier :
            if not s_colonne.isdigit():
                print("Erreur de saise : la valeur entrée par le joueur",self.joueur,"n'est pas un nombre entier. Recommencez.")

            # teste si s_colonne est comprise entre 0 et 6 :
            elif int(s_colonne) < 0 or int(s_colonne) > 6:
                print("Erreur de saise : la valeur numérique entrée par le joueur",self.joueur,"n'est pas comprise entre 0 et 6. Recommencez.")

            else:
                saisie_correct = True

        # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
        return s_colonne

#..............................................................................#
# La fonction jouer() demande au joueur courant dans quelle colonne            #
# il veut jouer                                                                #
#..............................................................................#

    def jouer(self, joueur_courant):
        if self.joueur_courant==1:
            self.joueur='ROUGE'

        else:
            self.joueur='BLEU'

        # La fonction tester_saisie renvoie la colonne dans laquelle jouer
        colonne = self.tester_saisie(self.joueur_courant)

        while tab_colonne[colonne]==6:
            print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,self.joueur))
            colonne=self.tester_saisie(self.joueur_courant)
        grille[5-tab_colonne[colonne]][colonne]=self.joueur_courant

        # dessine le pion sur la grille graphique :
        dessiner_pion(colonne,tab_colonne[colonne],self.joueur_courant)
        tab_colonne[colonne]+=1
        print('\nLe joueur %s vient de jouer dans la colonne %d :' % (self.joueur,colonne))

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