def multi_tri(listes):
    for sous_liste in listes:
        sous_liste.sort()
    return listes

def multi_tri_reverse(listes, reverses):
    for sous_liste in listes:
        sous_liste.sort(reverse=reverses[listes.index(sous_liste)])
    return listes


def name(personne, liste):
    for p in liste:
        if p['p'] == personne['p']:
            return personne['n']
            break

def tri_custom(liste):
    liste.sort(key=lambda personne: 'p2' in personne.keys())
    liste.sort(key=lambda personne: name(personne, liste))
    liste.sort(key=lambda personne: personne['p'])
    for personne in liste:
        for p in liste:
            if p['p'] == personne['p']:
                liste.sort(key=personne['n'])
    return liste

from _typeshed import OpenTextModeUpdating
from abc import abstractproperty
import operator
from math import *

def distance(*args):
    sum = 0
    for i in args:
        sum += i**2
    return sqrt(sum)

from functools import reduce
from operator import mul, add

def doubler_premier(*args):
    t = args[1:]
    l = list(t)
    l[0] *= 2 
    t = tuple(l)
    return reduce(args[0], t)

# ATTENTION vous devez aussi définir les arguments de la fonction
def doubler_premier_kwds(*args):
    t = args[1:]
    l = list(t)
    l[0] *= 2 
    t = tuple(l)
    return reduce(args[0], t)

# c'est à vous
def compare_all(f, g, entrees):
    l = []
    for i in entrees:
        if f(i) == g(i):
            l.append(True)
        else:
            l.append(False)
    return l

from functools import reduce
def compare_args(*args):
    t = args[2]
    l = []
    for i in t:
        if reduce(args[0], i) == reduce(args[1], i):
            l.append(True)
        else:
            l.append(False)
    return l

def aplatir(conteneurs):
    t = []
    for conteneur in conteneurs:
        for v in conteneur:
            t.append(v)
    return t

def alternat(c1, c2):
    t = []
    for i in range(len(c1)):
        t.append(c1[i])
        t.append(c2[i])
    return t

def intersect(A, B):
    d = set()
    for a1, a2 in A:
        for b1, b2 in B:
            if a1 == b1 :
                d.add(b2) 
                d.add(a2)  
    return d

mdc = ord(clear) % 26
        mdk = ord(key) % 26
        print(clear, ord(clear), mdc, key, ord(key), mdk)
        
import string
def cesar(clear, key, encode=True):
    if clear in string.ascii_letters and key in string.ascii_letters:
        if clear.islower():
            reduce = 96
            key = key.lower()
        else:
            reduce = 64
            key = key.upper()
        if encode == True:
            val = ( (ord(clear) - reduce) + (ord(key) - reduce) )
        else:
            val = ( (ord(clear) - reduce) - (ord(key) - reduce) ) - 1
            val += 27
        if val > 26:
            val  = val % 26
        return chr(val + reduce)
    else:
        return clear

# à vous de jouer
def vigenere(clear, key, encode=True):
    new_S = ""
    i = 0
    for j in range(len(clear)):
        if clear[j] in string.ascii_letters:
            new_S += cesar(clear[j], key[i], encode)
        else:
            new_S += clear[j]
        i += 1
        if i == len(key):
            i = 0
    return new_S

def produit_scalaire(X, Y):
    if len(X) == 2 and len(Y) == 2:
        somme = (X[i]*Y[i] for i in range(len(X)))
    return sum(somme)