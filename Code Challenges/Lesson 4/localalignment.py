import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

sys.setrecursionlimit(10000) # Don't delete! This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.
    
# Please do not remove package declarations because these are used by the autograder.
def Score_Matrix(match_reward: int, mismatch_penalty: int, indel_penalty: int, v: str, w: str):
    scoring_matrix = [[0 for i in range(len(v))] for i in range(len(w))]
    for i in range(1, len(w)):
        for j in range(1, len(v)):
            if w[i] == v[j]:
                misMatch = scoring_matrix[i-1][j-1] + match_reward
            else:
                misMatch = scoring_matrix[i-1][j-1] - mismatch_penalty
            maxed_value = max(scoring_matrix[i-1][j] - indel_penalty, scoring_matrix[i][j-1] - indel_penalty, misMatch)
            if maxed_value < 0:
                maxed_value = 0
            scoring_matrix[i][j] = maxed_value
    return scoring_matrix


# Insert your local_alignment function here, along with any subroutines you need
def local_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the local alignment of two strings based on match reward, mismatch penalty, and indel penalty.
    """
    s = "-" + s
    t = "-" + t
    cost_matrix = Score_Matrix(match_reward, mismatch_penalty, indel_penalty, s, t)
    max_index = (0,0)
    for i in range(len(cost_matrix)):
        for j in range(len(cost_matrix[i])):
            if cost_matrix[i][j] >= cost_matrix[max_index[0]][max_index[1]]:
                max_index = (i, j)
    r = max_index[0]
    c = max_index[1]
    return backtrack(cost_matrix, "", "", r, c, s, t, match_reward, mismatch_penalty, indel_penalty, max_index)

        
        
def backtrack(cost_matrix: List[List[int]], sub_seq_s: str, sub_seq_t: str, r: int, c: int, s: str, t: str, match_reward: int, mismatch_penalty: int, indel_penalty: int, max_index: Tuple[int, int]):
    if cost_matrix[r][c] == 0:
        return cost_matrix[max_index[0]][max_index[1]], sub_seq_s, sub_seq_t
    up = float('-inf')
    left = float('-inf')
    diag = float('-inf')
    
    if s[c] == t[r]:
        modifier = match_reward
    else:
        modifier = -mismatch_penalty
    diag = cost_matrix[r-1][c-1] + modifier
    up = cost_matrix[r-1][c] - indel_penalty
    left = cost_matrix[r][c-1] - indel_penalty
  
    if cost_matrix[r][c] == diag:
         # print('d')
        sub_seq_s = s[c] + sub_seq_s
        sub_seq_t = t[r] + sub_seq_t
        r = r-1
        c = c-1
    elif cost_matrix[r][c] == up:
        # print('u')
        sub_seq_s = "-" + sub_seq_s
        sub_seq_t = t[r] + sub_seq_t
        r = r-1
    elif cost_matrix[r][c] == left:
        # print('l')
        sub_seq_s = s[c] + sub_seq_s
        sub_seq_t = "-" + sub_seq_t
        c = c-1
    return backtrack(cost_matrix, sub_seq_s, sub_seq_t, r, c, s, t,match_reward,mismatch_penalty,indel_penalty, max_index)