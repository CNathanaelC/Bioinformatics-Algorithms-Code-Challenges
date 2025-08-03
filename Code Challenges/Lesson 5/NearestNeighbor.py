import sys
import copy

def nearestNeighbor(tree: dict, innerNodes: tuple):
    returnTree1 = copy.deepcopy(tree)
    returnTree1[innerNodes[0]].remove(innerNodes[1])
    returnTree1[innerNodes[1]].remove(innerNodes[0])
    tempval1 = returnTree1[innerNodes[0]][-1]
    returnTree1[tempval1].remove(innerNodes[0])
    returnTree1[tempval1].append(innerNodes[1])
    returnTree1[innerNodes[0]].pop()
    tempval2 = returnTree1[innerNodes[1]][-1]
    returnTree1[tempval2].remove(innerNodes[1])
    returnTree1[tempval2].append(innerNodes[0])
    returnTree1[innerNodes[1]].pop()
    returnTree1[innerNodes[1]].append(tempval1)
    returnTree1[innerNodes[0]].append(tempval2)
    returnTree1[innerNodes[0]].append(innerNodes[1])
    returnTree1[innerNodes[1]].append(innerNodes[0])

    returnTree2 = copy.deepcopy(returnTree1)
    returnTree2[innerNodes[0]].remove(innerNodes[1])
    returnTree2[innerNodes[1]].remove(innerNodes[0])
    tempval1 = returnTree2[innerNodes[0]][-1]
    returnTree2[tempval1].remove(innerNodes[0])
    returnTree2[tempval1].append(innerNodes[1])
    returnTree2[innerNodes[0]].remove(tempval1)
    tempval2 = returnTree2[innerNodes[1]][0]
    returnTree2[tempval2].remove(innerNodes[1])
    returnTree2[tempval2].append(innerNodes[0])
    returnTree2[innerNodes[1]].remove(tempval2)
    returnTree2[innerNodes[1]].append(tempval1)
    returnTree2[innerNodes[0]].append(tempval2)
    returnTree2[innerNodes[0]].append(innerNodes[1])
    returnTree2[innerNodes[1]].append(innerNodes[0])

    return returnTree1, returnTree2

