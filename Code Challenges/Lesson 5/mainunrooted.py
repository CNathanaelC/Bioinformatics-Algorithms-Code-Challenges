import smallParsimony

class Main:




    def main(self):
        l = open('unrooted_input.txt', 'r').read().split('\n')
        with open('input.txt', 'w') as file:
            for i in range(0, len(l), 2):
                file.write(l[i])
                file.write('\n')

        f = open('input.txt','r')
        contents = f.read()
        char = ""
        n = ""
        i = 0
        while char != "\n":
            char = contents[i]
            n += char
            i += 1
        n = int(n[:-1])
        contents=contents[i:]
        element = ""
        numList = []
        returnList = []
        num = 0
        for elm in contents:
            if elm == "-":
                num = int(element)
                element = ""
            elif elm == ">":
                pass
            elif elm == "\n":
                if element[0] == "A" or element[0] == "T" or element[0] == "C" or element[0] == "G":
                    node = (num,element)
                else:
                    node = (num,int(element))
                returnList.append(node)
                element = ""
            else:
                element += elm
        if element != "":
            if element[0] == "A" or element[0] == "T" or element[0] == "C" or element[0] == "G":
                node = (num,element)
            else:
                node = (num,int(element))
            returnList.append(node)
        tree = {}
        stringLength = len(returnList[0][1])
        for elm in returnList:
            if elm[0] in tree:
                if tree[elm[0]]:
                    tree[elm[0]].append(elm[1])
                    tree[elm[0]].append({"A":0,"T":0,"C":0,"G":0})
                    tree[elm[0]].append("")
                    tree[elm[0]].append(0)
                else:
                    tree[elm[0]] = [elm[1]]
            else:
                tree[elm[0]] = [elm[1]]
        for i in range(stringLength):
            tree = smallParsimony.smallParsimony(tree,i)
            tree = smallParsimony.smallParsimonyBacktrack(tree,i)
            for elm in tree:
                tree[elm][2] = {"A":0,"T":0,"C":0,"G":0}
        finallist = []
        outputString = ""
        firstElm = list(tree.keys())[-1]
        outputString += str(tree[firstElm][4])
        outputString += "\n"
        for elm in tree:
            if type(tree[elm][0]) == str:
                outputString += tree[elm][3]
                outputString += "->"
                outputString += tree[elm][0]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3],tree[elm][0]))
                outputString += "\n"
                outputString += tree[elm][0]
                outputString += "->"
                outputString += tree[elm][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[elm][0]))
                outputString += "\n"
            if type(tree[elm][1]) == str:
                outputString += tree[elm][1]
                outputString += "->"
                outputString += tree[elm][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3],tree[elm][1]))
                outputString += "\n"
                outputString += tree[elm][3]
                outputString += "->"
                outputString += tree[elm][1]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[elm][1]))
                outputString += "\n"
            if type(tree[elm][0]) == int:
                outputString += tree[elm][3]
                outputString += "->"
                outputString += tree[tree[elm][0]][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[tree[elm][0]][3]))
                outputString += "\n"
                outputString += tree[tree[elm][0]][3]
                outputString += "->"
                outputString += tree[elm][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[tree[elm][0]][3]))
                outputString += "\n"
            if type(tree[elm][1]) == int:
                outputString += tree[elm][3]
                outputString += "->"
                outputString += tree[tree[elm][1]][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[tree[elm][1]][3]))
                outputString += "\n"
                outputString += tree[tree[elm][1]][3]
                outputString += "->"
                outputString += tree[elm][3]
                outputString += ":"
                outputString += str(hammingDistance(tree[elm][3], tree[tree[elm][1]][3]))
                outputString += "\n"
        print(outputString)









def hammingDistance(str1, str2):
    hamdist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamdist += 1
    return hamdist

if __name__ == '__main__':
    main_instance = Main()
    main_instance.main()