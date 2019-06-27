# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#

from Bio import Align

if __name__ == '__main__':
    v = 'ATCTGATAA'
    w = 'TGCATA'

    print(f'Sequence v:')
    print(v)
    print()
    print(f'Sequence w:')
    print(w)
    print()

    k = input('Enter value of k: ')
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

    alignments = aligner.align(v, w)

    score = aligner.score(v, w)

    if -score > k:
        print(f'Value of k={k} is greater than the value of additions/deletions={-score}')

    print(f'Alignments based on {aligner.algorithm}:')

    for alignment in alignments:
        print(alignment)
