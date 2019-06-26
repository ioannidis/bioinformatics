# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#
from data import Data


def universal_match(v, w):
    n = len(w) + 1
    m = len(v) + 1

    s = [[0 for j in range(m)] for i in range(n)]
    b = [[' ' for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            v_token = v[j - 1]
            w_token = w[i - 1]

            s[i][j] = max(
                s[i - 1][j] - 1,
                s[i][j - 1] - 1,
                s[i - 1][j - 1] + 1
            )

            if s[i][j] == s[i - 1][j]:
                b[i][j] = f'\u2191'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = f'\u2190'
            elif s[i][j] == s[i - 1][j - 1] + 1:
                b[i][j] = f'\u2196'
    return s, b


if __name__ == '__main__':
    data = Data()
    v = data.load_data('lysozyme.txt')[:20]
    w = 'ACGCC'

    s, b = universal_match(v, w)

    # Print s matrix

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

    # Print b matrix

    print('Matrix b:')
    for row in b:
        print(row)

    print()
