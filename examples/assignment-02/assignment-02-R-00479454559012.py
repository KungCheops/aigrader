def encode_list(s_list):
  encoding = [s_list[0], 0]
  for c in s_list:
    cur_c, _ = encoding    
    if c != cur_c:
      yield encoding
      encoding = [c, 0]
    encoding[1] += 1
  yield encoding
def create_list (s_list):
  encoded_list = [enc for enc in encode_list(s_list)]    
  return encoded_list
if __name__ == "__main__":
  assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]