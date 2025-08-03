import copy


def profile_hmm(txt_file: str, output_file = 'output.txt'):
    emission_rows = ['S', 'I0']
    with open(txt_file, 'r') as file:
        theta = float(file.readline())
        file.readline()
        alphabet = file.readline()[:-1].split('\t')
        file.readline()
        alignments = [x[:-1] if x[-1] == '\n' else x for x in file.readlines()]
        alignment_len = len(alignments[0])
    totals = [0 for x in range(alignment_len)]
    exclude = []
    imp_alignments = ["" for i in alignments]
    for i in range(alignment_len):
        count = 0
        for alignment in alignments:
            if alignment[i] == '-':
                totals[i] += 1
                count += 1
        if count/len(alignments) < theta:
            for j in range(len(alignments)):
                imp_alignments[j] += alignments[j][i]
        else:
            exclude.append(i)
    graph = structure(len(imp_alignments[0]), alphabet)
    for alignment in alignments:
        current = 'S'
        print_string_test = 'S-'
        for i in range(alignment_len):
            if i in exclude:
                if alignment[i] != '-':
                    current = graph.connected[current][0]
                    graph.emit[current][alignment[i]] += 1
                    graph.all_states[current] += 1
                    i+=1
                    print_string_test += current + '-'
            elif alignment[i] == '-' and i not in exclude:
                current = graph.connected[current][-1]
                graph.all_states[current] += 1
                i+=1
                print_string_test += current + '-'
            else:
                current = graph.connected[current][1]
                graph.emit[current][alignment[i]] += 1
                graph.all_states[current] += 1
                i+=1
                print_string_test += current + '-'
        if current != 'E':
            print_string_test += 'E'
        print_string_test = print_string_test.split('-')
        for j in range(len(print_string_test)-1):
            if (print_string_test[j]+"->"+print_string_test[j+1]) not in graph.transitions:
                graph.transitions[print_string_test[j]+"->"+print_string_test[j+1]] = 0
            graph.row_totals[print_string_test[j]] += 1
            graph.transitions[print_string_test[j]+"->"+print_string_test[j+1]] += 1
    with open(output_file, 'w') as file:
        line_write = ' \t'
        for k in graph.correct_order:
            line_write += k+'\t'
        file.write(line_write[:-1]+'\n')
        for k1 in graph.correct_order:
            line_write = k1+'\t'
            for k2 in graph.correct_order:
                if (k1+'->'+k2) in graph.transitions:
                    cell = graph.transitions[(k1+'->'+k2)]/graph.row_totals[k1]
                    if len(str(cell)) <= 4:
                        line_write += str(cell)+'\t'
                    else:
                        line_write += str(round(cell, 3))+'\t'
                else:
                    line_write += str(0)+'\t'
            file.write(line_write[:-1]+'\n')
        file.write('--------\n')
        line_write = ' \t'
        for a in alphabet:
            line_write += a+'\t'
        file.write(line_write[:-1]+'\n')
        for k,v in graph.emit.items():
            line_write = k+'\t'
            for x in list(v.values()):
                if graph.all_states[k] != 0 and x != 0:
                    if len(str((x/graph.all_states[k],3))) <= 4:
                        line_write+=str(x/graph.all_states[k])+'\t'
                    else:
                        line_write+=str(round(x/graph.all_states[k],3))+'\t'
                else:
                    line_write += str(0)+'\t'
            file.write(line_write[:-1]+'\n')
        
        


class structure:
    def __init__(self, column_num, alphabet):
        self.transitions = {}
        self.basic = {}
        for x in alphabet:
            self.basic[x] = 0
        self.all_states = {'S':1,'I0':0}
        self.correct_order=['S', 'I0', ]
        self.connected = {'S':['I0','M1','D1'],'I0':['I0','M1','D1']}
        self.emit = {'S':copy.deepcopy(self.basic), 'I0':copy.deepcopy(self.basic)}
        self.row_totals = {}
        for i in range(column_num):
            if 'M'+str(i+1) not in self.connected:
                self.connected['M'+str(i+1)] = []
            if 'D'+str(i+1) not in self.connected:
                self.connected['D'+str(i+1)] = []
            if 'I'+str(i+1) not in self.connected:
                self.connected['I'+str(i+1)] = []
            if 'M'+str(i+1) not in self.emit:
                self.emit['M'+str(i+1)] = copy.deepcopy(self.basic)
            if 'D'+str(i+1) not in self.emit:
                self.emit['D'+str(i+1)] = copy.deepcopy(self.basic)
            if 'I'+str(i+1) not in self.emit:
                self.emit['I'+str(i+1)] = copy.deepcopy(self.basic)
            self.correct_order.append('M'+str(i+1))
            self.correct_order.append('D'+str(i+1))
            self.correct_order.append('I'+str(i+1))
            self.all_states['I'+str(i+1)]=0
            self.all_states['M'+str(i+1)]=0
            self.all_states['D'+str(i+1)]=0
            if i+1 == column_num:
                self.connected['I'+str(i+1)] = ['I'+str(i+1), 'E']
                self.connected['M'+str(i+1)] = ['I'+str(i+1), 'E', 'D'+str(i+1)]
                self.connected['D'+str(i+1)] = ['I'+str(i+1), 'E']
            else:
                self.connected['I'+str(i+1)].append('I'+str(i+1))
                self.connected['I'+str(i+1)].append('M'+str(i+2))
                self.connected['I'+str(i+1)].append('D'+str(i+2))
                self.connected['M'+str(i+1)].append('I'+str(i+1))
                self.connected['M'+str(i+1)].append('M'+str(i+2))
                self.connected['M'+str(i+1)].append('D'+str(i+2))
                self.connected['D'+str(i+1)].append('I'+str(i+1))
                self.connected['D'+str(i+1)].append('M'+str(i+2))
                self.connected['D'+str(i+1)].append('D'+str(i+2))
        self.emit['E'] = copy.deepcopy(self.basic)
        self.all_states['E'] = 1
        self.correct_order.append('E')
        for co in self.correct_order:
            self.row_totals[co] = 0
    def __str__(self):
        return self.all_states.__str__() + '\n' + self.emit.__str__()
profile_hmm('input.txt')