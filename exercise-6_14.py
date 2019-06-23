#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#

import random
from data import Data

# First player plays using winning strategy
def first_player(pointer_pos_seq_A, pointer_pos_seq_B):
    move_selection = 0

    if (pointer_pos_seq_A - 2) % 3 == 1 and (pointer_pos_seq_A - 2 > pointer_pos_seq_B - 1):
        move_selection = 1
    elif (pointer_pos_seq_A - 1) % 3 == 1 and (pointer_pos_seq_A - 1 > pointer_pos_seq_B - 2):
        move_selection = 2

    if (pointer_pos_seq_B - 1) % 3 == 1 and (pointer_pos_seq_B - 1 > pointer_pos_seq_A - 2):
        move_selection = 1
    elif (pointer_pos_seq_B - 2) % 3 == 1 and (pointer_pos_seq_B - 2 > pointer_pos_seq_A - 1):
        move_selection = 2

    if pointer_pos_seq_A - 2 == pointer_pos_seq_B - 1:
        if pointer_pos_seq_A % 3 == 2:
            move_selection = 1
        else:
            move_selection = 0
    elif pointer_pos_seq_A - 1 == pointer_pos_seq_B - 2:
        if pointer_pos_seq_A % 3 == 2:
            move_selection = 2
        else:
            move_selection = 0

    # Return the move of the first player
    if move_selection == 1:
        return pointer_pos_seq_A - 2, pointer_pos_seq_B -1
    elif move_selection == 2:
        return pointer_pos_seq_A - 1, pointer_pos_seq_B - 2
    else:
        random_pick = random.uniform(0, 1)
        if random_pick > 0.5:
            return pointer_pos_seq_A - 2, pointer_pos_seq_B - 1
        else:
            return pointer_pos_seq_A - 1, pointer_pos_seq_B - 2


# Second player plays randomly
def second_player(pointer_pos_seq_A, pointer_pos_seq_B):
    random_pick = random.uniform(0, 1)
    if random_pick > 0.5:
        return pointer_pos_seq_A - 2, pointer_pos_seq_B - 1
    else:
        return pointer_pos_seq_A - 1, pointer_pos_seq_B - 2


# Load data from files
a_lact_sequence = Data.load_data('a_lactalbumin.txt')
lysozyme_sequence = Data.load_data('lysozyme.txt')

# Init the pointers for each sequence
pointer_pos_seq_A = len(a_lact_sequence) - 1
pointer_pos_seq_B = len(lysozyme_sequence) - 1


while True:
    if (pointer_pos_seq_A >= 2 and pointer_pos_seq_B >= 1) or (pointer_pos_seq_A >= 1 and pointer_pos_seq_B >= 2):
        # First player move
        p1_move = first_player(pointer_pos_seq_A, pointer_pos_seq_B)
        # Update pointer values
        pointer_pos_seq_A = p1_move[0]
        pointer_pos_seq_B = p1_move[1]
    else:
        print("Player 1 wins!")
        break

    if (pointer_pos_seq_A >= 2 and pointer_pos_seq_B >= 1) or (pointer_pos_seq_A >= 1 and pointer_pos_seq_B >= 2):
        # Second player move
        p2_move = second_player(pointer_pos_seq_A, pointer_pos_seq_B)
        # Update pointer values
        pointer_pos_seq_A = p2_move[0]
        pointer_pos_seq_B = p2_move[1]
    else:
        print("Player 2 wins!")
        break
