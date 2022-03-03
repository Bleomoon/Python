def carre(ligne):
    new_liste = []
    i = 0
    x = 0
    print(len(ligne))
    while x < len(ligne):
        print(x)
        if ligne[x] >= '0' and ligne[x] <= '9':
            new_liste[i].join(ligne[x])
        else:
            i+=1
        x+=1
    return ':'.join(new_liste)
