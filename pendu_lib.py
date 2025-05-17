import random


def afficher_pendu(essais_restants):
    """Affiche l'état du pendu selon le nombre d'essais restants."""
    #Etat des de 6 essais restants à 0
    etats = [
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """
    ]
    print(etats[essais_restants])


def init_path():
    """Demande à l'utilisateur le chemin du fichier de mots ou utilise le fichier par défaut.
    
    Returns:
        str or None: Le chemin du fichier ou None si vide.
    """
    path = input("Entrez le chemin du fichier de mots (laisser vide pour le fichier par défaut) : ")
    if path == '':
        path = None
    return path


def ouvrir_fichier(path):
    """Ouvre le fichier de mots et retourne une liste de mots.

    Args:
        path (str or None): Chemin du fichier à ouvrir, ou None pour le fichier par défaut.

    Returns:
        list: Liste des mots lus dans le fichier, ou False si le fichier n'est pas trouvé.
    """
    # Si aucun chemin n'est donné, utilise le fichier par défaut
    if path is None:
        try:
            with open("mots_pendu.txt", 'r', encoding='utf-8') as mots_pendu:
                # Lit chaque ligne, enlève les espaces et ignore les lignes vides
                mots = [ligne.strip() for ligne in mots_pendu if ligne.strip()]
            return mots
        except FileNotFoundError:
            print("Le fichier 'mots_pendu.txt' n'a pas été trouvé.")
            return False
    # Sinon, utilise le chemin donné par l'utilisateur
    else:
        try:
            with open(path, 'r', encoding='utf-8') as mots_pendu:
                mots = [ligne.strip() for ligne in mots_pendu if ligne.strip()]
            return mots
        except FileNotFoundError:
            print("Le fichier sélectionné n'a pas été trouvé.")
            return False


def remplacer_accent(mot):
    """Remplace les accents dans un mot par leur équivalent sans accent.

    Args:
        mot (str): Le mot à traiter.

    Returns:
        str: Le mot sans accents.
    """
    accents = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'ô': 'o', 'ö': 'o',
        'ç': 'c',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'î': 'i', 'ï': 'i',
    }
    # Remplace chaque accent par son équivalent sans accent
    for accent, replacement in accents.items():
        mot = mot.replace(accent, replacement)
    return mot


def choisir_mot(mots):
    """Retourne un mot aléatoire de la liste de mots.

    Args:
        mots (list): Liste des mots.

    Returns:
        str: Un mot choisi aléatoirement.
    """
    return random.choice(mots)


def affichage_under_score(mot):
    """Retourne une chaîne d'underscores de la longueur du mot à deviner.

    Args:
        mot (str): Le mot à deviner.

    Returns:
        str: Chaîne d'underscores.
    """
    return '_' * len(mot)


def entrer_lettre():
    """Demande à l'utilisateur d'entrer une lettre et la retourne en minuscule.

    Returns:
        str: La lettre entrée par l'utilisateur.
    """
    while True:
        lettre = input("Entrez une lettre : ")
        # Vérifie que l'utilisateur entre bien une seule lettre alphabétique
        if len(lettre) == 1 and lettre.isalpha():
            return lettre.lower()
        else:
            print("Veuillez entrer une seule lettre.")


def verifier_gagne(mot_cache, mot_aleatoire):
    """Vérifie si le joueur a gagné en comparant le mot caché et le mot à deviner.

    Args:
        mot_cache (str): Mot affiché avec les lettres trouvées.
        mot_aleatoire (str): Mot à deviner.

    Returns:
        bool: True si le joueur a gagné, False sinon.
    """
    if mot_cache == mot_aleatoire:
        print("Vous avez gagné ! Le mot était :", mot_aleatoire)
        return True
    else:
        return False


def hint(mot_aleatoire, essais_restants, mot_cache, indice_donne):
    """Donne un indice au joueur si nécessaire.

    Args:
        mot_aleatoire (str): Mot à deviner.
        essais_restants (int): Nombre d'essais restants.
        mot_cache (str): Mot affiché avec les lettres trouvées.
        indice_donne (bool): Indique si l'indice a déjà été donné.

    Returns:
        bool: True si un indice a été donné, sinon la valeur de indice_donne.
    """
    #Vérifie si l'indice a déjà été donné
    if indice_donne:
        return True
    # Donne un indice si il reste un seul essai et que la première lettre n'est pas déjà révélée
    elif essais_restants == 1 and mot_cache[0] == '_':
        print("Indice : Le mot commence par la lettre '", mot_aleatoire[0], "'")
        return True
    # Donne un indice si il reste un seul essai et que la première lettre est déjà révélée
    elif essais_restants == 1:
        index = random.randint(0, len(mot_aleatoire) - 1)
        # Trouve une lettre non révélée dans le mot
        while mot_cache[index] != '_':
            index = random.randint(0, len(mot_aleatoire) - 1)
        print(f"Indice : La lettre à la position {index + 1} est '{mot_aleatoire[index]}'.")
        mot_cache = mot_cache[:index] + mot_aleatoire[index] + mot_cache[index + 1:]
        print("Mot : ", mot_cache)
        return True
    return indice_donne


def check_lettre(lettre, mot_aleatoire, mot_cache, essais_restants):
    """Vérifie si la lettre proposée est dans le mot à deviner.

    Args:
        lettre (str): Lettre proposée.
        mot_aleatoire (str): Mot à deviner.
        mot_cache (str): Mot affiché avec les lettres trouvées.
        essais_restants (int): Nombre d'essais restants.

    Returns:
        tuple: (essais_restants, mot_cache) mis à jour.
    """
    if lettre in mot_aleatoire:
        print("Bien joué ! La lettre est dans le mot.")
        # Met à jour le mot caché avec la lettre trouvée
        for j in range(len(mot_aleatoire)):
            if mot_aleatoire[j] == lettre:
                mot_cache = mot_cache[:j] + lettre + mot_cache[j + 1:]
        print("Mot : ", mot_cache)
    else:
        print("Dommage ! La lettre n'est pas dans le mot.")
        print("Vous avez perdu un essai.")
        essais_restants -= 1
    return essais_restants, mot_cache


def replay(mots):
    """Demande au joueur s'il veut rejouer et réinitialise la partie si besoin.

     Args:
        mots (list): Liste des mots.

    Returns:
        tuple: (essais_restants, mot_aleatoire, mot_cache, indice_donne) si rejoue,
               (0, None, None, None) sinon.
    """
    # Boucle jusqu'à ce que l'utilisateur entre une réponse valide
    while True:
        replay = input("Voulez-vous rejouer ? (O/N) : ")
        if len(replay) == 1 and replay.isalpha():
            replay = replay.lower()
            break
        else:
            print("Veuillez entrer une seule lettre.")

    if replay == 'o':
        return init(mots)
    else:
        print("Merci d'avoir joué !")
        return 0, None, None, None


def acceuil():
    """Affiche l'écran d'accueil et les règles du jeu, puis charge la liste des mots.

    Returns:
        list or bool: Liste des mots ou False si aucun mot n'est disponible.
    """
    # Affichage d'une illustration et des règles du jeu
    print("=======================================")
    print("      Bienvenue dans le jeu du Pendu ! ")
    print("=======================================")
    print("         +---+")
    print("         |   |")
    print("         O   |")
    print("        /|\\  |")
    print("        / \\  |")
    print("             |")
    print("      =========")
    print("Règles :")
    print("- Devinez le mot mystère en proposant une lettre à la fois.")
    print("- Vous avez 6 essais pour trouver le mot complet.")
    print("- Les accents sont remplacés par leur équivalent sans accent.")
    print("- Entrez une seule lettre à chaque essai.")
    print("---------------------------------------")
    # Demande le chemin du fichier de mots et charge la liste
    path = init_path()
    mots = ouvrir_fichier(path)
    if not mots:
        print("Aucun mot disponible pour le jeu.")
        return False
    else:
        return mots


def init(mots):
    """Initialise les variables pour une nouvelle partie.

    Args:
        mots (list): Liste des mots.

    Returns:
        tuple: (essais_restants, mot_aleatoire, mot_cache, indice_donne)
    """
    # Nombre d'essais au début de la partie
    essais_restants = 6
    indice_donne = False
    mot_aleatoire = choisir_mot(mots)
    mot_aleatoire = remplacer_accent(mot_aleatoire)
    mot_cache = affichage_under_score(mot_aleatoire)
    return essais_restants, mot_aleatoire, mot_cache, indice_donne


def pendu():
    """Lance la boucle principale du jeu du pendu."""
    mots = acceuil()
    if not mots:
        print("Aucun mot disponible pour le jeu.")
        exit()
    essais_restants, mot_aleatoire, mot_cache, indice_donne = init(mots)
    # Boucle principale du jeu
    while essais_restants > 0:
        # Donne un indice si besoin
        indice_donne = hint(mot_aleatoire, essais_restants, mot_cache, indice_donne)
        print("Il vous reste ", essais_restants, " essais")
        afficher_pendu(essais_restants)
        lettre = entrer_lettre()
        # Met à jour le mot caché et le nombre d'essais restants
        essais_restants, mot_cache = check_lettre(lettre, mot_aleatoire, mot_cache, essais_restants)
        if verifier_gagne(mot_cache, mot_aleatoire) or essais_restants == 0:
            if essais_restants == 0:
                print("Vous avez perdu ! Le mot était :", mot_aleatoire)
                afficher_pendu(essais_restants)
            # Propose de rejouer
            essais_restants, mot_aleatoire, mot_cache, indice_donne = replay(mots)

#Execution du jeu
if __name__ == "__main__":
    pendu()