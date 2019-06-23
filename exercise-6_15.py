#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#

import random
from data import Data

# First player moves
def first_player():
    if pointer_pos % 3 == 0:
        return 1
    elif pointer_pos % 3 == 1:
        return 2
    else:
        random_pick = random.uniform(0, 1)
        return 1 if random_pick > 0.5 else 2

# First player moves
def second_player():
    random_pick = random.uniform(0, 1)
    return 1 if random_pick > 0.5 else 2

# Total moves counter
count_moves = 0

# Load data from file
lysozyme_sequence = Data.load_data('lysozyme.txt')

# Pointer position
pointer_pos = len(lysozyme_sequence) - 1


if not lysozyme_sequence:  # if there are no nucleotides
    print('Sequence is empty!')
else:
    while True:

        # If pointer_pos is less than zero, then the sequence is empty. So the second player wins!
        if pointer_pos < 0:
            print('### Second player wins! ###')
            break

        # First player makes a move
        move = first_player()

        # Increase moves counter by 1
        count_moves = count_moves + 1

        # Update pointer position
        pointer_pos = pointer_pos - move

        # If pointer_pos is less than zero, then the sequence is empty. So the first player wins!
        if pointer_pos < 0:
            print('=== First player wins! ===')
            break

        # Second player makes a move
        move = second_player()

        # Increase moves counter by 1
        count_moves = count_moves + 1

        # Update pointer position
        pointer_pos = pointer_pos - move

print("The total moves both players made are:", count_moves)