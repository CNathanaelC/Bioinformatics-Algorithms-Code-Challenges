import sys
import math
import copy
from typing import List, Dict, Iterable, Tuple

class node:
    def __init__(self, genome):
        #list of integers that refer to the nodes connected
        self.genome = genome
        self.acgt = {'A':float('inf'),'C':float('inf'),'G':float('inf'),'T':float('inf')}
    def __str__(self):
        return f"genome:{self.genome}|ACGT:{self.acgt}"
    def __repr__(self):
        return self.__str__()
    def reset_acgt(self, ACGT: int):
        self.acgt = {'A':float('inf'),'C':float('inf'),'G':float('inf'),'T':float('inf')}
        if ACGT != -1:
            self.acgt[self.genome[ACGT]] = 0  

class node_tree:
    def __init__(self, n: int):
        self.tree = {}
        self.root = 0
        self.next_node = 0
        self.score = 0
    def __str__(self):
        return f"tree: {self.tree}"
    def length(self):
        return len(self.tree)
    def graft(self,  node: node):
        node.acgt = {'A':float('inf'),'C':float('inf'),'G':float('inf'),'T':float('inf')}
        self.tree[self.next_node] = node
        self.next_node = self.next_node+1
    def backtrack(self, curr_node, edge_forward, edge_backward, max_node, ACGT):
        if curr_node not in edge_forward:
            self.tree[curr_node].genome += ACGT
            self.score += self.tree[curr_node].acgt[ACGT]
        if len(self.tree[edge_backward[curr_node][0]].genome) < len(self.tree[0].genome) and len(self.tree[edge_backward[curr_node][1]].genome) < len(self.tree[0].genome):
            for k in "ACGT":
                if k == ACGT:
                    score_addition = 0
                else:
                    score_addition = 1
                if tree.tree[curr_node].acgt[ACGT] == tree.tree[edge_backward[curr_node][0]].acgt[ACGT] + tree.tree[edge_backward[curr_node][1]].acgt[k] + score_addition:
                    min_s_k = [ACGT, k, score_addition]
                    self.tree[edge_backward[curr_node][0]].genome += min_s_k[0]
                    self.tree[edge_backward[curr_node][1]].genome += min_s_k[1]
                    self.backtrack(edge_backward[curr_node][0], edge_forward, edge_backward, max_node, min_s_k[0])
                    self.backtrack(edge_backward[curr_node][1], edge_forward, edge_backward, max_node, min_s_k[1])
                    return
                elif tree.tree[curr_node].acgt[ACGT] == tree.tree[edge_backward[curr_node][0]].acgt[k] + tree.tree[edge_backward[curr_node][1]].acgt[ACGT] + score_addition:
                    min_s_k = [k, ACGT, score_addition]
                    self.tree[edge_backward[curr_node][0]].genome += min_s_k[0]
                    self.tree[edge_backward[curr_node][1]].genome += min_s_k[1]
                    self.backtrack(edge_backward[curr_node][0], edge_forward, edge_backward, max_node, min_s_k[0])
                    self.backtrack(edge_backward[curr_node][1], edge_forward, edge_backward, max_node, min_s_k[1])
                    return
    


def read_in_input(input_file: str):
    file = open(input_file, 'r')
    file = file.readlines()
    n = int(file.pop(0))
    edge_forward = {}
    edge_backward = {}
    tree = node_tree(n)
    line = file.pop(0)[:-1].split("->")
    line2 = file.pop(0)[:-1].split("->")
    while str.isalpha(line[0]) and str.isnumeric(line[1]):
        edge_forward[tree.next_node] = int(line[1])
        if int(line[1]) in edge_backward:
            edge_backward[int(line[1])].append(tree.next_node)
        else:
            edge_backward[int(line[1])] = [tree.next_node]
        tree.graft(node(line[0]))
        line = file.pop(0)[:-1].split("->")
        line2 = file.pop(0).split("->")
    tree.tree[int(line[0])] = node("")
    tree.tree[int(line2[0])] = node("")
    lenfile = len(file)//2
    
    if lenfile == 0:
        max_nodes = [int(line[0]), int(line[1])]
        edge_forward[int(line[0])] = max_nodes[1]+1
        edge_forward[int(line[1])] = max_nodes[1]+1
        edge_backward[max_nodes[1]+1] = [int(line[0]), int(line[1])]
    else:
        edge_forward[int(line[0])] = int(line[1])
        if int(line[1]) in edge_backward:
            edge_forward[int(line[0])] = edge_forward(int(line[1]))
            edge_backward[int(line[1])].append(int(line[0]))
        else:
            edge_backward[int(line[1])] = [int(line[0])]
        for i in range(lenfile):
            line = file.pop(0)[:-1].split("->")
            line2 = file.pop(0).split("->")
            tree.tree[int(line[0])] = node("")
            tree.tree[int(line[1])] = node("")
            if i == lenfile-1:
                max_nodes = [int(line[0]), int(line[1])]
                edge_forward[int(line[0])] = max_nodes[1]+1
                edge_forward[int(line[1])] = max_nodes[1]+1
                edge_backward[max_nodes[1]+1] = [int(line[0]), int(line[1])]
            else:
                edge_forward[int(line[0])] = int(line[1])
                if int(line[1]) in edge_backward:
                    edge_backward[int(line[1])].append(int(line[0]))
                else:
                    edge_backward[int(line[1])] = [int(line[0])]
    tree.tree[max_nodes[1]+1] = node("")
    return n, tree, edge_forward, edge_backward, max_nodes

def tree_to_file(output_File: str, tree: node_tree, edge_foward: Dict[int, int], max_nodes: List[int]):
    output_list = []
    for x in range(max_nodes[1]+1):
        hamming_dist = 0
        if edge_forward[x] < max_nodes[1]+1:
            for i in range(len(tree.tree[x].genome)):
                if tree.tree[x].genome[i] != tree.tree[edge_forward[x]].genome[i]:
                    hamming_dist += 1
            output_list.append(f"{tree.tree[x].genome}->{tree.tree[edge_forward[x]].genome}:{hamming_dist}\n")
            output_list.append(f"{tree.tree[edge_forward[x]].genome}->{tree.tree[x].genome}:{hamming_dist}\n")
    hamming_dist = 0
    for i in range(len(tree.tree[max_nodes[0]].genome)):
        if tree.tree[max_nodes[0]].genome[i] != tree.tree[edge_forward[max_nodes[1]]].genome[i]:
            hamming_dist += 1
    output_list.append(f"{tree.tree[max_nodes[0]].genome}->{tree.tree[edge_forward[max_nodes[1]]].genome}:{hamming_dist}\n")
    output_list.append(f"{tree.tree[max_nodes[1]].genome}->{tree.tree[max_nodes[0]].genome}:{hamming_dist}\n")
    with open(output_File, 'w') as file:
        file.write(f"{tree.score}\n")
        for item in output_list:
            file.write(item)


def small_parsimony_unrooted(n: int, tree: node_tree, edge_forward: Dict[int, int], edge_backward:Dict[int, int], max_nodes: List[int]):
    genome_len = len(tree.tree[0].genome)
    for j in range(genome_len):
        for x in range(max_nodes[1]+2):
            if len(tree.tree[x].genome)-1 >= j:
                tree.tree[x].reset_acgt(j)
        for i in range(n, max_nodes[1]+2):
            #find min acgt of 0
            son = min(tree.tree[edge_backward[i][0]].acgt, key=tree.tree[edge_backward[i][0]].acgt.get)
            daughter = min(tree.tree[edge_backward[i][1]].acgt, key=tree.tree[edge_backward[i][1]].acgt.get)
            if edge_backward[i][0] < n:
                for k in "ACGT":
                    if k == son and k==daughter:
                        tree.tree[i].acgt[k] = 0
                    elif k == son or k == daughter:
                        tree.tree[i].acgt[k] = 1
                    else:
                        tree.tree[i].acgt[k] = 2
            else:
                for k in "ACGT":
                    tree.tree[i].acgt[k] = float('inf')
                for k in "ACGT":
                    for kk in "ACGT":
                        if k == kk:
                            score_addition = 0
                        else:
                            score_addition = 1
                        if tree.tree[i].acgt[kk] > tree.tree[edge_backward[i][0]].acgt[kk] + tree.tree[edge_backward[i][1]].acgt[k] + score_addition:
                            tree.tree[i].acgt[kk] = tree.tree[edge_backward[i][0]].acgt[kk] + tree.tree[edge_backward[i][1]].acgt[k] + score_addition
                        if tree.tree[i].acgt[k] > tree.tree[edge_backward[i][0]].acgt[k] + tree.tree[edge_backward[i][1]].acgt[kk] + score_addition:
                            tree.tree[i].acgt[k] = tree.tree[edge_backward[i][0]].acgt[k] + tree.tree[edge_backward[i][1]].acgt[kk] + score_addition
                        if tree.tree[i].acgt[k] > tree.tree[edge_backward[i][0]].acgt[kk] + tree.tree[edge_backward[i][1]].acgt[k] + score_addition:
                            tree.tree[i].acgt[k] = tree.tree[edge_backward[i][0]].acgt[kk] + tree.tree[edge_backward[i][1]].acgt[k] + score_addition
                        if tree.tree[i].acgt[kk] > tree.tree[edge_backward[i][0]].acgt[k] + tree.tree[edge_backward[i][1]].acgt[kk] + score_addition:
                            tree.tree[i].acgt[kk] = tree.tree[edge_backward[i][0]].acgt[k] + tree.tree[edge_backward[i][1]].acgt[kk] + score_addition
        tree.backtrack(max_nodes[1]+1, edge_forward, edge_backward, max_nodes[1]+1, min(tree.tree[max_nodes[1]+1].acgt, key=tree.tree[max_nodes[1]+1].acgt.get))

n, tree, edge_forward, edge_backward, max_nodes = read_in_input("un_input.txt")
small_parsimony_unrooted(n, tree, edge_forward, edge_backward, max_nodes)
tree_to_file("parsimonyoutput.txt", tree, edge_forward, max_nodes)