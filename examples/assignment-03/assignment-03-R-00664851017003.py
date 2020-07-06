def sublist(s_list):
    i = 0
    while i < len(s_list):
        result = [s_list[i]]
        j = i
        while j < (len(s_list) - 1):
            if s_list[j] == s_list[j+1]:
                result.append(s_list[j+1])
            elif s_list[j] + 1 == s_list[j+1]:
                result.append(s_list[j+1])
            else:
                break
            j += 1
        yield result
        i += 1
    return
def longest_common_list(s_list):
    common = [x for x in sublist(s_list) if x in sublist(s_list[::-1])]
    return max(common, key=len)
if __name__ == "__main__":
    list = longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2])
    print (list)
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]