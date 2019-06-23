#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#

import numpy as np


def lcs(v, w):
    n = len(v)
    m = len(w)

    s = [[0 for j in range(m)] for i in range(n)]
    b = [['' for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if v[i] == w[j]:
                s[i][j] = s[i - 1][j - 1] + 1
            else:
                s[i][j] = max(s[i - 1][j], s[i][j - 1])

            if s[i][j] == s[i - 1][j]:
                b[i][j] = '\u2191'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = '\u2190'
            elif s[i][j] == s[i - 1][j - 1] + 1:
                b[i][j] = '\u2196'
    return s, b


def printLcs(b, v, i, j):
    pass


if __name__ == '__main__':
    v = 'TGCATA'
    w = 'ATCTGAT'

    print('Sequence v:')
    print(v)

    print()

    print('Sequence w:')
    print(w)

    print()

    s, b = lcs(v, w)
    print('Matrix s:')
    for row in s:
        print(row)

    print()

    print('Matrix b:')
    for row in b:
        print(row)
