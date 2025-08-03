import math

def viterbi(txt_file: str):
    with open(txt_file, 'r') as file:
        x_pattern = file.readline()[:-1]
        file.readline()
        x_states = file.readline()[:-1].split(' ')
        file.readline()
        pi_states = file.readline()[:-1].split(' ')
        file.readline()
        file.readline()
        pi_transitions = {}
        for i in range(len(pi_states)):
            current_line = [float(x) for x in file.readline().split('\t')[1:] if try_float(x)]
            for j in range(len(pi_states)):
                pi_transitions[pi_states[i]+pi_states[j]] = current_line[j]
        file.readline()
        file.readline()
        x_transitions = {}
        for i in range(len(pi_states)):
            current_line = [float(x) for x in file.readline().split('\t')[1:] if try_float(x)]
            for j in range(len(x_states)):
                x_transitions[pi_states[i]+x_states[j]] = current_line[j]
    
    viterbi_graph = {}
    b_matrix = [['' for y in x_pattern] for x in pi_states]
    for state in pi_states:
        viterbi_graph[state] = [0.0 for x in range(len(x_pattern))]
        viterbi_graph[state][0] = float(1/len(pi_states)) * x_transitions[state+x_pattern[0]]
    
    for i in range(1, len(x_pattern)):
        for j, state in enumerate(pi_states):
            maxes = []
            for state2 in pi_states:
                maxes.append(viterbi_graph[state2][i-1] * pi_transitions[state2+state] * x_transitions[state+x_pattern[i]])
            mi, mv = super_max(maxes)
            viterbi_graph[state][i] = mv
            b_matrix[j][i-1] = pi_states[mi]
    for i in range(len(b_matrix)):
        b_matrix[i][-1] = pi_states[i]
    mi, mv = super_max([x[-1] for x in viterbi_graph.values()])
    pi_pattern = ''
    what_to_do_next = pi_states[mi]
    for i in range(len(viterbi_graph[pi_states[0]])-1, -1, -1):
        what_to_do_next = b_matrix[pi_states.index(what_to_do_next)][i]
        pi_pattern = what_to_do_next + pi_pattern
    print(pi_pattern)




def super_max(structure):
    i_nmind = 0
    for i in range(len(structure)):
        if structure[i_nmind] < structure[i]:
            i_nmind = i
    return i_nmind, structure[i_nmind]

def try_float(maybe_float):
    try:
        float(maybe_float)
        return True
    except ValueError:
        return False

viterbi('input.txt')