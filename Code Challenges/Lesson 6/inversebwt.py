import sys
from typing import List, Dict, Iterable, Tuple


# Please do not remove package declarations because these are used by the autograder.

# Insert your inverse_burrows_wheeler_transform function here, along with any subroutines you need
def inverse_burrows_wheeler_transform(transform: str) -> str:
    """
    Generate the inverse of the Burrows-Wheeler Transform.
    """
    first_pair = sorted([i for i in transform])
    l_transform = [i for i in transform]
    pairs = [first_pair[i]+l_transform[i] for i in range(len(transform))]
    COUNTS1 = {'$':1,'A':1,'C':1,'G':1,'T':1}
    COUNTS2 = {'$':1,'A':1,'C':1,'G':1,'T':1}
    counts1 = []
    counts2 = []
    for pair in pairs:
        counts1.append(COUNTS1[pair[0]])
        COUNTS1[pair[0]] += 1
        counts2.append(COUNTS2[pair[1]])
        COUNTS2[pair[1]] += 1
    curr_point = pairs[0][0]
    count = 1
    bwt = ""
    for i in range(len(transform)):
        for j in range(len(transform)):
            if curr_point == pairs[j][1]:
                if count == counts2[j]:
                    if len(bwt) >= len(transform):
                        return bwt[1:]+'$'
                    else:
                        bwt += pairs[j][1]
                        curr_point = pairs[j][0]
                        count = counts1[j]
                        j = len(transform)