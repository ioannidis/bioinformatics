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
# [[p(a|a), p(b|a), p(c|a)],
#  [p(a|b), p(b|b), p(c|b)],
#  [p(a|c), p(b|c), p(c|c)]]
transition_matrix = [[0.50, 0.25, 0.25],
                     [0.25, 0.50, 0.25],
                     [0.00, 0.00, 0.00]]


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
    emission_matrix_log = np.log2(emission_matrix)
    dice_selection_prob_log = np.log2(dice_selection_prob)


viterbi_array= np.zeros(shape=(len(states), len(observation)))

# Calculate the score at first step and then
# use dynamic programming to calculate the other steps
for i in range(len(observation)):

    if (i == 0):
        viterbi_array[0][i] = dice_selection_prob_log[0] + emission_matrix_log[0][emissions.index(observation[i])]
        viterbi_array[1][i] = dice_selection_prob_log[1] + emission_matrix_log[1][emissions.index(observation[i])]
    else:
        temp_scores = []
        for j in range(len(states)):
            prev_node_score = viterbi_array[j][i-1]

            temp_scores.append(prev_node_score + transition_matrix_log[j][states.index('D1')] + emission_matrix_log[j][emissions.index(observation[i])])
            temp_scores.append(prev_node_score + transition_matrix_log[j][states.index('D2')] + emission_matrix_log[j][emissions.index(observation[i])])
            print("temp_scores ======================================================================")
            print(temp_scores)
            print(" ======================================================================")

        viterbi_array[0][i] = max(temp_scores[0], temp_scores[2])
        viterbi_array[1][i] = max(temp_scores[1], temp_scores[3])

print(np.flip(viterbi_array, axis=1))
best_sequences_matrix = []
best_sequence = ['end']
viterbi_array_reversed = np.flip(viterbi_array, axis=1)

for i in range(viterbi_array.shape[1]):
    if viterbi_array_reversed[0][i] > viterbi_array_reversed[1][i]:
        best_sequence.insert(0, "D1")
    elif viterbi_array_reversed[0][i] < viterbi_array_reversed[1][i]:
        best_sequence.insert(0, "D2")
    else:
        best_sequence.insert(0, "*")


best_sequence.insert(0, "start")

print(best_sequence)
print("The best path for the sequence is:", "-".join(best_sequence))

