from itertools import combinations
def two_sum(data, target):
    result = []
    result = combinations(data, 2)
    for s in result:
        if s[0] != s[1]:
            if s[0] + s[1] == target:
                return (data.index(s[0]), data.index(s[1]))

# votre code
import string
def longest_gap(liste):
    longest = 0
    while liste:
        i = liste.pop(0)
        if i in liste:
            if longest < (liste.index(i) + 1):
                longest = liste.index(i) + 1
    return longest

def postfix_eval(chaine):
    if any(c.isalpha() for c in chaine):
        return 'error-unfinished'
    else:
        result = 0
