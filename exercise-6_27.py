# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#
import time

from Bio import Align
from Bio.Seq import Seq

from data import Data


if __name__ == '__main__':
    data = Data()
    v = data.load_data('lysozyme.txt')[:50]
    w = data.load_data('a_lactalbumin.txt')[:50]

    seq1 = Seq(v)
    seq2 = Seq(w)

    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'

    alignments = aligner.align(seq1, seq2)

    for alignment in alignments:
        print(alignment)
        time.sleep(1)
