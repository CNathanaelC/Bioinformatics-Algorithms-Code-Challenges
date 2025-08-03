import sys
import copy
from typing import List, Dict, Iterable, Tuple



def suffix_array(text: str) -> List[int]:
    suffixes = []
    for i in range(len(text)):
        suffixes.append((text[i:],i))
    sortedSuffixes = sorted(suffixes, key=lambda val:val[0])
    suffixArray = []
    for elm in sortedSuffixes:
        suffixArray.append(elm[1])
    return suffixArray