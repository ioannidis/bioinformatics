#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#


def lcs(v, w):
    n = len(w) + 1
    m = len(v) + 1

    s = [[0 for j in range(m)] for i in range(n)]
    b = [[' ' for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            v_token = v[j - 1]
            w_token = w[i - 1]

            if v_token == w_token:
                s[i][j] = s[i - 1][j - 1] + 1
            else:
                s[i][j] = max(s[i - 1][j], s[i][j - 1])

    for i in range(1, n):
        for j in range(1, m):
            if s[i][j] == s[i - 1][j]:
                b[i][j] = f'\u2191'
            elif s[i][j] == s[i][j - 1]:
                b[i][j] = f'\u2190'
            elif s[i][j] == s[i - 1][j - 1] + 1:
                b[i][j] = f'\u2196'
    return s, b


def getLCS(b, v, i, j, seq=[]):
    if i == 0 or j == 0:
        return

    if b[i][j] == '\u2196':
        getLCS(b, v, i - 1, j - 1, seq)
        seq.append(v[j - 1])
    elif b[i][j] == '\u2191':
        getLCS(b, v, i - 1, j, seq)
    else:
        getLCS(b, v, i, j - 1, seq)

    return seq


if __name__ == '__main__':
    v = 'GTAGGCTTAAGGTTA'
    w = 'TAGATA'

    # Print sequence v

    print('Sequence v:')
    print(v)

    print()

    # Print sequence w

    print('Sequence w:')
    print(w)

    print()

    # Print s matrix

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

    # Print b matrix

    print('Matrix b:')
    for row in b:
        print(row)

    print()

    # Print LCS result

    n = len(w)
    m = len(v)
    lcs = getLCS(b, v, n, m)
    token = ''.join(lcs)
    print(f'Result: {token}')

    # Print distance

    print()

    distance = n + m - (2 * s[-1][-1])
    print(f'Distance: {distance}')
