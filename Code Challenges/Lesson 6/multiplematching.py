import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your multiple_pattern_matching function here, along with any subroutines you need
def multiple_pattern_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in text where each string from patterns appears as a substring.
    """
    text += '$'
    return_dict = {}
    sa = suffix_array(text)
    sa.pop(0)
    s = ''
    for i in sa:
        s += text[i]
    sub_range_key = []
    sub_range = []
    counter = 0
    curr_char = text[sa[0]]
    for i, a in enumerate(sa):
        if text[a] != curr_char:
            sub_range_key.append(curr_char)
            curr_char = text[a]
            sub_range.append(counter)
        counter += 1
    sub_range.append(counter)
    sub_range_key.append(curr_char)
    for pattern in patterns:
        potentials = []
        for i, key in enumerate(sub_range_key):
            if pattern[0] == key:
                if i == 0:
                    potentials = sa[:sub_range[i]]
                elif i == len(sub_range)-1:
                    potentials = sa[sub_range[i]:]
                else:
                    potentials = sa[sub_range[i-1]:sub_range[i]]
        real = []
        for potential in potentials:
            if text[potential:potential+len(pattern)] == pattern:
                real.append(potential)
        return_dict[pattern] = sorted(real)
    return return_dict
        
def suffix_array(text: str) -> List[int]:
    suffixes = []
    for i in range(len(text)):
        suffixes.append((text[i:],i))
    sortedSuffixes = sorted(suffixes, key=lambda val:val[0])
    suffixArray = []
    for elm in sortedSuffixes:
        suffixArray.append(elm[1])
    return suffixArray
        
# print(multiple_pattern_matching('AATCGGGTTCAATCGGGGT', ['ATCG', 'GGGT']))
# print(multiple_pattern_matching('ATATATATAT', ['GT', 'AGCT', 'TAA', 'AAT', 'AATAT']))
# print(multiple_pattern_matching('bananas', ['ana', 'as']))