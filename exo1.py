import math

matrice = [[1,0,2],[0,0,0],[1,0,3]]
u = [1,2,1]
v = [2,1,1]

class function:
    def __init__(self):
        pass

    def scal(self,u,v):
        return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
    
    def norme(self, u):
        return math.sqrt((u[0]**2 + u[1]**2 + u[2]**2))

    def det(self, matrice):

        deltaOneOne = matrice[1][1]*matrice[2][2]-matrice[2][1]*matrice[1][2]
        deltaTwoOne = matrice[0][1]*matrice[2][2]-matrice[2][1]*matrice[0][2]
        deltaThreeOne = matrice[0][1]*matrice[1][2]-matrice[1][1]*matrice[0][2]
        
        return deltaOneOne+deltaTwoOne+deltaThreeOne
    
    #def transformationIdentite(self):

def checkTransfo():
    if function.det != 1 or function.det != -1:
        print("Pas isometrique")
    else:
        if matrice[0][0] == 1 and matrice[1][1] == 1 and matrice[2][2] == 1:
            print("Matrice identite")
        else:
            #pas fini car pas sur d'ou je vais'
            return 0


def main():
    print(function.scal(function,u,v))
    print(function.norme(function,u))
    print(function.det(function,matrice))

main()