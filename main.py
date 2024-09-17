x = 10
x = x + 2   # x+=2
x = x * 2   # x*=2

y = x % 2      # % je modulo a to je zvyšok po delení
z = x // 3     # // je delenie bezozvyšku

# trik
124 % 10 = 2    # posledna cifra
124 // 10 = 12  # prvé dve cifry

if x % 2 == 0:  # či je číslo párne
    x % 2 != 0: # != znamená nerovná sa, toto je pre nepárne alebo
    x % 2 == 1:

** je umocnenie


print(x)




2 hodina

from math import pi     # namiesto import math, celej knižnice, som naimportoval iba jednu vec, to pi
from math import acos
from math import degrees





def obsahKruhu(r):
    s = pi * r ** 2                             # a teraz ked nemam celu knižnicu ale len to pi tak nedávam math.pi, ale iba pi
    return s





def heron(a, b, c):
    s = (a + b + c) / 2
    S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return S
def heronzmazat():
    strana_a = float(input("Zadaj mi stranu A:"))
    strana_b = float(input("Zadaj mi stranu B:"))
    strana_c = float(input("Zadaj mi stranu C:"))

    print(heron(strana_a,strana_b,strana_c))



def uholAlpha(a, b, c):
    cosAplha = (-a ** 2 + b ** 2 + c ** 2) / (2 * b * c)
    alphaRadiany = acos(cosAplha)
    alphaStupne = degrees(alphaRadiany)
    return alphaStupne

def uholBeta(a, b, c):
    cosBeta = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    betaRadiany = acos(cosBeta)
    betaStupne = degrees(betaRadiany)
    return betaStupne

def uholGama(a, b, c):
    cosGama = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    gamaRadiany = acos(cosGama)
    gamaStupne = degrees(gamaRadiany)
    return gamaStupne

def uhly():
    a = float(input("Zadaj mi stranu A:"))
    b = float(input("Zadaj mi stranu B:"))
    c = float(input("Zadaj mi stranu C:"))

    print(uholAlpha(a, b, c))
    print(uholBeta(a, b, c))
    print(uholGama(a, b, c))





def polomerVpísana
