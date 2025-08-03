def hidden_path_prob(txt_file: str):
    with open(txt_file, 'r') as file:
        pattern = file.readline()[:-1]
        file.readline()
        states = file.readline()[:-1].split(' ')
        file.readline()
        file.readline()
        transitions = {}
        for i in range(len(states)):
            current_line = [float(x) for x in file.readline().split('\t')[1:] if float(x)]
            for j in range(len(states)):
                transitions[states[i]+states[j]] = current_line[j]
    prob = 1/len(states)
    for i in range(len(pattern)-1):
        prob *= transitions[pattern[i]+pattern[i+1]]
    return prob

def try_float(maybe_float):
    try:
        float(maybe_float)
        return True
    except ValueError:
        return False

hidden_path_prob('input.txt')
