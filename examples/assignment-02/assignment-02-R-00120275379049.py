def encode_list(s_list):
    count =1
    for i in range(len(s_list)):
       number_to_check= s_list[i]
       if (i == len(s_list)-1 ):  
           yield [number_to_check,count]
           count=1
       elif (s_list[i+1]== number_to_check):
           count+=1
       else :
           yield [number_to_check,count]
           count=1
def create_list (s_list):
    the_list=encode_list(s_list)
    return list(the_list)
if __name__ == "__main__":
    assert create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1,1,7,5]) == [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]