import sys
from collections import OrderedDict

#for each node, here is a key for the list:
#T[elm] is the node
#T[elm][0] is the daughter
#T[elm][1] is the son
#T[elm][2] is the scores dictionary
#T[elm][3] is the node's string
#T[elm][4] is the node's score

def smallParsimony(T: dict, character: int):
    tagged = []
    alphabet = "ACGT"

    #filling in the leaf nodes
    for elm in T:
        if type(T[elm][0]) == str:
            tagged.append(elm)
            for k in alphabet:
                if k != T[elm][0][character]:
                    T[elm][2][k] += 1
        if type(T[elm][1]) == str:
            tagged.append(elm)
            for k in alphabet:
                if k != T[elm][1][character]:
                    T[elm][2][k] += 1


    #filling in the inner nodes
    for elm in T:

        #son

        if type(T[elm][0]) == int:
            for letter in alphabet:
                finalScore = 0
                Ascore1 = T[T[elm][0]][2]["A"]
                if letter != "A":
                    Ascore1 += 1
                Tscore1 = T[T[elm][0]][2]["T"]
                if letter != "T":
                    Tscore1 += 1
                Cscore1 = T[T[elm][0]][2]["C"]
                if letter != "C":
                    Cscore1 += 1
                Gscore1 = T[T[elm][0]][2]["G"]
                if letter != "G":
                    Gscore1 += 1
                if Ascore1 <= Tscore1 and Ascore1 <= Cscore1 and Ascore1 <= Gscore1:
                    finalScore += Ascore1
                elif Tscore1 <= Ascore1 and Tscore1 <= Cscore1 and Tscore1 <= Gscore1:
                    finalScore += Tscore1
                elif Cscore1 <= Ascore1 and Cscore1 <= Tscore1 and Cscore1 <= Gscore1:
                    finalScore += Cscore1
                elif Gscore1 <= Tscore1 and Gscore1 <= Cscore1 and Gscore1 <= Ascore1:
                    finalScore += Gscore1
                T[elm][2][letter] += finalScore

        #daughter

        if type(T[elm][1]) == int:
            for letter in alphabet:
                finalScore = 0
                Ascore2 = T[T[elm][1]][2]["A"]
                if letter != "A":
                    Ascore2 += 1
                Tscore2 = T[T[elm][1]][2]["T"]
                if letter != "T":
                    Tscore2 += 1
                Cscore2 = T[T[elm][1]][2]["C"]
                if letter != "C":
                    Cscore2 += 1
                Gscore2 = T[T[elm][1]][2]["G"]
                if letter != "G":
                    Gscore2 += 1
                if Ascore2 <= Tscore2 and Ascore2 <= Cscore2 and Ascore2 <= Gscore2:
                    finalScore += Ascore2
                elif Tscore2 <= Ascore2 and Tscore2 <= Cscore2 and Tscore2 <= Gscore2:
                    finalScore += Tscore2
                elif Cscore2 <= Ascore2 and Cscore2 <= Tscore2 and Cscore2 <= Gscore2:
                    finalScore += Cscore2
                elif Gscore2 <= Tscore2 and Gscore2 <= Cscore2 and Gscore2 <= Ascore2:
                    finalScore += Gscore2
                T[elm][2][letter] += finalScore

    return T

def smallParsimonyBacktrack(T: dict, character: int):
    alphabet = "ACGT"

    #start from root node, and base strings and scores off this root
    firstElm = list(T.keys())[-1]
    Ascore = T[firstElm][2]["A"]
    Gscore = T[firstElm][2]["G"]
    Cscore = T[firstElm][2]["C"]
    Tscore = T[firstElm][2]["T"]
    if Ascore <= Gscore and Ascore <= Cscore and Ascore <= Tscore:
        T[firstElm][3] += "A"
        T[firstElm][4] += Ascore
    elif Tscore <= Gscore and Tscore <= Cscore and Tscore <= Ascore:
        T[firstElm][3] += "T"
        T[firstElm][4] += Tscore
    elif Gscore <= Ascore and Gscore <= Cscore and Gscore <= Tscore:
        T[firstElm][3] += "G"
        T[firstElm][4] += Gscore
    elif Cscore <= Ascore and Cscore <= Gscore and Cscore <= Tscore:
        T[firstElm][3] += "C"
        T[firstElm][4] += Cscore


    #Scoring inner nodes
    for i in range(1,len(T)):
        elm = list(T.keys())[-i]
        if type(T[elm][0]) == str and type(T[elm][1]) == str:
            pass
        else:
            rootScore = T[elm][2][T[elm][3][character]]


            #have to figure out how to score if one node is a leaf and the other is an inner node
            if type(T[elm][0]) == str or type(T[elm][1]) == str:
                if type(T[elm][0]) == str:
                    for char in alphabet:
                        mod1 = 0
                        mod2 = 0
                        if T[elm][0][character] != T[elm][3][-1]:
                            mod1 += 1
                        if char != T[elm][3][-1]:
                            mod2 += 1
                        if (mod1 + T[T[elm][1]][2][char] + mod2) == rootScore:
                            T[T[elm][1]][3] += char
                            T[T[elm][1]][4] += T[T[elm][1]][2][char]
                            break
                if type(T[elm][1]) == str:
                    for char in alphabet:
                        mod1 = 0
                        mod2 = 0
                        if T[elm][1][character] != T[elm][3][-1]:
                            mod1 += 1
                        if char != T[elm][3][-1]:
                            mod2 += 1
                        if (mod1 + T[T[elm][0]][2][char] + mod2) == rootScore:
                            T[T[elm][0]][3] += char
                            T[T[elm][0]][4] += T[T[elm][0]][2][char]
                            break

            #for scoring two inner nodes
            else:
                for char1 in alphabet:
                    for char2 in alphabet:
                        mod1 = 0
                        mod2 = 0
                        if char1 != T[elm][3][-1]:
                            mod1 += 1
                        if char2 != T[elm][3][-1]:
                            mod2 += 1
                        if (T[T[elm][0]][2][char1] + mod1) + (T[T[elm][1]][2][char2] + mod2) == rootScore:
                            T[T[elm][0]][3] += char1
                            T[T[elm][0]][4] += T[T[elm][0]][2][char1]
                            T[T[elm][1]][3] += char2
                            T[T[elm][1]][4] += T[T[elm][1]][2][char2]
                            break
                    else:
                        continue
                    break

    return T
































