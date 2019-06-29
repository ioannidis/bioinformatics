#============ CS UNIPI =============#
#       BioInformatics 2018-19      #
#===================================#
#   P16036 - Ioannidis Panagiotis   #
#   P16112 - Paravantis Athanasios  #
#===================================#

import numpy as np
import copy

# Transition matrix
# [[p(START|D1), p(D1|D1) , p(D2|D1) , p(END|D1) ],
#  [p(START|D2), p(D1|D2) , p(D2|D2) , p(END|D2) ],
#  [p(START|D3), p(D1|D2) , p(D2|D2) , p(END|D2) ],
#  [p(START|END), p(D1|END), p(D2|END), p(END|END)]]
transition_matrix = [[0.00, 0.50, 0.50, 0.00],
                     [0.00, 0.50, 0.25, 0.25],
                     [0.00, 0.25, 0.50, 0.25],
                     [0.00, 0.00, 0.00, 0.00]]


# Emission matrix
# [[p(1|START), p(1|D1), p(1|D2), p(1|END)],
#  [p(2|START), p(2|D1), p(2|D2), p(2|END)],
#  [p(3|START), p(3|D1), p(3|D2), p(3|END)]]
emission_matrix = [[0.00, 0.50, 0.25, 0.00],
                   [0.00, 0.25, 0.50, 0.00],
                   [0.00, 0.25, 0.25, 0.00]]

states = ['D1', 'D2']
states_len = len(states)

observation = '112122'
observation_len = len(observation)

viterbi_matrix = np.zeros((states_len, observation_len), dtype=int)
backtracking_matrix = np.zeros((states_len, observation_len), dtype=int)

# Viterbi algorithm
for i in range(states_len):
    viterbi_matrix[i][0] = np.log2(emission_matrix[int(observation[0]) - 1][i + 1]) + np.log2(transition_matrix[0][i + 1])
    
counter = 1
for i in observation[1:]:

    for j in range(states_len):

        max_node_score = [viterbi_matrix[0][counter - 1] + np.log2(transition_matrix[1][j + 1]), viterbi_matrix[1][counter - 1] + np.log2(transition_matrix[2][j + 1])]

        if max_node_score[0] > max_node_score[1]:
            viterbi_matrix[j][counter] = np.log2(emission_matrix[int(i) - 1][j + 1]) + max_node_score[0]
        elif max_node_score[0] < max_node_score[1]:
            viterbi_matrix[j][counter] = np.log2(emission_matrix[int(i) - 1][j + 1]) + max_node_score[1]
            backtracking_matrix[j][counter] = 1
        else:
            viterbi_matrix[j][counter] = np.log2(emission_matrix[int(i) - 1][j + 1]) + max_node_score[0]
            backtracking_matrix[j][counter] = 2

    counter += 1

# Viterbi backtracking
best_sequences = [[]]
if viterbi_matrix[0][states_len] > viterbi_matrix[1][states_len]:
    best_index = [0]
    best_sequences[0].append(states[0])
else:
    best_index = [1]
    best_sequences[0].append(states[1])

for i in range(backtracking_matrix.shape[1] - 1, 0, -1):
    for j in range(len(best_sequences)):
        if backtracking_matrix[best_index[j], i] != 2:
            best_sequences[j].append(states[backtracking_matrix[best_index[j]][i]])
            best_index[j] = backtracking_matrix[best_index[j]][i]
        else:
            best_sequences.append(copy.deepcopy(best_sequences[j]))
            best_index.append(best_index[j])

            best_sequences[j].append(states[0])
            best_sequences[j+1].append(states[1])

            best_index[j] = backtracking_matrix[0][i - 1]
            best_index[j+1] = backtracking_matrix[1][i - 1]

# Print viterbi matrix
print('The viterbi matrix is:')
print(viterbi_matrix)

# Print best sequences
print('\nThe best sequences are:')
for seq in np.flip(best_sequences, axis=1):
    print('START-', '-'.join(str(x) for x in seq), '-END')


# Print best score
best_index = 0 if viterbi_matrix[0][states_len] > viterbi_matrix[1][states_len] else 1
print('\nThe best score is:', str(viterbi_matrix[best_index][counter - 1] + np.log2(transition_matrix[best_index + 1][3])))


