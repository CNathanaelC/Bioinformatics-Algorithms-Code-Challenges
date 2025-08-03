import math

def outcome_likelihood(txt_file: str):
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
    for state in pi_states:
        viterbi_graph[state] = [0.0 for x in range(len(x_pattern))]
        viterbi_graph[state][0] = float(1/len(pi_states)) * x_transitions[state+x_pattern[0]]
    
    for i in range(1, len(x_pattern)):
        for j, state in enumerate(pi_states):
            maxes = []
            for state2 in pi_states:
                maxes.append(viterbi_graph[state2][i-1] * pi_transitions[state2+state] * x_transitions[state+x_pattern[i]])
            viterbi_graph[state][i] = sum(maxes)
    print("A4:", viterbi_graph['A'][3])
    print("B4:", viterbi_graph['B'][3])
    print("A5:", viterbi_graph['A'][4])
    print("B5:", viterbi_graph['B'][4])
    print("Answer:", sum([x[-1] for x in viterbi_graph.values()]))

def try_float(maybe_float):
    try:
        float(maybe_float)
        return True
    except ValueError:
        return False

outcome_likelihood('i.txt')