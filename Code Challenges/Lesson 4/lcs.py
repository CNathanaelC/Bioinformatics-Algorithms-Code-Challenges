import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

sys.setrecursionlimit(10000) # Don't delete! This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.
class cell:
    def __init__(self, cost: int, bridge=False):
        self.cost = cost
        self.bridge = bridge
    def __repr__(self):
        if self.bridge:
            return str(self.cost)+"\'"
        else:
            return str(self.cost)
    def __le__(self, other):
        return self.cost <= other.cost
    def __ge__(self, other):
        return self.cost >= other.cost

# Insert your longest_common_subsequence function here, along with any subroutines you need

def longest_common_subsequence(s: str, t: str) -> str:
    """
    Calculate the longest common subsequence of two strings.
    """
    cost_matrix = []
    s = "-" + s
    t = "-" + t
    #t = y-axis; s = x-axis
    for i in range(len(t)):
        row = []
        for j in range(len(s)):
            if i != 0 and j != 0:
                if t[i] == s[j]:
                    row.append(cell(cost_matrix[i-1][j-1].cost+1, True))
                elif cost_matrix[i-1][j] >= row[j-1]:
                    row.append(cell(cost_matrix[i-1][j].cost))
                elif cost_matrix[i-1][j] <= row[j-1]:
                    row.append(cell(row[j-1].cost))
            else:
                row.append(cell(0))
        cost_matrix.append(row)
    print(cost_matrix)
    r = len(t)-1
    c = len(s)-1
    return backtrack(cost_matrix, "", r, c, t)

def backtrack(cost_matrix: List[List[cell]], sub_seq: str, r: int, c: int, t: str):
    current_cell = cost_matrix[r][c]
    if len(sub_seq) == cost_matrix[-1][-1].cost:
        return sub_seq
    elif current_cell.bridge:
        sub_seq = t[r] + sub_seq
        if len(sub_seq) == cost_matrix[-1][-1].cost:
            return sub_seq
        else:
            r=r-1
            c=c-1
            return backtrack(cost_matrix, sub_seq, r, c, t)
    else:
        base_c = c
        while c != 0:
            if current_cell.cost == cost_matrix[r][c-1].cost:
                c = c-1
                current_cell = cost_matrix[r][c]
                if current_cell.bridge:
                    sub_seq = t[r] + sub_seq
                    if len(sub_seq) == cost_matrix[-1][-1].cost:
                        return sub_seq
                    else:
                        r=r-1
                        c=c-1
                        return backtrack(cost_matrix, sub_seq, r, c, t)
            else:
                c=0
        if r!= 0 and current_cell.cost == cost_matrix[r-1][base_c].cost:
            c = base_c
            r = r-1
            return backtrack(cost_matrix, sub_seq, r, c, t)

print(longest_common_subsequence("GACT","ATG"))