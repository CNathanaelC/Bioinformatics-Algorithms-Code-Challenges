import sys
from typing import List, Dict, Tuple

# Please do not remove package declarations because these are used by the autograder.
def Score_Matrix(match_reward: int, mismatch_penalty: int, indel_penalty: int, v: str, w: str):
    scoring_matrix = [[0 for i in range(len(v))] for i in range(len(w))]
    for i in range(1,len(v)):
        scoring_matrix[0][i] = scoring_matrix[0][i-1] - indel_penalty
    for i in range(1,len(w)):
        scoring_matrix[i][0] = scoring_matrix[i-1][0] - indel_penalty
    for i in range(1, len(w)):
        for j in range(1, len(v)):
            if w[i] == v[j]:
                misMatch = scoring_matrix[i-1][j-1] + match_reward
            else:
                misMatch = scoring_matrix[i-1][j-1] - mismatch_penalty
            scoring_matrix[i][j] = max(scoring_matrix[i-1][j] - indel_penalty, scoring_matrix[i][j-1] - indel_penalty, misMatch)
    return scoring_matrix

# Insert your global_alignment function here, along with any subroutines you need
def global_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                     s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the global alignment of two strings based on given rewards and penalties.

    Args:
    match_reward (int): The reward for a match between two characters.
    mismatch_penalty (int): The penalty for a mismatch between two characters.
    indel_penalty (int): The penalty for an insertion or deletion.
    s (str): The first string.
    t (str): The second string.

    Returns:
    Tuple[int, str, str]: A tuple containing the alignment score and the aligned strings.
    """
    s = "-" + s
    t = "-" + t
    cost_matrix = Score_Matrix(match_reward, mismatch_penalty, indel_penalty, s, t)
    r = len(t)-1
    c = len(s)-1
    return backtrack(cost_matrix, "", "", r, c, s, t,match_reward,mismatch_penalty,indel_penalty)

def backtrack(cost_matrix: List[List[int]], sub_seq_s: str, sub_seq_t: str, r: int, c: int, s: str, t: str, match_reward: int, mismatch_penalty: int, indel_penalty: int):
    if r == 0 and c == 0:
        return cost_matrix[-1][-1], sub_seq_s, sub_seq_t
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
    return backtrack(cost_matrix, sub_seq_s, sub_seq_t, r, c, s, t,match_reward,mismatch_penalty,indel_penalty)