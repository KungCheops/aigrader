import numpy as np
from itertools import cycle
def sublist(s_list):
    revlist=[]
    currentbest=[]
    for s in s_list:
        revlist.append(s)
    revlist.reverse()
    listoflists=[]
    for i in range(0,len(s_list)):
        for k in range(0,len(s_list)):
            tmplist=[]
            if s_list[k]==revlist[i]:
                while s_list[k]==revlist[i] and k<=len(s_list)-1 and i<=len(s_list)-1:
                    tmplist.append(revlist[i])
                    if i != len(s_list)-1:
                        i+=1
                    if k != len(s_list)-1:
                        k+=1
                yield tmplist
    return
def longest_common_list(s_list):
    kingiterator=sublist(s_list)
    kinglist=[]
    for element in kingiterator:
        kinglist.append((element,len(element)))
    sortedlist = sorted(kinglist, key=lambda tup: tup[1],reverse=True)
    return sortedlist[0][0]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]