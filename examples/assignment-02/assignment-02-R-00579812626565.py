def encode_list(s_list):
    input= (i for i in s_list )
    for i in input:
      yield i
def create_list1(s_list):
  encoded_list=[]
  l=[]
  x=encode_list(s_list)
  for i in x:
    l.append(i)
  current=[l[0],1]
  encoded_list=[current]
  for j in l[1:]:
    if j==current[0]:
      current[1]+=1
    else:
      current=[j,1]
      encoded_list.append(current)
  return encoded_list
if __name__ == "__main__":
    assert create_list1([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], 
[3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]