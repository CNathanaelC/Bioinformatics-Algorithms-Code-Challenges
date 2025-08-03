import sys
from typing import List, Dict, Iterable, Tuple, Set

# Please do not remove package declarations because these are used by the autograder.

# Insert your trie_construction function here, along with any subroutines you need
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
        self.tree = {}
        self.tree[0] = {0: node("", 0, 0)}
        self.len = len(max(patterns, key = lambda s : len(s)))
        self.n = 1
        self.node_to_char = {}
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
                        self.tree[curr_node[0]+1] = {}
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
    

    
def trie_construction(patterns: List[str]) -> List[Tuple[int, int, str]]:
    """
    Construct a trie from a collection of patterns.
    """
    new_trie = trie(patterns)
    trie_tuples = []
    for i in range(1, new_trie.len+1):
        for k, v in new_trie.tree[i].items():
            trie_tuples.append(tuple(str(v).split(" ")))
    return sorted(trie_tuples)
