import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your greedy_motif_search function here, along with any subroutines you need

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.
    
    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    best_motif = ""
    best_motif_val = 0
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        prob = profile[0][pattern[0]]
        for j in range(1,len(pattern)):
            prob = prob * profile[j][pattern[j]]
        if i == 0 or prob > best_motif_val:
            best_motif_val = prob
            best_motif = pattern
    return best_motif

def score(motifs: list[str], k: int) -> int:
    score = 0
    for i in range(k):
        occurs = {'A':0,'C':0,'G':0,'T':0}
        for j in range(len(motifs)):
            occurs[motifs[j][i]] = occurs[motifs[j][i]] + 1
            kmer = motifs[j]
        score += len(motifs) - max(occurs.values())
    return score
def profile(text: list[str], k: int, profile: list[dict[str, float]]) ->list[dict[str, float]]:
    for i in range(k):
        numAs = 0
        numCs = 0
        numGs = 0
        numTs = 0
        for j in range(len(text)):
            if text[j][i] == 'A':
                numAs += 1
            if text[j][i] == 'C':
                numCs += 1
            if text[j][i] == 'G':
                numGs += 1
            if text[j][i] == 'T':
                numTs += 1
        profile[i]['A'] = numAs / len(text)
        profile[i]['C'] = numCs / len(text)
        profile[i]['G'] = numGs / len(text)
        profile[i]['T'] = numTs / len(text)
    return profile

def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the GreedyMotifSearch algorithm."""
    best_motifs = []
    currProfile = [{}]
    for i in range(k):
        currProfile.append({'A':0, 'C':0, 'G':0, 'T':0})
    for i in range(len(dna)):
        best_motifs.append(dna[i][0:k])
    for i in range(len(dna[0])-k+1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            currProfile = profile(motifs, k, currProfile)
            best_motif = profile_most_probable_kmer(dna[j], k, currProfile)
            if j >= len(motifs):
                motifs.append(best_motif)
            else:
                motifs[j] = best_motif
        if score(motifs, k) < score(best_motifs, k):
            best_motifs = motifs
    return best_motifs


###No need to include this line or below, these were just the test cases provided

# print(greedy_motif_search(["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"], 3, 5))
# print(greedy_motif_search(["GCCCAA", "GGCCTG", "AACCTA", "TTCCTT"],3,4))
# print(greedy_motif_search(["GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC", "TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC", "TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT", "GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG", "GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT", "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT", "AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG", "AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA"],5,8))
# print(greedy_motif_search(["GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT", "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT", "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT", "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC", "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG"],6,5))
# print(greedy_motif_search(["GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA", "TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA", "GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA", "GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC", "AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA", "AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA", "GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA", "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT"],5,8))