def sublist(s_list):
    for element, index in zip(s_list, range(len(s_list))):
        for innerdex in range(index,len(s_list)):
            yield s_list[index:innerdex+1]
    return
def longest_common_list(s_list):
    sublists1 = []
    sublists2 = []
    generator1 = sublist(s_list)
    for list in generator1:
        sublists1 += [list]
    s_list.reverse()
    generator2 = sublist(s_list)
    for list in generator2:
        sublists2 += [list]
    s_list.reverse()
    sublist_counts = [(elem,len(elem)) for elem in sublists1 if elem in sublists2]
    output         = [elem for (elem,count) in sublist_counts if count == max([count for (elem,count) in sublist_counts])]
    return output[0]
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]