import sys
import copy
import smallparsimonyunrooted
from typing import List, Dict, Iterable, Tuple

def NearestNeighborInterchange(strings: List[str]):
    score = float('inf')
    #generate an arbitrary unrooted binary tree tree with |Strings| leaves

    #label the leaves of tree by arbitrary strings from Strings
    #solve  the  Small Parsimony in an Unrooted tree Problem for tree
    #label the internal nodes of tree according to a most parsimonious labeling
    n, tree, ef, eb, mn = smallparsimonyunrooted.read_in_input("input.txt")
    smallparsimonyunrooted.small_parsimony_unrooted(n, tree, ef, eb, mn)
    new_score = tree.score
    new_tree = tree
    while new_score < score:
        score = new_score
        tree = new_tree
        for i in range(n, len(mn[1]+1)):
            e = ef[i]
            en = edge_neighborhood(e, tree)
            for neighbor_tree in en:
                smallparsimonyunrooted.small_parsimony_unrooted(n, neighbor_tree, ef, eb, mn)
                neighbor_score = neighbor_tree.score
                if neighbor_score < new_score:
                    new_score = neighbor_score
                    new_tree = neighbor_tree
    return new_tree

def strings_to_tree(strings: List[str]):
    tree = smallparsimonyunrooted.node_tree(int(strings[0]))
    return tree
def edge_neighborhood(e, tree):
    return []