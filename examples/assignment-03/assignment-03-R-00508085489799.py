def sublist(s_list):
    sequences_s_list = []
    s_sequence = []
    for i in range(len(s_list)):
        number = s_list[i]
        if i+1 < len(s_list):
            if number <= s_list[i+1]:
                s_sequence.append(number)
            else:
                if(len(s_sequence) > 0):
                    s_sequence.append(number)
                    yield s_sequence
                    s_sequence = []
        else:
            s_sequence.append(s_list[len(s_list) - 1])
            sequences_s_list.append(s_sequence)
    return sequences_s_list
def longest_common_list(s_list):
    s_list_reversed = list(reversed(s_list))
    sequence_lists = []
    sequence_reversed_lists = []
    generator_s_list = sublist(s_list)
    generator_s_list_reversed = sublist(s_list_reversed)
    for x in generator_s_list:
        sequence_lists.append(x)
    for x in generator_s_list_reversed:
        sequence_reversed_lists.append(x)
    common_lists = [sequence_lists[i] for i in range(len(sequence_lists)) for j in range(len(sequence_reversed_lists)) if sequence_lists[i] == sequence_reversed_lists[j]]
    longest_common_list = max(common_lists, key=len)
    return longest_common_list
s_list = [1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]
common_list = longest_common_list(s_list)
print('Longest common list:', common_list)
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]