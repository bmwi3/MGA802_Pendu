import random

def ouvrir_fichier():
    try:
        with open("mots_pendu.txt", 'r',encoding='utf-8') as mots_pendu:
            mots = [ligne.strip() for ligne in mots_pendu if ligne.strip()]
        return mots
    except FileNotFoundError:
        print("Le fichier 'mots_pendu.txt' n'a pas été trouvé.")
        return False

def remplacer_accent(mot):
    accents = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'ô': 'o', 'ö': 'o',
        'ç': 'c',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'î': 'i', 'ï': 'i',
    }
    for accent, replacement in accents.items():
        mot = mot.replace(accent, replacement)
    return mot

#mots = ouvrir_fichier()
def choisir_mot(mots):
    return random.choice(mots)

#mot_aleatoire= choisir_mot(mots)
# Remplacer les accents dans le mot choisi
#mot_aleatoire = remplacer_accent(mot_aleatoire)
#Deboguage
#print(f"Le mot à deviner est : ", mot_aleatoire)

def affichage_under_score(mot):
    return '_' * len(mot)
#mot_cache = affichage_under_score(mot_aleatoire)
#print(f'Mots :',mot_cache)

def entrer_lettre():
    while True:
        lettre = input("Entrez une lettre : ")
        if len(lettre) == 1 and lettre.isalpha():
            return lettre.lower()
        else:
            print("Veuillez entrer une seule lettre.")

def verifier_gagne(mot_cache, mot_aleatoire):
    if mot_cache == mot_aleatoire:
        print("Vous avez gagné ! Le mot était :", mot_aleatoire)
        return True
    else:
        return False

def hint(mot_aleatoire, essais_restants, mot_cache,indice_donne):
    if indice_donne:
        return True
    elif essais_restants == 1 and mot_cache[0] == '_':
        # Afficher la première lettre du mot
        print("Indice : Le mot commence par la lettre '", mot_aleatoire[0], "'")
        return True
    elif essais_restants == 1:
        # Afficher une lettre aléatoire du mot
        index = random.randint(0, len(mot_aleatoire) - 1)
        while mot_cache[index] != '_':
            index = random.randint(0, len(mot_aleatoire) - 1)

        print(f"Indice : La lettre à la position {index + 1} est '{mot_aleatoire[index]}'.")
        mot_cache = mot_cache[:index] + mot_aleatoire[index] + mot_cache[index + 1:]
        print("Mot : ", mot_cache)
        return True
    return indice_donne

def check_lettre(lettre,mot_aleatoire,mot_cache,essais_restants):
    if lettre in mot_aleatoire:
        print("Bien joué ! La lettre est dans le mot.")
        for j in range(len(mot_aleatoire)):
            if mot_aleatoire[j] == lettre:
                mot_cache = mot_cache[:j] + lettre + mot_cache[j+1:]
        print("Mot : ", mot_cache)
    else:
        print("Dommage ! La lettre n'est pas dans le mot.")
        print("Vous avez perdu un essai.")
        essais_restants -= 1
    return essais_restants,mot_cache

def replay():
    while True:
        replay = input("Voulez-vous rejouer ? (O/N) : ")
        if len(replay) == 1 and replay.isalpha():
            replay=replay.lower()
            break
        else:
            print("Veuillez entrer une seule lettre.")

    if replay.lower() == 'o':
        return init(mots)
    else:
        print("Merci d'avoir joué !")
        return 0, None, None, None




def acceuil():
    print("Bienvenue dans le jeu du Pendu !")
    print("Essayez de deviner le mot en entrant une lettre à la fois.")
    print("Vous avez 6 essais pour deviner le mot.")
    print("Les accents seront remplacés par leur équivalent sans accent.")
    mots=ouvrir_fichier()
    if mots== False:
        print("Aucun mot disponible pour le jeu.")
        return False
    else:
        return mots


def init(mots):
    essais_restants = 6
    indice_donne = False
    mot_aleatoire = choisir_mot(mots)
    mot_aleatoire = remplacer_accent(mot_aleatoire)
    print(f"Le mot à deviner est : ", mot_aleatoire)
    mot_cache = affichage_under_score(mot_aleatoire)
    return essais_restants, mot_aleatoire, mot_cache,indice_donne


mots=acceuil()

if mots== False:
    print("Aucun mot disponible pour le jeu.")
    exit()
essais_restants, mot_aleatoire, mot_cache,indice_donne=init(mots)

while essais_restants > 0:
    indice_donne=hint(mot_aleatoire, essais_restants, mot_cache,indice_donne)
    print("Il vous reste ", essais_restants, " essais")
    lettre = entrer_lettre()
    

    essais_restants,mot_cache=check_lettre(lettre,mot_aleatoire,mot_cache,essais_restants)
    if verifier_gagne(mot_cache, mot_aleatoire) or essais_restants == 0:
        if essais_restants == 0:
            print("Vous avez perdu ! Le mot était :", mot_aleatoire)
        essais_restants,mot_aleatoire,mot_cache,indice_donne=replay()
 
