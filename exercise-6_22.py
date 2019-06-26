# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#
from Bio.Seq import Seq
from Bio import Align

from difflib import get_close_matches

from data import Data


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
    data = Data()
    v = data.load_data('lysozyme.txt')[:50]
    w = data.load_data('a_lactalbumin.txt')[:50]

    print(f'Sequence v:')
    print(v)
    print()
    print(f'Sequence w:')
    print(w)
    print()

    # Print sequence v
    #
    # print('Sequence v:')
    # print(v)
    #
    # print()
    #
    # # Print sequence w
    #
    # print('Sequence w:')
    # print(w)
    #
    # print()
    #
    # # Print s matrix
    #
    # s, b = lcs(v, w)
    # print('Matrix s:')
    #
    # print('      ', end='')
    # for char in v:
    #     print(char, end='  ')
    # print()
    #
    # w_chars = [char for char in w]
    # idx = -1
    # for row in s:
    #     if idx > -1:
    #         print(w_chars[idx] + ' ', end='')
    #     else:
    #         print('  ', end='')
    #     print(row)
    #     idx += 1
    #
    # print()
    #
    # # Print b matrix
    #
    # print('Matrix b:')
    # for row in b:
    #     print(row)
    #
    # print()
    #
    # # Print LCS result
    #
    # n = len(w)
    # m = len(v)
    # lcs = getLCS(b, v, n, m)
    # token = ''.join(lcs)
    # print(f'Result: {token}')

    seq1 = Seq(v)
    seq2 = Seq(w)

    print('Calculating subsequences...')
    print()

    window = len(v)
    sub_sequences = []

    while window > 0:
        results = [v[i:i + window] for i in range(len(v) - window - 1)]
        [sub_sequences.append(seq) for seq in results]
        window -= 1

    print(f'Found {len(sub_sequences)} subsequences of v.')
    print()

    aligner = Align.PairwiseAligner()

    aligner.mode = 'global'
    aligner.match = 1
    aligner.mismatch = -1
    aligner.query_left_open_gap_score = -1
    aligner.query_left_extend_gap_score = -1
    aligner.query_internal_open_gap_score = -1
    aligner.query_internal_extend_gap_score = -1
    aligner.query_right_open_gap_score = -1
    aligner.query_right_extend_gap_score = -1
    aligner.target_left_open_gap_score = -1
    aligner.target_left_extend_gap_score = -1
    aligner.target_internal_open_gap_score = -1
    aligner.target_internal_extend_gap_score = -1
    aligner.target_right_open_gap_score = -1
    aligner.target_right_extend_gap_score = -1

    print('Calculating scores of subsequences...')
    print()

    scores = [[seq, aligner.score(Seq(seq), seq2)] for seq in sub_sequences]
    max_seq = scores[-1][0]
    max_score = scores[-1][1]

    for pair in scores:
        if pair[1] > max_score:
            max_seq = pair[0]
            max_score = pair[1]

    print('Found best subsequence:')
    print(max_seq)
    print()

    max_seq = Seq(max_seq)

    alignments = list(aligner.align(max_seq, seq2))

    print(f'Alignment based on {aligner.algorithm}:')
    print(alignments[-1])

    print('Score:')
    print(aligner.score(max_seq, seq2))
