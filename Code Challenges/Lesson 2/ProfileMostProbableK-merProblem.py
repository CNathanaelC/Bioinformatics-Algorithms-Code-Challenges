import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your profile_most_probable_kmer function here, along with any subroutines you need.

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.
    
    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    best_motif = ""
    best_motif_val = 0
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        prob = profile[0][pattern[0]]
        for j in range(1,len(pattern)):
            prob = prob * profile[j][pattern[j]]
        if i == 0 or prob > best_motif_val:
            best_motif_val = prob
            best_motif = pattern
    return best_motif