import sys
import random
import copy
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your string_reconstruction function here, along with any subroutines you need
def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    dB = de_bruijn(patterns, k)
    path = eulerian(dB, k)
    return path

def eulerian_cycle(g: Dict[str, List[str]], k) -> Iterable[str]:
    """Constructs an Eulerian cycle in a graph."""
    path = []
    for key in list(g.keys()):
        for point in g[key]:
            path.append(str(key)+str(point)[-1])
    while not inorder(path, k):
        path = arrange(path, k)
        good_path, bad_path = list_separation(path, k)
        path = arrange(good_path, k) + arrange(bad_path, k)
    path_string = ""
    for i in range(len(path)-1):
        path_string += path[i][0]
    path_string += path[-1]
    return path_string
def eulerian(g: Dict[str, List[str]], k: int) -> Iterable[str]:
    """Constructs an Eulerian cycle in a graph."""
    path = []
    for key in list(g.keys()):
        for point in g[key]:
            path.append(str(key)+str(point)[-1])
    values = []
    start_points = []
    end_points = []
    for value in list(g.values()):
        values.extend(value)
    for key, val in g.items():
        #start and end have odd edges:
        start_points.extend([key+v[-1] for v in val if abs(values.count(key) - len(val)) == 1])
        end_points.extend([g[v][-1]+key for v in val if abs(values.count(key) - len(val)) == 1])
    while not inorder(path, k) or len(path) != len(values):
        start = start_points[random.randint(0, len(start_points)-1)]
        path = []
        values_size = len(values)
        path.append(start)
        graph = copy.deepcopy(g)
        graph[start[0:k-1]].remove(start[1:])
        values_size -= 1
        while values_size > 0:
            try:
                rand_ind = random.randint(0,len(graph[path[-1][1:]])-1)
                path.append(path[-1][1:] + graph[path[-1][1:]].pop(rand_ind)[-1])
                values_size -= 1
            except:
                values_size = 0
    path_string = ""
    for i in range(len(path)-1):
        path_string += path[i][0]
    path_string += path[-1]
    return path_string
    
def de_bruijn(path: List[str], k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""
    de_bruijn = {}
    path = arrange(path, k)
    for i in range(len(path)):
        if path[i][0:k-1] in de_bruijn:
            de_bruijn[path[i][0:k-1]].append(path[i][1:])
            de_bruijn[path[i][0:k-1]] = list((de_bruijn[path[i][0:k-1]]))
        else:
            de_bruijn[path[i][0:k-1]] = [path[i][1:]]
    return de_bruijn

def list_separation(path: List[str], k: int):
    dead_ind = random.randint(0,len(path)-1)
    path.insert(random.randint(0,len(path)-1), path.pop(random.randint(0,len(path)-1)))
    good_path = path[:dead_ind]
    bad_path = path[dead_ind:]
    return good_path, bad_path
def arrange(path: List[str], k: int):
    for i in range(1, len(path)-1):
        pattern = path[i]
        for j in range(1, len(path)-1):
            if j != i:
                if path[j][0:(k-1)] == pattern[1:]:
                    path.insert(j, path.pop(i))
    return path
def inorder(path: List[str], k: int):
    if len(path) == 0:
        return False
    for i in range(len(path)-1):
        if str(path[i][1:]) != str(path[i+1][0:(k-1)]):
            return False
    return True

print(string_reconstruction(['ACG', 'CGT', 'GTG', 'TGT', 'GTA', 'TAT', 'ATA'], int(3)))
print("vs.")
print("ACGTGTATA")
# print()
# print(string_reconstruction(['GG', 'AC', 'GA', 'CT'], int(2)))
# print("vs.")
# print('GGACT')
# print()
# print(string_reconstruction(['AAC', 'AAC', 'ACG', 'ACT', 'CGA', 'GAA'], int(3)))
# print("vs.")
# print('AACGAACT')
# print()
# print(string_reconstruction(['CTAC', 'CTCC', 'TCCT', 'ACTC', 'CCTC', 'CCTA', 'TACT'], int(4)))
# print("vs.")
# print('CCTACTCCTC')
# print()
# print(string_reconstruction(['CCC', 'CCC', 'CCC', 'TCC', 'CCC', 'CCG', 'CCC', 'CCC', 'CCC'], int(3)))
# print("vs.")
# print('TCCCCCCCCCG')
# print()
# print(string_reconstruction(['AG', 'AT', 'AA', 'GA', 'GG', 'GT', 'TA', 'TG', 'TT', 'AT'], int(2)))
# print("vs.")
# print('AAGTTGGATAT')
# print()
# print(string_reconstruction(['ACG', 'CGT', 'GTA', 'TAC'], int(3)))
# print("vs.")
# print('ACGTAC')