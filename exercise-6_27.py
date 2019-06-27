# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#

from Bio import Align
from Bio.Seq import Seq
from data import Data


if __name__ == '__main__':
    data = Data()
    v = 'ATCTGAT'
    w = 'TGCATA'

    print(f'Sequence v:')
    print(v)
    print()
    print(f'Sequence w:')
    print(w)
    print()

    seq1 = Seq(v)
    seq2 = Seq(w)

    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'

    alignments = aligner.align(seq1, seq2)

    print(f'Alignments based on {aligner.algorithm}:')

    for alignment in alignments:
        print(alignment)
