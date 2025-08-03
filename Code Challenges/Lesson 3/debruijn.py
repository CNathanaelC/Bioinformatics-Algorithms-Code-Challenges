import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_string function here, along with any subroutines you need
def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""
    arranged_pattern = ""
    de_bruijn = {}
    path = []
    for i in range(len(text)-k+1):
        path.append(text[i:i+k])
    for i in range(len(path)):
        pattern = path[i]
        for j in range(len(path)):
            if j != i:
                if path[j][:len(pattern)] == pattern[1:]:
                    path.pop(i)
                    path = path[:j]+[pattern]+path[j:]
    for i in range(len(path)):
        if i < len(path)-1:
            arranged_pattern += path[i][0]
        else:
            arranged_pattern += path[i]
    for i in range(len(arranged_pattern)-(k-1)):
        if arranged_pattern[i:i+k-1] in de_bruijn:
            de_bruijn[arranged_pattern[i:i+k-1]].append(arranged_pattern[i+1:i+k])
        else:
            de_bruijn[arranged_pattern[i:i+k-1]] = [arranged_pattern[i+1:i+k]]
    return de_bruijn
