import sys
import copy
from typing import List, Dict, Iterable, Tuple
from collections import defaultdict 

class node:
    def __init__(self, alpha, prev_lvl, lvl):
        self.alpha = alpha
        self.prev_lvl = prev_lvl
        self.next_lvl = set()
        self.lvl = lvl
                
    def __str__(self):
        return f"{self.prev_lvl} {self.lvl} {self.alpha}"
    def __repr__(self):
        return self.__str__()

class trie:
    def __init__(self, patterns):
        self.tree = defaultdict()
        self.tree[0] = {0: node("", 0, 0)}
        self.len = len(max(patterns, key = lambda s : len(s)))
        self.n = 1
        self.node_to_char = defaultdict()
        self.suffix_array = []
        for pattern in patterns:
            curr_node = [0, 0]
            for i in range(len(pattern)):
                contains = False
                edge = -1
                for outward_edge in self.tree[curr_node[0]][curr_node[1]].next_lvl:
                    if pattern[i] == self.node_to_char[outward_edge]:
                        contains = True
                        edge = outward_edge
                        break
                if contains:
                    curr_node = [curr_node[0]+1, edge]
                else:
                    self.tree[curr_node[0]][curr_node[1]].next_lvl.add(self.n)
                    if curr_node[0]+1 not in self.tree:
                        self.tree[curr_node[0]+1] = defaultdict()
                    self.tree[curr_node[0]+1][self.n] = node(pattern[i], curr_node[1], self.n)
                    self.node_to_char[self.n] = pattern[i]
                    curr_node = [curr_node[0]+1, self.n]
                    self.n += 1
        
    def __str__(self):
        return_list = []
        for i in range(1, self.len+1):
            for k, v in self.tree[i].items():
                return_list.append(v)
        return_list = sorted(return_list, key = lambda v : v.prev_lvl * 90000000000 + v.lvl)
        return "\n".join([str(x) for x in return_list])
                
    def __repr__(self):
        return self.__str__()
    def dfs(self, i: int, curr_node: node, leaves: List[str]):
        if curr_node.alpha[-1] == "$":
            built_v = ""
            track_up = i
            while track_up != 0:
                built_v = curr_node.alpha+built_v
                track_up = track_up - 1
                while curr_node.prev_lvl not in self.tree[track_up]:
                    track_up = track_up - 1
                curr_node = self.tree[track_up][curr_node.prev_lvl]
            leaves.append(built_v)
            del built_v
        else:
            for node in sorted(curr_node.next_lvl):
                deep_i = i
                while node not in self.tree[deep_i]:
                    deep_i +=1
                self.dfs(deep_i, self.tree[deep_i][node], leaves)
    


# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_array function here, along with any subroutines you need
def input_str_to_patterns(input: str):
    patterns = []
    for i in range(len(input)):
        patterns.append(input[i:])
    return patterns

def suffix_array1(text: str) -> List[int]:
    patterns = input_str_to_patterns(text)
    """
    Generate the suffix array for the given text.
    """
    Trie = trie(sorted(patterns))
    #iterate through trie and combine nodes
    Trie.node_to_char.clear()
    for i in range(1, len(Trie.tree)):
        for k, v in Trie.tree[i].items():
            deeper_i = i
            while len(Trie.tree[i][v.lvl].next_lvl) == 1:
                next = list(Trie.tree[i][v.lvl].next_lvl)[0]
                Trie.tree[i][v.lvl].alpha += Trie.tree[deeper_i+1][next].alpha
                Trie.tree[i][v.lvl].next_lvl = Trie.tree[deeper_i+1][next].next_lvl
                for va in Trie.tree[deeper_i+1][next].next_lvl:
                    Trie.tree[deeper_i+2][va].prev_lvl = v.lvl
                Trie.tree[deeper_i+1].pop(next)
                deeper_i += 1
            Trie.node_to_char[v.alpha] = v.lvl
    for i in range(len(Trie.tree)):
        if len(Trie.tree[i]) == 0:
            Trie.tree.pop(i)
    suffix_array = []
    vs = []
    for k, v in Trie.tree[1].items():
        Trie.dfs(1, v, vs)
    for built_v in vs:
        for j in range(len(patterns)):
            if patterns[j] == built_v:
                suffix_array.append(j)
    return suffix_array