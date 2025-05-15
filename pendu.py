import random
import pendu_lib 
from pendu_lib import acceuil, init, hint, entrer_lettre, check_lettre, verifier_gagne, afficher_pendu, replay

mots=acceuil()

if mots== False:
    print("Aucun mot disponible pour le jeu.")
    exit()
essais_restants, mot_aleatoire, mot_cache,indice_donne=init(mots)

while essais_restants > 0:
    indice_donne=hint(mot_aleatoire, essais_restants, mot_cache,indice_donne)
    print("Il vous reste ", essais_restants, " essais")
    afficher_pendu(essais_restants)
    lettre = entrer_lettre()
    

    essais_restants,mot_cache=check_lettre(lettre,mot_aleatoire,mot_cache,essais_restants)
    if verifier_gagne(mot_cache, mot_aleatoire) or essais_restants == 0:
        if essais_restants == 0:
            print("Vous avez perdu ! Le mot était :", mot_aleatoire)
            afficher_pendu(essais_restants)

        essais_restants,mot_aleatoire,mot_cache,indice_donne=replay()
 
