def sublist(s_list):
    for first in range(0, len(s_list)):
        for last in range(first, len(s_list)):
            yield s_list[first:last+1]
def longest_common_list(s_list):
    xs = [x for x in sublist(s_list) for y in sublist(s_list[::-1]) if x == y]
    return max(xs, key=len)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]