import NearestNeighbor

class Main:




    def main(self):
        f = open('input.txt','r')
        contents = f.read()
        char = ""
        n = ""
        i = 0
        num1 = 0
        num2 = 0
        while char != "\n":
            char = contents[i]
            if(char == " "):
                num1 = int(n)
                n = ""
            n += char
            i += 1
        num2 = int(n[:-1])
        innerNodes = (num1,num2)
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
        for elm in returnList:
            if elm[0] in tree:
                if tree[elm[0]]:
                    tree[elm[0]].append(elm[1])
                else:
                    tree[elm[0]] = [elm[1]]
            else:
                tree[elm[0]] = [elm[1]]
        newTree1, newTree2 = NearestNeighbor.nearestNeighbor(tree,innerNodes)
        outputString = ""
        for elm in newTree1:
            for i in range(len(newTree1[elm])):
                outputString += str(elm)
                outputString += "->"
                outputString += str(newTree1[elm][i])
                outputString += "\n"
        outputString += "\n"
        for elm in newTree2:
            for i in range(len(newTree2[elm])):
                outputString += str(elm)
                outputString += "->"
                outputString += str(newTree2[elm][i])
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