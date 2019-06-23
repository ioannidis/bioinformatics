# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#

import numpy as np


def lcs(v, w):
    n = len(v)
    m = len(w)

    s = [[0 for j in range(m)] for i in range(n)]
    b = [[' ' for j in range(m)] for i in range(n)]

    v_index = 0

    for i in range(1, n):
        w_index = 0
        for j in range(1, m):
            v_token = v[v_index]
            w_token = w[w_index]

            # print(f'{v[v_index]} ? {w[w_index]}')
            print(f'{i}, {j}')
            if v_token == w_token:
                s[i][j] = s[i - 1][j - 1] + 1
            else:
                s[i][j] = max(s[i - 1][j], s[i][j - 1])

            if s[i][j] == s[i - 1][j]:
                b[i][j] = '\u2191'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = '\u2190'
            elif s[i][j] == s[i - 1][j - 1] + 1:
                b[i][j] = '\u2196'

            w_index += 1
        print()
        v_index += 1
    return s, b


def printLcs(b, v, i, j):
    if i == 0 or j == 0:
        return

    if b[i][j] == '\u2196':
        printLcs(b, v, i - 1, j - 1)
        print(v[i])
    else:
        if b[i][j] == '\u2191':
            printLcs(b, v, i - 1, j)
        else:
            printLcs(b, v, i, j - 1)


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

    print('      ', end='')
    for char in v:
        print(char, end='  ')
    print()

    w_chars = [char for char in w]
    idx = -1
    for row in s:
        if idx > -1:
            print(w_chars[idx] + ' ', end='')
        else:
            print('  ', end='')
        print(row)
        idx += 1

    print()

    print('Matrix b:')
    for row in b:
        print(row)

    print()
    # print(printLcs(b, v, n, m))
