import sys 
import random

# Please do not remove package declarations because these are used by the autograder.

# Insert your gibbs_sampler function here, along with any subroutines you need

def profile_most_probable_kmer_with_rand(text: str, k: int, profile: list[dict[str, float]]) -> str:
    patterns = []
    probs = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        patterns.append(pattern)
        prob = profile[0][pattern[0]]
        for j in range(1,len(pattern)):
            prob = prob * profile[j][pattern[j]]
        probs.append(prob)
    rand_kmer = random.choices(patterns, weights=probs)[0]
    return rand_kmer

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
        if numAs == 0 or numCs == 0 or numGs == 0 or numTs == 0:
            numAs += 1
            numCs += 1
            numGs += 1
            numTs += 1
        profile[i]['A'] = numAs / len(text)
        profile[i]['C'] = numCs / len(text)
        profile[i]['G'] = numGs / len(text)
        profile[i]['T'] = numTs / len(text)
    return profile

def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """Implements the GibbsSampling algorithm for motif finding."""
    best_motifs = gibbs_helper(dna, k, t, n)
    for i in range(1000):
        motifs = gibbs_helper(dna, k, t, n)
        if score(motifs, k) < score(best_motifs, k):
            best_motifs = motifs
    return best_motifs
    
def gibbs_helper(dna: list[str], k: int, t: int, n: int):
    motifs = []
    best_motifs = []
    curr_profile = [{}]
    for i in range(k):
        curr_profile.append({'A':0, 'C':0, 'G':0, 'T':0})
    for i in range(len(dna)):
        rand_ind = random.randrange(len(dna[i])-k)
        motifs.append(dna[i][rand_ind:rand_ind+k])
    best_motifs = motifs
    for j in range(n):
        i = random.randrange(t)
        motifs_except = motifs[:i]
        motifs_except.extend(motifs[i+1:])
        curr_profile = profile(motifs, k, curr_profile)
        rand_ind = random.randrange(len(motifs))
        motifs[rand_ind] = profile_most_probable_kmer_with_rand(dna[rand_ind], k, curr_profile)
        if score(motifs, k) < score(best_motifs, k):
            best_motifs = motifs
    return best_motifs
# print(gibbs_sampler(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'], 8, 5, 100))