import random

def ouvrir_fichier():
    try:
        with open("mots_pendu.txt", 'r',encoding='utf-8') as mots_pendu:
            mots = [ligne.strip() for ligne in mots_pendu if ligne.strip()]
        return mots
    except FileNotFoundError:
        print("Le fichier 'mots_pendu.txt' n'a pas été trouvé.")
        return []

mots = ouvrir_fichier()
def choisir_mot(mots):
    return random.choice(mots)

mot_aleatoire= choisir_mot(mots)
print(f"Le mot à deviner est : ", mot_aleatoire)

def affichage_under_score(mot):
    return '_' * len(mot)
mot_cache = affichage_under_score(mot_aleatoire)
print(f'Mots :',mot_cache)

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



# Initialiser le nombre d'essais restants
essais_restants = 6
indice_donne = False
while essais_restants > 0:
    indice_donne=hint(mot_aleatoire, essais_restants, mot_cache,indice_donne)
    print("Il vous reste ", essais_restants, " essais")
    lettre = entrer_lettre()
    
    

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
    if verifier_gagne(mot_cache, mot_aleatoire) or essais_restants == 0:
        if essais_restants == 0:
            print("Vous avez perdu ! Le mot était :", mot_aleatoire)
        # Demander à l'utilisateur s'il veut rejouer
        replay = input("Voulez-vous rejouer ? (O/N) : ")
        if replay.lower() == 'o':
            essais_restants = 6
            mot_aleatoire = choisir_mot(mots)
            print(f"Le mot à deviner est : ", mot_aleatoire)
            mot_cache = affichage_under_score(mot_aleatoire)
            continue
        else:
            print("Merci d'avoir joué !")
        break

