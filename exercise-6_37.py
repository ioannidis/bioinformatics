# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#
import re


def restore(seq):
    seq = re.sub('A{2,5}', 'A', seq)
    seq = re.sub('C{2,10}', 'C', seq)
    seq = re.sub('G+', 'G', seq)
    seq = re.sub('T+', 'T', seq)

    return seq


if __name__ == '__main__':
    before = 'AAATAAAGGGGCCCCCTTTTTTTCC'
    after = restore(before)

    print(f'Befor: {before}')
    print(f'After: {after}')
