# ============ CS UNIPI =============#
#       BioInformatics 2018-19      #
# ===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
# ===================================#

def restore(seq):
    seq = [char for char in seq]
    idx_removes = []

    prev = ''
    for idx, char in enumerate(seq):
        if len(prev) > 0 and char == prev:
            idx_removes.append(idx)
        prev = char

    result = []

    for idx, char in enumerate(seq):
        if idx in idx_removes:
            continue
        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    before = 'AAATAAAGGGGCCCCCTTTTTTTCC'
    after = restore(before)

    print(f'Befor: {before}')
    print(f'After: {after}')
