import numpy as np
import math

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

observation = 'GGCT'

transition_matrix_log = np.log(transition_matrix)
print(transition_matrix_log)

emission_matrix_log = np.log(emission_matrix)
print(emission_matrix_log)

start_prob_log = np.log(start_prob)
print(start_prob_log)

# Holds the max score of each step
v_max_score_matrix = []

# Holds the best path
v_best_path_matrix = []


# v11 = start_prob_log[0] + emission_matrix_log[emissions.index('G')][0]
# v12 = start_prob_log[1] + emission_matrix_log[emissions.index('G')][1]

# v_max_score_matrix.append(max(v11, v12))
# v_best_path_matrix.append(1)
#
# a= [v11, v12]
#
# print(42342342342)
# print(a)
# print(a.index(max(a)))


# print("v_max_score_matrix")
# print(v_max_score_matrix)
# print("v_best_path_matrix")
# print(v_best_path_matrix)

for i in range(len(observation)):
    temp_scores = []
    if (i == 0):
        temp_scores.append(start_prob_log[0] + emission_matrix_log[emissions.index(observation[i])][0])
        temp_scores.append(start_prob_log[1] + emission_matrix_log[emissions.index(observation[i])][1])
    else:
        if (v_best_path_matrix[i - 1] == 'a'):
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[states.index(v_best_path_matrix[i - 1])][0] +
                emission_matrix_log[emissions.index(observation[i])][0])
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[states.index(v_best_path_matrix[i - 1])][1] +
                emission_matrix_log[emissions.index(observation[i])][1])
        else :
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[1][states.index(v_best_path_matrix[i - 1])] +
                emission_matrix_log[emissions.index(observation[i])][0])
            temp_scores.append(
                v_max_score_matrix[i - 1] + transition_matrix_log[1][states.index(v_best_path_matrix[i - 1])] +
                emission_matrix_log[emissions.index(observation[i])][1])


    print("temp scores ====================================")
    print(temp_scores)
    v_max_score_matrix.append(max(temp_scores))
    v_best_path_matrix.append(states[temp_scores.index(max(temp_scores))])

print("v_max_score_matrix")
print(v_max_score_matrix)
print("v_best_path_matrix")
print(v_best_path_matrix)

print("The best path for the ", observation, " sequence is:")
print(v_best_path_matrix)

