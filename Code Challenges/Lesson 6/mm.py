import sys
import suffixarray
import copy
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your multiple_pattern_matching function here, along with any subroutines you need
def multiple_pattern_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in text where each string from patterns appears as a substring.
    """
    # text += "$"
    # text='panamabananas$'
    lc = ""
    fo = {}
    count = []
    sa = suffix_array(text)
    s = ''
    for i in sa:
        s += text[i]
    print(s)
    # count_it = {'$':0, 'a':0, 'b':0, 'm':0, 'n':0, 'p':0, 's':0}
    count_it = {'$':0, 'A':0, 'C':0, 'G':0, 'T':0}
    sub_range = []
    counter = 0
    for i, a in enumerate(sa):
        if i % 5 == 0:
            count.append(copy.deepcopy(count_it))
        count_it[text[a-1]] += 1
        counter += 1
        if text[a] not in fo:
            fo[text[a]] = i
        lc += text[a-1]
    if len(text) % 5 == 0:
        count.append(count_it)
    print(count_it)
    # print(better_bW_matching(text, fo, lc, 'ana', count))
    for pat in patterns:
        print(better_bW_matching(text, fo, lc, pat, count, sa))
def better_bW_matching(text: str, first_occurence: Dict[str, int], last_column: str, pat: str, counts:List[Dict[str, int]], suff_arr: List[int]):
    pattern = [i for i in pat]
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern.pop(-1)
            if symbol in text[top:bottom+1]:
                ##closer to lower
                if top % 5 < 2.5 or top//5+1 >= len(counts):
                    top = first_occurence[symbol] + counts[top//5][symbol]
                ##closer to higher
                else:
                    top = first_occurence[symbol] + counts[top//5+1][symbol]
                ##closer to lower
                if bottom % 5 < 2.5 or bottom//5+1 >= len(counts):
                    bottom = first_occurence[symbol] + counts[bottom//5][symbol] - 1
                ##closer to higher
                else:
                    bottom = first_occurence[symbol] + counts[bottom//5+1][symbol] - 1
            else:
                return 0
        else:
            return bottom - top + 1
        
def suffix_array(text: str) -> List[int]:
    suffixes = []
    for i in range(len(text)):
        suffixes.append((text[i:],i))
    sortedSuffixes = sorted(suffixes, key=lambda val:val[0])
    suffixArray = []
    for elm in sortedSuffixes:
        suffixArray.append(elm[1])
    return suffixArray
        
multiple_pattern_matching('AATCGGGTTCAATCGGGGT', ['ATCG', 'GGGT'])