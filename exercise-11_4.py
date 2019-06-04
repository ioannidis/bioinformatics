import numpy as np
import math

# Starting probabilities
start_prob = [0.5, 0.5]

# Transition matrix
# [[p(a|a), p(b|a)],
#  [p(a|b), p(b|b)]]
transition_matrix = [[0.9, 0.1],
                     [0.1, 0.9]]

# Emission matrix
# [[p(A|a), p(A|b)],
#  [p(G|a), p(G|b)],
#  [p(T|a), p(T|b)],
#  [p(C|a), p(C|b)]]
emission_matrix = [[0.4, 0.20],
                   [0.4, 0.20],
                   [0.1, 0.30],
                   [0.1, 0.30]]

emissions = ['A', 'G', 'T', 'C']
states = ['a', 'b']

# Observation sequence
observation = 'GGCT'

# Transform probability matrices to log-scores
transition_matrix_log = np.log(transition_matrix)
emission_matrix_log = np.log(emission_matrix)
start_prob_log = np.log(start_prob)

# Holds the max score of each step
v_max_score_matrix = []

# Holds the best path
v_best_path_matrix = []


for i in range(len(observation)):
    # Holed the scores for each step
    temp_scores = []

    # Calculate the score at first step and then
    # use dynamic programming to calculate the other steps
    if (i == 0):
        temp_scores.append(start_prob_log[0] + emission_matrix_log[emissions.index(observation[i])][0])
        temp_scores.append(start_prob_log[1] + emission_matrix_log[emissions.index(observation[i])][1])
    else:
        if (v_best_path_matrix[i - 1] == 'a'):
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[states.index('a')][0] +
                emission_matrix_log[emissions.index(observation[i])][0])
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[states.index('a')][1] +
                emission_matrix_log[emissions.index(observation[i])][1])
        else :
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[1][states.index('b')] +
                emission_matrix_log[emissions.index(observation[i])][0])
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[1][states.index('b')] +
                emission_matrix_log[emissions.index(observation[i])][1])

    v_max_score_matrix.append(max(temp_scores))
    v_best_path_matrix.append(states[temp_scores.index(max(temp_scores))])

print("The best path for the sequence ", observation, " is:")
print(v_best_path_matrix)

