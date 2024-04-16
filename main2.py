from MathClass import *
from math import pi
import pygame as py
import time
py.init()
py.font.init()

"""
cos 0 -sin
0   1   0
sin 0  cos

N0 = 20, 0, 10
A0 = 20 - 2sqrt2,  2sqrt2,  10

points A , B, C, D par rapport a N0
-2sqrt2, 2qsrt2, 0 A0
-2sqrt2, -2qsrt2, 0 B0
2sqrt2, -2qsrt2, 0 C0
2sqrt2, 2qsrt2, 0 D0

angle rotation Roue : 
Alpha = pi/6 * t
angle rotation Nacelle : 
beta = pi/3 * t

N(t) = Rot(Alpha) * N0 + (10, 0, 10)

point en fonction du temps
A(t) = N(t) + Rot(beta)(-2sqrt2, 2sqrt2, 0)
B(t) = N(t) + Rot(beta)(-2sqrt2, -2sqrt2, 0)
C(t) = N(t) + Rot(beta)(2sqrt2, -2sqrt2, 0)
D(t) = N(t) + Rot(beta)(2sqrt2, 2sqrt2, 0)

"""
TITLE = py.font.SysFont("Arial", 30)
TXT = py.font.SysFont("Arial", 20)

N0 = VectorN(10, 0, 0)

A0 =  VectorN(-2 * sqrt(2), -2 * sqrt(2), 0)
B0 = VectorN(-2 * sqrt(2), 2 * sqrt(2), 0)
C0 = VectorN(2 * sqrt(2), 2 * sqrt(2), 0)
D0 = VectorN(2 * sqrt(2), -2 * sqrt(2), 0)

temps = 20
points = 1000
delta = temps / (points-1)
tetaR = [(delta * pi/6) * i for i in range(points)]
Nr = [multMatrixVec(N0, Matrice3x3([cos(tetaR[i]), 0, sin(tetaR[i])], [0, 1, 0], [-sin(tetaR[i]), 0, cos(tetaR[i])])) + VectorN(10, 0, 10) for i in range(points)]
#coordonnées de N0 sur origine
for elt in Nr:
    print(elt)
    


SCREEN = py.display.set_mode((1500, 500))

# 500 = 25 ? 
# X * 20

nacelle = py.Surface((80 * sqrt(2), 80 * sqrt(2)))
nacelle.fill((0, 255, 0))


t = 0
angle = 0
angle2 = 0
currentN = VectorN(20, 0, 10)
currentSurface = py.transform.rotate(nacelle, angle2)
running = True

tstart = time.time()
while running:

    SCREEN.fill(0)
    currentSurface = py.transform.rotozoom(nacelle, angle2 * 180 / pi, 1)

    currentN = multMatrixVec(N0, Matrice3x3([cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]))
    A = currentN + multMatrixVec(A0, Matrice3x3([cos(angle2), sin(angle2), 0], [-sin(angle2), cos(angle2), 0], [0, 0, 1])) + VectorN(10, 0, 10)
    B = currentN + multMatrixVec(B0, Matrice3x3([cos(angle2), sin(angle2), 0], [-sin(angle2), cos(angle2), 0], [0, 0, 1])) + VectorN(10, 0, 10)
    C = currentN + multMatrixVec(C0, Matrice3x3([cos(angle2), sin(angle2), 0], [-sin(angle2), cos(angle2), 0], [0, 0, 1])) + VectorN(10, 0, 10)
    D = currentN + multMatrixVec(D0, Matrice3x3([cos(angle2), sin(angle2), 0], [-sin(angle2), cos(angle2), 0], [0, 0, 1])) + VectorN(10, 0, 10)
    currentN += VectorN(10, 0, 10)

    # Séparation
    py.draw.line(SCREEN, (255, 255, 255), (500, 0), (500, 500)) 
    py.draw.line(SCREEN, (255, 255, 255), (1000, 0), (1000, 500))
    py.draw.line(SCREEN, (255, 255, 255), (1500, 0), (1500, 500))

    #===================================================================================================================
    # Vue Face
    SCREEN.blit(TITLE.render("Vue De Face", True, (255, 255, 255)), (100, 10))
    py.draw.circle(SCREEN,(255,255,255), (0, 500), 8)
    SCREEN.blit(TXT.render("O", True, (255, 255, 255)), (15, 475))

    #Axes
    py.draw.line(SCREEN, (255, 255, 255), (350, 150), (450, 150))
    SCREEN.blit(TXT.render("x", True, (255, 255, 255)), (450, 125))
    py.draw.line(SCREEN, (255, 255, 255), (350, 150), (350, 50))
    SCREEN.blit(TXT.render("z", True, (255, 255, 255)), (350, 25))
    # Cercle Roue
    py.draw.circle(SCREEN,(255,255,255), (200, 500 - 200), 200, 2)
    py.draw.circle(SCREEN,(255,255,255), (200, 500 - 200), 190, 2)
    # point R
    SCREEN.blit(TXT.render("R", True, (0, 0, 255)), (225, 500 - 225))
    py.draw.circle(SCREEN,(0,0,255), (200, 500 - 200), 10)
    #ligne haut
    py.draw.line(SCREEN, (0, 255, 0), (currentN.x() * 20 - 40 * sqrt(2), 500 - currentN.z() * 20), (currentN.x() * 20 + 40 * sqrt(2), 500 - currentN.z() * 20), 2)
    # Point N
    py.draw.circle(SCREEN, (255, 0, 0), (currentN.x() * 20, 500 - currentN.z() * 20), 5)
    
    #===================================================================================================================
    # Vue du dessus
    SCREEN.blit(TITLE.render("Vue Du Dessus", True, (255, 255, 255)), (650, 10))
    py.draw.circle(SCREEN,(255,255,255), (550, 250), 4)
    SCREEN.blit(TXT.render("O", True, (255, 255, 255)), (550, 250))
    
    py.draw.line(SCREEN, (255, 255, 255), (550, 200), (650, 200))
    SCREEN.blit(TXT.render("x", True, (255, 255, 255)), (650, 175))
    py.draw.line(SCREEN, (255, 255, 255), (550, 200), (550, 100))
    SCREEN.blit(TXT.render("y", True, (255, 255, 255)), (550, 75))
    # Cercle Roue
    py.draw.line(SCREEN, (255, 255, 255), (550, 500 - 250), (950, 500 - 250))
    # point R
    SCREEN.blit(TXT.render("R", True, (0, 0, 255)), (775, 500 - 275))
    py.draw.circle(SCREEN,(0,0,255), (750, 500 - 250), 10)
    #lignes nacelles
    py.draw.line(SCREEN, (0, 255, 0), (550 + A.x() * 20, 250 + A.y() * 20), (550 + B.x() * 20, 250 + B.y() * 20), 2)
    py.draw.line(SCREEN, (0, 255, 0), (550 + A.x() * 20, 250 + A.y() * 20), (550 + D.x() * 20, 250 + D.y() * 20), 2)
    py.draw.line(SCREEN, (0, 255, 0), (550 + B.x() * 20, 250 + B.y() * 20), (550 + C.x() * 20, 250 + C.y() * 20), 2)
    py.draw.line(SCREEN, (0, 255, 0), (550 + C.x() * 20, 250 + C.y() * 20), (550 + D.x() * 20, 250 + D.y() * 20), 2)
    
    SCREEN.blit(TXT.render("A", True, (255, 255, 0)), (550 + A.x() * 20 - 12, 250 + A.y() * 20 - 12))
    SCREEN.blit(TXT.render("B", True, (255, 255, 0)), (550 + B.x() * 20 - 12, 250 + B.y() * 20 - 12))
    SCREEN.blit(TXT.render("C", True, (255, 255, 0)), (550 + C.x() * 20 - 12, 250 + C.y() * 20 - 12))
    SCREEN.blit(TXT.render("D", True, (255, 255, 0)), (550 + D.x() * 20 - 12, 250 + D.y() * 20 - 12))
    # Point N
    py.draw.circle(SCREEN, (255, 0, 0), (550 + currentN.x() * 20, 500 - currentN.y() * 20 - 250), 5)

    #===================================================================================================================
    # Vue de coté
    SCREEN.blit(TITLE.render("Vue de coté", True, (255, 255, 255)), (1200, 10))
    py.draw.circle(SCREEN,(255,255,255), (1250, 450), 4)
    SCREEN.blit(TXT.render("O", True, (255, 255, 255)), (1250, 450))

    py.draw.line(SCREEN, (255, 255, 255), (1050, 200), (1150, 200))
    SCREEN.blit(TXT.render("y", True, (255, 255, 255)), (1150, 175))
    py.draw.line(SCREEN, (255, 255, 255), (1050, 200), (1050, 100))
    SCREEN.blit(TXT.render("z", True, (255, 255, 255)), (1050, 75))
    # Cercle Roue
    py.draw.line(SCREEN, (255, 255, 255), (1250, 50), (1250, 450) )
    # point R
    SCREEN.blit(TXT.render("R", True, (0, 0, 255)), (1275, 225))
    py.draw.circle(SCREEN,(0,0,255), (1250, 250), 10)
    #ligne haut
    py.draw.line(SCREEN, (0, 255, 0), (1250 + currentN.y() * 20 - 40 * sqrt(2), 450 - currentN.z() * 20), (1250 + currentN.y() * 20 + 40 * sqrt(2), 450 - currentN.z() * 20), 2)
    # Point N
    py.draw.circle(SCREEN, (255, 0, 0), (1250 + currentN.y() * 20, 450 - currentN.z() * 20), 5)

    t = time.time() - tstart
    angle = t * pi/6
    angle2 = -t * pi/3
    
    
    py.display.flip()
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            
