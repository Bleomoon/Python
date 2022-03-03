def label(prenom, note):
    if note < 10 and note >= 0:
        return (f"{prenom} est recalé")
    elif note >= 10 and note < 16:
        return (f"{prenom} est reçu")
    elif note >= 16 and note <= 20:
        return (f"félicitations à {prenom}")

composite = connue + inconnue + connue
connue = '0bf1'
composite = '0bf1a9730e150bf1'
inconnue = 'a9730e15'

def inconnue(composite, connue):
    return composite[len(connue):len(composite)-len(connue)]

def laccess(liste):
    if len(liste) != 0:
        if len(liste) % 2 == 0:
            return liste[len(liste)]
        else:
            x = len(liste)/2+1
            return liste[x]
    else:
        return None

def divisible(a, b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

def morceaux(x):
    if x >= 5:
        return (1/5*x - 1)
    elif x <= -5:
        return (-x -5)
    else:
        return 0

def wc(string):
    liste = [0,0,0]
    for c in string:
        liste[2] += 1
        if c == '\n':
            liste[0] += 1
        if c != '\t':
            if c == ' ':
                liste[1] += 1
            elif c == '\n' and string[liste[2]-1] != ' ' and string[liste[2]-1] != '\t':
                liste[1] += 1
            elif liste[2] == len(string) and string[liste[2]-1] != ' ' and string[liste[2]-1] != '\t':
                liste[1] += 1
    return liste

def P(x):
    return 2*x**2 -3*x -2

def liste_P(liste_x):
    return[P(liste_x[i]) for i in range(0, len(liste_x))]

def carre(ligne):
    new_liste = []
    i = 0
    x = 0
    while x < len(ligne):
        if ligne[x] >= '0' and ligne[x] <= '9':
            x2 = x
            while x2 < len(ligne) and  ligne[x2] >= '0' and ligne[x2] <= '9':
                x2 += 1
            new_liste += [ligne[x:x2]]
            x = x2
            i+=1
        x+=1
    liste = []
    for i in range(0, len(new_liste)):
        new_liste[i] = str(int(new_liste[i])**2)
    return ':'.join(new_liste)