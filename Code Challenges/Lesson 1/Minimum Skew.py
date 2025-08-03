import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your MinimumSkew function here, along with any subroutines you need
def minimum_skew(genome: str) -> list[int]:
    """Find positions in a genome where the skew diagram attains a minimum."""
    skew = 0
    minimum_skew = 0
    return_list = list()
    for i in range(len(genome)):
        if genome[i] == 'C':
            skew -= 1
        elif genome[i] == 'G':
            skew += 1
        if skew < minimum_skew:
            minimum_skew = skew
            return_list.clear()
            return_list.append(i+1)
        elif skew == minimum_skew:
            return_list.append(i+1)
    return return_list