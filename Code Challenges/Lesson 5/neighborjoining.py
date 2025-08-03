import sys
from typing import List, Dict, Iterable, Tuple

class node:
    def __init__(self, index: int, connected = []):
        self.connected=connected
        self.connected.extend([index])
        self.index = index

def NeighborJoining(n: int, D: List[List[int]], merge_index = 0, node_ids = [], n_plus = 0):
    if len(node_ids) == 0:
        n_plus = n
        node_ids = [node(k) for k in range(0, n)]
    if n == 2:
        T = []
        T.append("{}->{}:{:.3f}".format(node_ids[1].index, node_ids[0].index, D[1][0]))
        T.append("{}->{}:{:.3f}".format(node_ids[0].index, node_ids[1].index, D[0][1]))
        return T
    D_alt =  alt_matrix(n, D)
    i, j = smallest_i_j(D_alt, n, node_ids)
    change = (total_distance(D[i]) - total_distance(D[j]))/(n - 2)
    limb_length_i = (D[i][j] + change) * (.5)
    limb_length_j = (D[i][j] - change) * (.5)
    D_new = [[D[k][m] for k in range(n) if k != i and k != j] for m in range(n) if m != i and m != j]
    print(D)
    print(D_new)
    new_leaf = [0]
    for k in range(1, n-2):
        new_leaf.append((1/2) * (D[k][i] + D[k][j] - D[i][j]))
    D_new.insert(0, new_leaf)
    for k in range(1, len(new_leaf)):
        D_new[k].insert(0, new_leaf[k])
    connected_ij = node_ids[i].connected
    connected_ij.extend(node_ids[j].connected)
    new_node_ids = [node_ids[k] for k in range(len(node_ids)) if k != i and k != j]
    new_node_ids.insert(0, node(n_plus, connected_ij))
    n_plus += 1
    merge_index += 1
    T = NeighborJoining(n-1, D_new, merge_index, new_node_ids, n_plus)
    T.append("{}->{}:{:.3f}".format(new_node_ids[0].index, node_ids[i].index, limb_length_i))
    T.append("{}->{}:{:.3f}".format(new_node_ids[0].index, node_ids[j].index, limb_length_j))
    T.append("{}->{}:{:.3f}".format(node_ids[i].index, new_node_ids[0].index, limb_length_i))
    T.append("{}->{}:{:.3f}".format(node_ids[j].index, new_node_ids[0].index, limb_length_j))
    return T
    
def alt_matrix(n: int, D: List[List[int]]):
    D_alt = []
    for i in range(len(D)):
        row = []
        for j in range(len(D[i])):
            if i == j:
                row.append(0)
            else:
                row.append((n-2)*D[i][j] - total_distance(D[i]) - total_distance(D[j]))
        D_alt.append(row)
    return D_alt
def smallest_i_j(D_alt: List[List[int]], n: int, node_ids: List[node]):
    small_i = 0
    small_j = 0
    small_val = float('inf')
    for i in range(len(D_alt)-1):
        j = i+1
        if D_alt[i][j] < small_val and i != j and ((node_ids[i].index+1 in node_ids[j].connected or node_ids[i].index-1 in node_ids[j].connected) or (node_ids[j].index+1 in node_ids[i].connected or node_ids[j].index-1 in node_ids[i].connected)):
            small_i = i
            small_j = j
            small_val = D_alt[i][j]
    return small_i, small_j


def total_distance(i_to_all: List[int]):
    return sum(i_to_all)

def read_file(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline())
        D = []
        for line in file:
            D.append(list(map(int, line.strip().split())))
    return n, D
# n, D = read_file("dataset_40204_6.txt")
# n, D = read_file("sample2.txt")
n, D = read_file("sample1.txt")
# n, D = read_file("extra.txt")
def sorted_key(branch: str):
    cleaved_branch = branch.split("->")
    return int(cleaved_branch[0] + cleaved_branch[1].split(":")[0])
def write_file(file_name, input_list):
    with open(file_name, 'w') as file:
        for item in input_list:
            file.write(item+"\n")
write_file("output.txt", sorted(NeighborJoining(n, D), key=sorted_key))
