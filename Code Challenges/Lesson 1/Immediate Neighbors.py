import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your neighbors function here, along with any subroutines you need
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