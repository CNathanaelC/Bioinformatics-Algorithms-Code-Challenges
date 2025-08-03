import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph."""
    path = [0]
    item = euler_helper(g, path, [])
    while type(item) == None:
        item = euler_helper(g, path, [])
    return item
def euler_helper(g: Dict[int, List[int]], path: List[int], visited: List[List[int]]) -> List[int]:
    if path[-1] != 0 or len(path) == 1:
        for point in g[path[-1]]:
            if [path[-1],point] not in visited:
                visited.append([path[-1],point])
                path.append(point)
                euler_helper(g, path, visited)
                visited.pop(-1)
                path.pop(-1)
    else:
        print(path)
        return path
print(eulerian_cycle({0: [3],
1: [0],
2: [1, 6],
3: [2],
4: [2],
5: [4],
6: [5, 8],
7: [9],
8: [7],
9: [6]}))