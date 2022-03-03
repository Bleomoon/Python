def dispatch1(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return a**2 + b**2
        else:
            return a * (b - 1)
    else:
        if b % 2 == 0:
            return (a -1) * b
        else:
            return a**2 - b**2

def dispatch2(a, b, A, B):
    if a in A:
        if b in B:
            return a**2 + b**2
        else:
            return a * (b -1)
    else:
        if b in B:
            return (a - 1) * b
        else:
            return a**2 + b**2

# écrivez votre code ici
def libelle(ligne):
    ligne = ligne.rstrip()
    tab = ligne.split(',')
    print('oui +', len(tab))
    if len(tab) == 3:
        i = '0'
        for c in tab[2]:
            if c >= '1' and c <= '9':
                i = c
        if i == '1':
            return tab[1].strip() + '.' + tab[0].strip() + ' (' + i + 'er)'
        elif i == '0':
            return tab[1].strip() + '.' + tab[0].strip() + ' (-ème)'
        else:
            return tab[1].strip() + '.' + tab[0].strip() + ' (' + i + '-ème)'

def pgcd(a, b):
    if a > b:
        c = a
    else:
        c = b
    while c > 0:
        if a % c == 0 and b % c == 0:
            break
        c -= 1
    return c

def power(x, n):
    while n > 0:
        x *= x
        n -= 1
    return x

# ATTENTION vous devez aussi définir les arguments de la fonction
from math import *
def distance(*args):
    sum = 0
    for i in args:
        sum += i**2
    return sqrt(sum)

# vous devez définir votre propre signature
def numbers(*args):
    min = 0
    sum = 0
    max = 0
    for i in args:
        sum += i
        if min > i or min == 0:
            min = i
        if max < i:
            max = i
    l = (sum, min, max)
    return l