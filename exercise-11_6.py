#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#

import numpy as np

# Dice selection probabilities
dice_selection_prob = [0.5, 0.5]

# Transition matrix
# [[p(D1|D1) , p(D2|D1) , p(END|D1) ],
#  [p(D1|D2) , p(D2|D2) , p(END|D2) ],
#  [p(D1|END), p(D2|END), p(END|END)]]
transition_matrix = [[0.50, 0.25, 0.25],
                     [0.25, 0.50, 0.25],
                     [0.00, 0.00, 0.00]]

# Transition matrix
# [[p(1|D1), p(1|D2), p(1|END)],
#  [p(2|D1), p(2|D2), p(2|END)],
#  [p(3|D1), p(3|D2), p(3|END)]]
emission_matrix = [[0.50, 0.25, 0.00],
                   [0.25, 0.50, 0.00],
                   [0.25, 0.25, 0.00]]

emissions = ['1', '2', '3']

states = ['D1', 'D2']

# Observation sequence
observation = '112122'

# Transform probability matrices to log-scores
with np.errstate(divide='ignore'):
    transition_matrix_log = np.log2(transition_matrix)
    transition_matrix_log[np.isneginf(transition_matrix_log)] = 0

    emission_matrix_log = np.log2(emission_matrix)
    emission_matrix_log[np.isneginf(emission_matrix_log)] = 0

    dice_selection_prob_log = np.log2(dice_selection_prob)


viterbi_array= np.zeros(shape=(len(states), len(observation)))

# Calculate the score at first step and then
# use dynamic programming to calculate the other steps
for i in range(len(observation)):

    if (i == 0):
        viterbi_array[0][i] = dice_selection_prob_log[0] + emission_matrix_log[emissions.index(observation[i])][0]
        viterbi_array[1][i] = dice_selection_prob_log[1] + emission_matrix_log[emissions.index(observation[i])][1]
    else:
        temp_scores = []
        for j in range(len(states)):
            prev_node_score = viterbi_array[j][i-1]

            temp_scores.append(prev_node_score + transition_matrix_log[states.index('D1')][j] + emission_matrix_log[emissions.index(observation[i])][j])
            temp_scores.append(prev_node_score + transition_matrix_log[states.index('D2')][j] + emission_matrix_log[emissions.index(observation[i])][j])

        viterbi_array[0][i] = max(temp_scores[0], temp_scores[2])
        viterbi_array[1][i] = max(temp_scores[1], temp_scores[3])

viterbi_array_len = viterbi_array.shape[1]
best_score = max(viterbi_array[0][viterbi_array_len - 1], viterbi_array[1][viterbi_array_len - 1])

print("The best score is:", best_score)


viterbi_array_reversed = np.flip(viterbi_array, axis=1)
observation_reversed = observation[::-1]
print(viterbi_array_reversed)
print(observation_reversed)

best_sequence = []
v_best_score_matrix = []
for i in range(len(observation_reversed)):

    if (i == 0):
        # viterbi_array[0][i] = dice_selection_prob_log[0] + emission_matrix_log[emissions.index(observation[i])][0]
        # viterbi_array[1][i] = dice_selection_prob_log[1] + emission_matrix_log[emissions.index(observation[i])][1]
        if (viterbi_array_reversed[0][i] == best_score - transition_matrix_log[2][0]):
            best_sequence.append('D1')
            v_best_score_matrix.append(best_score - transition_matrix_log[2][0])

        if (viterbi_array_reversed[1][i] == best_score - transition_matrix_log[2][1]):
            best_sequence.append('D2')
            v_best_score_matrix.append(best_score - transition_matrix_log[2][1])

        # print(viterbi_array_reversed[i][0])
        # print(viterbi_array_reversed[i][1])
        # print(best_score - transition_matrix_log[states.index('END')][0])
        # print(viterbi_array_reversed[i][0] == best_score - transition_matrix_log[states.index('END')][0])
        # print(best_score - transition_matrix_log[states.index('END')][1])
        # print(viterbi_array_reversed[i][1] == best_score - transition_matrix_log[states.index('END')][1])
    else:
        temp_scores = []
        # for j in range(len(states)):

        prev_best_score = v_best_score_matrix[i-1]



        j = states.index(best_sequence[i-1])

        a = prev_best_score - (transition_matrix_log[states.index('D1')][j] + emission_matrix_log[emissions.index(observation_reversed[i-1])][j])
        b = prev_best_score - (transition_matrix_log[states.index('D2')][j] + emission_matrix_log[emissions.index(observation_reversed[i-1])][j])

        if (viterbi_array_reversed[0][i] == a and viterbi_array_reversed[1][i] == b):
            best_sequence.append('D1')
            print("*****")
            v_best_score_matrix.append(a)

        elif (viterbi_array_reversed[0][i] == a):
            best_sequence.append('D1')
            v_best_score_matrix.append(a)

        elif (viterbi_array_reversed[1][i] == b):
            best_sequence.append('D2')
            v_best_score_matrix.append(b)



        print(a , b)
        # break


        print(best_sequence)
        print(v_best_score_matrix)

            # temp_scores.append(prev_node_score + transition_matrix_log[states.index('D1')][j] + emission_matrix_log[emissions.index(observation[i])][j])
            # temp_scores.append(prev_node_score + transition_matrix_log[states.index('D2')][j] + emission_matrix_log[emissions.index(observation[i])][j])
    #
    #     viterbi_array[0][i] = max(temp_scores[0], temp_scores[2])
    #     viterbi_array[1][i] = max(temp_scores[1], temp_scores[3])


# v_max_score_matrix = []
# j=5
# if viterbi_array[0][j] > viterbi_array[1][j]:
#     state = "D1"
#     v_max_score_matrix.append(viterbi_array[0][j])
# elif viterbi_array[0][j] < viterbi_array[1][j]:
#     state = "D2"
#     v_max_score_matrix.append(viterbi_array[1][j])
# else:
#     state = "*"
#     v_max_score_matrix.append(viterbi_array[1][j])

# for j in range(viterbi_array_reversed.shape[1]-1):
#     # print(v_max_score_matrix[j] - (transition_matrix_log[states.index('D2')][0] +  emission_matrix_log[emissions.index(observation[j])][0]))
#     if ( viterbi_array_reversed[0][j] == v_max_score_matrix[0] - (transition_matrix_log[1][0] +  emission_matrix_log[1][0]) ):
#         print("malakas")

# print(v_max_score_matrix[0] - (transition_matrix_log[1][0] +  emission_matrix_log[1][0]))

    # if viterbi_array[0][j] > viterbi_array[1][j]:
    #     for seq_index in range(len(best_sequences)):
    #         best_sequences[seq_index] = best_sequences[seq_index] + "D1"
    #
    # if viterbi_array[0][j] < viterbi_array[1][j]:
    #     for seq_index in range(len(best_sequences)):
    #         best_sequences[seq_index] = best_sequences[seq_index] + "D2"
    #
    # if viterbi_array[0][j] == viterbi_array[1][j]:
    #     for seq_index in range(len(best_sequences)):
    #         best_sequences[seq_index] = best_sequences[seq_index] + "*"

        # best_sequences.append(best_sequences[seq_index] + "D2")


# print("best_sequences_matrix: ")
# print(best_sequences)
# print(v_max_score_matrix)
# print(viterbi_array_reversed)
# print(observation_reversed)

#
# j = viterbi_array.shape[1] - 1
# if viterbi_array[0][j] > viterbi_array[1][j]:
#     state = "D1"
#     v_max_score_matrix.append(viterbi_array[0][j])
# elif viterbi_array[0][j] < viterbi_array[1][j]:
#     state = "D2"
#     v_max_score_matrix.append(viterbi_array[1][j])
# else:
#     state = "*"
#     v_max_score_matrix.append(viterbi_array[1][j])
#
# best_sequences_matrix[0].insert(0,state)





# print("The best path for the sequence is:", "-".join(best_sequence))

