def sublist(s_list):
    fst, *rest = s_list
    buf = [fst]
    for val in rest:
      yield buf
      if val < buf[-1]:
        buf = []
      buf = [*buf, val]
    yield buf
def longest_common_list(s_list):
    return max(
      [x for x in sublist(s_list) if x in sublist(reversed(s_list))], key=len
      )
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]