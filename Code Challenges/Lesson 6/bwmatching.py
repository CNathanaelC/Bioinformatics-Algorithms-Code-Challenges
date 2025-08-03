import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your bw_matching function here, along with any subroutines you need
def bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Perform Burrows-Wheeler Matching for a set of patterns against the Burrows-Wheeler Transform of a text.
    """
    prev = sorted([i for i in bwt])
    curr = [i for i in bwt]
    pairs = [prev[i]+curr[i] for i in range(len(bwt))]
    COUNTS1 = {'$':1,'A':1,'C':1,'G':1,'T':1}
    COUNTS2 = {'$':1,'A':1,'C':1,'G':1,'T':1}
    counts1 = []
    counts2 = []
    for pair in pairs:
        counts1.append(COUNTS1[pair[0]])
        COUNTS1[pair[0]] += 1
        counts2.append(COUNTS2[pair[1]])
        COUNTS2[pair[1]] += 1
    path = {}
    for i in range(len(bwt)):
        path[prev[i]+str(counts1[i])] = curr[i]+str(counts2[i])
    del pairs
    del COUNTS2
    del counts1
    del counts2
    counts = [0 for i in patterns]
    for i, pattern in enumerate(patterns):
        for j in range(1, COUNTS1[pattern[-1]]):
            curr_point = pattern[-1]+str(j)
            k = len(pattern)-1
            while k >= 0:
                if curr_point[0] == pattern[k] and curr_point in path:
                    curr_point = path[curr_point]
                    if k == 0:
                        counts[i] += 1
                    k -= 1
                else:
                    k = -1
    return counts