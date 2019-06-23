import numpy as np


def lcs(v, w):
    width = len(v)
    height = len(w)
    s = np.zeros((width, height))
    b = np.empty((width, height), dtype='U4')

    for i in range(width):
        for j in range(height):
            if v[i] == w[j]:
                s[i][j] = s[i - 1][j - 1] + 1
            else:
                s[i][j] = max(s[i - 1][j], s[i, j - 1])

            if s[i][j] == s[i - 1][j]:
                b[i][j] = '\2191'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = '\2190'
            elif s[i][j] == s[i - 1][j - 1]:
                b[i][j] = '\2196'
    return s, b


if __name__ == '__main__':
    v = 'TGCATA'
    w = 'ATCTGAT'

    print(v, w)

    s, b = lcs(v, w)
    print(s)
