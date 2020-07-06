def sublist(s_list):
    for i in range(0, len(s_list)):
        for j in range(i+1, len(s_list)):
            if s_list[j] >= s_list[j-1]:
                yield s_list[i:j+1]
            else:
                break
def longest_common_list(s_list):
    sublists_original = [l for l in sublist(s_list)]
    sublists_reversed = [l for l in sublist(s_list[::-1])]
    common_sublists = [l1 for l1 in sublists_original for l2 in sublists_reversed if l1 == l2]
    longest_length = 0
    longest_sublist = []
    for l in common_sublists:
        if len(l) > longest_length:
            longest_length = len(l)
            longest_sublist = l
    return longest_sublist    
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1,2,3]
    print("TEST SUCCESS")