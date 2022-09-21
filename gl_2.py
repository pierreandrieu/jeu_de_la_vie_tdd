"""
Une cellule vivante ave moins de 2 voisins vivants meurt 
Une cellule vivante avec 2 ou 3 voisins survit
une cellule vivante avec plus de 3 voisins meurt
une cellule morte avec exactement 3 voisins vivants devient vivante

"""

class Jdlv:
    def __init__(self, path: str):
        self.n = 4
        self.m = 8


def test1():
    jdlv = Jdlv("jdlv.txt")
    assert jdlv.n == 4
    assert jdlv.m == 8

test1()

