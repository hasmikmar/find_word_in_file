import  sys

res = ""


def check(d, s):
    s = s.lower()
    global res
    i = 0
    j = 0
    while (i < len(d) and j < len(s)):

        if (d[i] == s[j]):
            i += 1
            j += 1
        else:
            j += 1

        if (i == len(d) and len(res) < len(d)):
            res = d
    return res       


def LongestWord(d, S):
    for c in d:
        check(c, S)

    return res


filename='file'
mylist=[]
with open(filename,'r') as file:
   
    for line in file:
           for word in line.split():
             word = word.lower()
             mylist.append(word)
string = "abpcplea"
print(LongestWord(mylist, string))
