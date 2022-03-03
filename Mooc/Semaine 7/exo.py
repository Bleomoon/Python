import numpy as np
def checkers(size, corner_0_0=True):
    x = 0
    a = np.arange(0, size*size, dtype=np.int8)
    while x in range(0, size*size):
        if corner_0_0 == True:
            a[x] = (x % 2)
        else:
            if x % 2:
                a[x] = 0
            else:
                a[x] = 1
        x += 1
    a.reshape(size, size)
    return a

import numpy as np
def hundreds(lines, columns, offset):
    M = np.arange(0 + offset,columns*10,10) + 100 * np.arange(lines)[:, np.newaxis]
    return M

def stairs(taille):
    taillebis = taille
    isBigger = False
    M2 = np.zeros(shape=(taille*2+1, taille*2+1))
    for i in range(1, taille*2+1):
        l1 = np.arange(0, taillebis+1)
        l2 = np.arange(taillebis-1, -1, -1)
        M = np.concatenate((l1, l2), axis=None)
        if M2.size > 0:
            M2 = np.concatenate((M2, M), axis=0)
        else:
            M2 = M
        if taillebis == (taille * 2):
            isBigger = True
        if isBigger == True:
            taillebis -= 1
        else:
            taillebis += 1
    return M

# à vous de jouer
def dice(target, nb_dice=2, nb_sides=6):
    M = np.arange(2 , nb_sides+2) + 1 * np.arange(nb_sides)[:, np.newaxis]
    return np.sum(M == target)