# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#

from Bio import Align
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

if __name__ == '__main__':
    seq = Seq('TTSAGESADPVTTTVENYGGETQIQRRQHTDVSFIMDRFVKVT'
              'PQNQINILDLMQVPSHTLVGGLLRASTYYFSDLEIAVKHEGDL'
              'TWVPNGAPEKALDNTTNPTAYHKAPLTRLALPYTAPHRVLATV'
              'YNGECRYSRNAVPNLRGDLQVLAQKVARTLPTSFNYGAIKATR'
              'VTELLYRMKRAETYCPRPLLAIHPTEARHKQKIVAPVKQTL', IUPAC.ambiguous_dna)

    print(seq)
    v = 'AGTACT'
    w = ['ATAGAC', 'CTGATA', 'ATGGCC', 'ACGGGT']

    print(f'Sequence v:')
    print(v)
    print()
    print(f'Sequences w:')
    print(w)
    print()

    print('Calculating combinations of w...')
    print()

    w_comb = []

    for i in range(len(w)):
        for j in range(len(w)):
            if i == j:
                continue
            seq = f'{w[i]}{w[j]}'
            w_comb.append(seq)

    print(f'Found {len(w_comb)} combinations of w: {w_comb}')
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

    print('Calculating scores of combinations...')
    print()

    w_seq_max = w_comb[0]
    score = aligner.score(v, w_seq_max)
    scores = []

    for seq in w_comb:
        new_score = aligner.score(v, seq)
        if new_score > score:
            w_seq_max = seq
            score = new_score
        scores.append(score)

    print(f'Calculated scores: {scores}')
    print()

    print('Best combination of w:')
    print(w_seq_max)
    print()
    print('Highest Score:')
    print(score)
    print()

    alignments = list(aligner.align(v, w_seq_max))

    print(f'Alignments based on {aligner.algorithm}:')

    for alignment in alignments:
        print(alignment)
