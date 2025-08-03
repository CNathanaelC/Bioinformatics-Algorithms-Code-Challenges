def hidden_path_prob(txt_file: str):
    with open(txt_file, 'r') as file:
        x_pattern = file.readline()[:-1]
        file.readline()
        x_states = file.readline()[:-1].split(' ')
        file.readline()
        pi_pattern = file.readline()[:-1]
        file.readline()
        pi_states = file.readline()[:-1].split(' ')
        file.readline()
        file.readline()
        transitions = {}
        for i in range(len(pi_states)):
            current_line = [float(x) for x in file.readline().split('\t')[1:] if try_float(x)]
            for j in range(len(x_states)):
                transitions[pi_states[i]+x_states[j]] = current_line[j]
    prob = 1
    for i in range(len(x_pattern)):
        prob *= transitions[pi_pattern[i]+x_pattern[i]]
    return prob

def try_float(maybe_float):
    try:
        float(maybe_float)
        return True
    except ValueError:
        return False

hidden_path_prob('input.txt')