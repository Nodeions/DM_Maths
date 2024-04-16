from MathClass import *
from math import pi

def Exercice1(mat: Matrice3x3):
    """
    Dans le langage de votre choix, écrire une fonction prenant comme paramètre une matrice
    M3x3 et retournant une liste 𝑡𝑟𝑎𝑛𝑠𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛. Cette liste sera une chaîne de caractère
    pouvant correspondre à :
        - « Transformation identité »
        - « Symétrie par rapport à l'origine »
        - « Symétrie par rapport à une droite »
        - « Symétrie par rapport à un plan »
        - « Rotation par rapport à une droite »
        - « Anti-rotation par rapport à une droite »
        - « Pas une isométrie vectorielle »

    """
    if IsOrthogonal(mat):
        if mat == Matrice3x3():
            return "Transfomation identité"
        elif mat == Matrice3x3([-1, 0, 0], [0, -1, 0], [0, 0, -1]):
            return "Symétrie par rapport à l’origine"
        elif IsSymetric(mat):
            if roundfloat(mat.det()) == 1:
                return "Symétrie par rapport à une droite vectorielle "
            else:
                return "Symétrie par rapport à un plan vectoriel"
        else:
            if roundfloat(mat.det()) == 1:
                return "Rotation par rapport à une droite vectorielle"
            else:
                return "Anti-rotation par rapport à une droite vectorielle"
    else:
        return "Pas une isométrie vectorielle"


if __name__ == "__main__":
    # Exercice 1 ===================================================================
    print("============================Exercice 1=======================================")
    print()

    print(Exercice1(Matrice3x3([1, 0, 1], [1, 1, 0], [0, 1, 1]))) # pas une isométrie vectorielle

    print(Exercice1(Matrice3x3())) # Transfomation identité
    print(Exercice1(Matrice3x3([-1, 0, 0], [0, -1, 0], [0, 0, -1]))) # Symétrie par rapport à l’origine

    print(Exercice1(Matrice3x3([sqrt(2)/2, 0, sqrt(2)/2], [0,-1,0], [sqrt(2)/2, 0, -sqrt(2)/2]))) # Symétrie par rapport à une droite vectorielle
    print(Exercice1(Matrice3x3([sqrt(2)/2, 0, sqrt(2)/2], [0,1,0], [sqrt(2)/2, 0, -sqrt(2)/2]))) #symétrie sur plan vectoriel
    
    print(Exercice1(Matrice3x3([1, 0, 0], [0, cos(pi/4), sin(pi/4)], [0, -sin(pi/4), cos(pi/4)]))) # Rotation par rapport à une droite vectorielle
    print(Exercice1(Matrice3x3([-1, 0, 0], [0, cos(pi/4), sin(pi/4)], [0, -sin(pi/4), cos(pi/4)]))) # Anti-rotation par rapport à une droite vectorielle
    print()

    # Execrice 2 dans main2.py