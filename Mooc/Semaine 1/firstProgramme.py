a = 10 * 10
b = 20 * 20
c = 30 * 30
print("a =", a, "et b =", b, c)
print(f"a = {a} et b = {b} et c = {c}")

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument(dest="entier", type=int,
help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier

def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux petites valeurs de n, on peut retourner n
    if n <= 1:
        return n
    # sinon on initialise f2 pour n-2 et f1 pour n-1
    f2, f1 = 0, 1
        
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
        print(i, f2, f1)
    # le résultat est dans f1
    return f1

# print(f"fibonacci({entier}) = {fibonacci(entier)}")

from turtle import *

def square(length):
    for side in range(4):
        forward(length)
        left(90)

def megaForm():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()