# ============ CS UNIPI =============#
#       BioInformatics 2018-19       #
# ===================================#
#   P16036 - Ioannidis Panagiotis    #
#   P16112 - Paravantis Athanasios   #
# ===================================#

import random
from Bio.Seq import Seq
from Bio import Align
from data import Data

if __name__ == '__main__':
    data = Data()
    v = data.load_data('lysozyme.txt')[:50]
    w = data.load_data('a_lactalbumin.txt')[:50]

    print(f'Sequence v - lysozime - {len(v)} chars:')
    print(v)
    print()
    print(f'Sequence w - lactalbumin alpha - {len(w)} chars:')
    print(w)
    print()

    seq1 = Seq(v)
    seq2 = Seq(w)

    print('Calculating subsequences...')
    print()

    v_seqs = [v[i:] for i in range(len(v) - 1, 0, -1)]
    w_seqs = [w[:j] for j in range(1, len(w), 1)]

    print(f'Found {len(v_seqs)} subsequences of v.')
    print(f'Found {len(w_seqs)} subsequences of w.')
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

    v_seq_max = v_seqs[0]
    w_seq_max = w_seqs[0]
    score = aligner.score(v_seq_max, w_seq_max)
    scores = []

    for v_seq in v_seqs:
        for w_seq in w_seqs:
            new_score = aligner.score(v_seq, w_seq)
            if new_score > score:
                v_seq_max = v_seq
                w_seq_max = w_seq
                score = new_score
            scores.append(score)

    print(f'Calculated {len(scores)} scores.')
    print()

    print('Best subsequence v:')
    print(v_seq_max)
    print()
    print('Best subsequence w:')
    print(w_seq_max)
    print()
    print('Highest Score:')
    print(score)
    print()

    alignments = list(aligner.align(v_seq_max, w_seq_max))
    alignment = random.choice(alignments)

    print(f'Alignment based on {aligner.algorithm}:')
    print(alignment)
