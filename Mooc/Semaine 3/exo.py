def comptage(in_filename, out_filename):
    with open(in_filename, encoding='utf-8') as entree:
        with open(out_filename, "a", encoding='utf-8') as sortie:
            i = 0
            for line in entree:
                i += 1
                words = line.split(" ")
                sortie.write(f"{i}:{len(words)}:{len(line)}:{line}")

def surgery(liste):
    if len(liste) > 1:
        if len(liste) % 2 == 0:
            a = liste[0]
            liste[0] = liste[1]
            liste[1] = a
        else:
            a = liste[-1]
            liste[-1] = liste[-2]
            liste[-2] = a
    return liste


def graph_dict(filename):
    d = {}
    with open(filename, encoding='utf-8') as entree:
        for line in entree:
            line = line.rstrip()  
            tab = line.split(' ')
            if (tab[0] in d.keys()):
                data = d[tab[0]]
                data.append((tab[2], int(tab[1])))
                d[tab[0]] = (data)
            else:
                d[tab[0]] = [(tab[2], int(tab[1]))]
        return d

def index(extended):
    index = {}
    for bateau in extended:
        index[bateau[0]] = bateau
    return index

def merge(extended, abbreviated):
    abbreviated = {}
    for bateau in extended[0]:
        for bateaubis in extended[1]:
            if bateau[0][0] == bateaubis[0][0]:
                abbreviated[bateau[0][0]] = [bateau[0][4], bateau[0][5], (bateau[0][1], bateau[0][2], bateau[0][3]), (bateau[1][1], bateau[1][2], bateau[1][3])]
    return abbreviated

def read_set(filename):
    s = set()
    with open(filename, encoding='utf-8') as entree:
        for line in entree:
            line = line.strip(' ')
            line = line.rstrip()
            s.add(line)
    return s

def search_in_set(filename_reference, filename):
    s = set()
    with open(filename, encoding='utf-8') as mots:
        for line_mots in mots:
            isIn = False
            line_mots = line_mots.strip(' ')
            line_mots = line_mots.rstrip()
            with open(filename_reference, encoding='utf-8') as ref:
                for line_ref in ref:
                    line_ref = line_ref.strip(' ')
                    line_ref = line_ref.rstrip()
                    if line_mots == line_ref:
                        isIn = True
                if isIn == True:
                    s.add((line_mots, True))
                else:
                    s.add((line_mots, False))
    return s

def diff(extended, abbreviated):
    diff = (set(),set(),set())
    for bateau in extended:
        isIn = False
        for bateau_bis in abbreviated:
            if bateau[0] == bateau_bis[0]:
                isIn = True
        if isIn == True:
            diff[1].add(bateau[4])
            diff[2].add(bateau[0])
        else:
            diff[0].add(bateau[4])
    s = set()
    for bateau_bis in abbreviated:
        if bateau_bis[0] not in diff[2]:
            s.add(bateau_bis[0])
    diff[2].clear()
    diff[2].update(s)
    return diff

class Fifo:
    def __init__(self):
        self.s = []
    def incoming(self, value):
        self.s.append(value)
    def outgoing(self):
        if len(self.s) > 0:
            return self.s.pop(0)