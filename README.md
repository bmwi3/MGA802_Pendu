# MGA802_Pendu
## Présentation
### Introduction
Ce projet est un jeu du pendu en Python, à jouer dans le terminal.
Il est réalisé dans le cadre du cours MGA802.
Le but est de deviner un mot en proposant des lettres, avec un nombre limité d’essais.
Par souci de compatibilité python 3.9.12 a été utilisé.

### Règles du jeu
Devine le mot mystère en proposant une lettre à la fois.
Tu as 6 essais pour trouver le mot complet.
Les accents sont remplacés par leur équivalent sans accent.
Entre une seule lettre à chaque essai.
Si tu ne trouves pas le mot tu auras un indice pour ton dernier essai.
Tu pourras rejouer tant que tu le souhaites !

## Contenu du repositerie
Le dépôt est constitué de 3 fichiers principaux :
- `README.md` : Ce fichier, qui présente le projet.
- `mots_pendu.txt` : Le fichier contenant les mots à deviner (un mot par ligne).
- `pendu_vf.py` : Le script principal du jeu.

## Utilisation
Pour pouvoir jouer au pendu plusieurs options s'offre a toi
### Clonage du dépot
1. Clique sur le bouton `Code` en haut à droite du dépot
2. Copie le lien
3. Ouvre ton IDE favori sur lequel est configuré git
4. Clone le dépot soit de manière graphique soit en utilisant :
   ```bash
   git clone <https://github.com/bmwi3/MGA802_Pendu.git>
   ```
5. Ouvre le fichier `pendu_vf.py`.
6. Execute-le, il n'y a plus qu'à suivre les instructions dans le terminal

### Téléchargement du fichier 
1. Télécharge directement le fichier `pendu_vf.py` et `mots_pendu.txt`
2. Crée un dossier et mets les deux fichier à l'intérieur
3. Ouvre le dossier dans ton IDE favori et tu éxecute `pendu_vf.py`

### Option utilisation d'un autre dictionnaire que mots_pendu.txt
Si tu souhaites utiliser ton propres dictionnaires de mots pour jouer tu peux.
Pour cela il te suffit de spécifier le chemin d'accès de ton fichier lors du lancement du jeu.
Exemple de chemin d'accès : C:\Users\Julien\Downloads\ **test_v1.txt** 
Avec le nom du document texte à ouvrir, ici : **test_v1.txt** 
Attention à la séparation des mots dans le dictionnaire : chaque mot est à la ligne.