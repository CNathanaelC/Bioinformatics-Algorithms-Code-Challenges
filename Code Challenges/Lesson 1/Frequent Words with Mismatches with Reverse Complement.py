import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words_mismatches_reverse_complements function here, along with any subroutines you need
def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freq_map = dict()
    freq_map2 = dict()
    n = len(text)
    text_real = []
    reverse_machine = {'A':'T','T':'A','G':'C','C':'G'}
    for i in range(n-k+1):
        pattern = text[i:i+k]
        text_real.append(pattern)
        neighborhood = list(neighbors(pattern, d))
        reverse = ""
        for base in pattern:
            reverse = reverse_machine[base] + reverse
        neighborhood.extend(list(neighbors(reverse, d)))
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freq_map:
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] = freq_map[neighbor] + 1
    m = max(freq_map.values())
    for key in list(freq_map.keys()):
        if freq_map[key] == m:
            patterns.append(key)
    return patterns

def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    neighborhood = [s]
    if d > 0:
        neighborhood.extend(list(neighborhelper(s)))
        for i in range(d-1):
            moveins = []
            for item in neighborhood:
                moveins.extend(neighborhelper(item))
            neighborhood.extend(moveins)
    return set(neighborhood)
def neighborhelper(s: str) -> list[str]:
    neighborhood = set()
    bases = {'A':['T','G','C'], 'T':['A','G','C'], 'G':['A','T','C'], 'C':['A','T','G']}
    for i in range(len(s)):
        symbol = s[i]
        for base in bases[s[i]]:
            neighbor = s[:i] + base + s[i+1:]
            neighborhood.add(neighbor)
    return neighborhood