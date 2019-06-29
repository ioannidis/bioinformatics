# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#
import random

from Bio import Align

from data import Data

if __name__ == '__main__':
    data = Data()
    v = data.load_data('lysozyme.txt')[:50]
    w = data.load_data('a_lactalbumin.txt')[:random.randint(45, 50)]

    print(f'Sequence v - lysozime - {len(v)} chars:')
    print(v)
    print()
    print(f'Sequence w - lactalbumin alpha - {len(w)} chars:')
    print(w)
    print()

    k = input('Enter value of k: ')
    print()

    k = float(k)

    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'
    aligner.match = 0
    aligner.mismatch = 0
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

    score = abs(aligner.score(v, w))

    if score > k:
        print(f'Alignment stopped because k={k} < score={score}.')
    else:
        print(f'Aligning sequences since k={k} < score={score}.')
        print()
        print(f'Alignment based on {aligner.algorithm}:')

        alignments = list(aligner.align(v, w))
        alignment = random.choice(alignments)
        print(alignment)
