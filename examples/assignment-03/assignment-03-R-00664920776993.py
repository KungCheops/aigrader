from operator import itemgetter
def sublist(s_list):
    n=s_list[0]
    sublist=[]
    for v in s_list:
        if v>=n:
            sublist.append(v)
            n=v
        else:
            yield sublist
            sublist=[v]
            n=v
    yield sublist
def longest_common_list(s_list):
    s_list_rev=[i for i in reversed(s_list)]
    sublists=sublist(s_list)
    sublists_rev=sublist(s_list_rev)
    common_list=[[len(a),a] for a in sublists if a in sublists_rev]
    return sorted(common_list)[-1][1]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]