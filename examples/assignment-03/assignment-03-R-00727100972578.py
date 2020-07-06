def sublist(s_list):
    returnlist= []
    for i in range (len(s_list)):
        if len(returnlist) ==0 :
            returnlist.append(s_list[i])
        if (i == len(s_list)-1):
            yield returnlist
        elif (s_list[i+1]  >= s_list[i]):
            returnlist.append(s_list[i+1])
        else:
             yield returnlist
             returnlist=[]
def longest_common_list(s_list):
    sub_list= list(sublist(s_list))
    s_list.reverse()
    reversedsublist= list(sublist(s_list))
    common_list = [i for i in sub_list if i in reversedsublist]
    return  max(common_list,key=len)
thelist = [1,2,3,2,2,3,2,1,4]
print(longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]))
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]