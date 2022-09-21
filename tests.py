"""
Une cellule vivante ave moins de 2 voisins vivants meurt 
Une cellule vivante avec 2 ou 3 voisins survit
une cellule vivante avec plus de 3 voisins meurt
une cellule morte avec exactement 3 voisins vivants devient vivante

"""

class Jdlv:
    def __init__(self, path: str):
        with open(path, 'r') as fichier:
            lignes = fichier.read().split("\n")
            en_tete = lignes[0].split(" ")
            self.n = int(en_tete[0])
            self.m = int(en_tete[1])


def test1():
    jdlv = Jdlv("jdlv.txt")
    assert jdlv.n == 4
    assert jdlv.m == 8

test1()

