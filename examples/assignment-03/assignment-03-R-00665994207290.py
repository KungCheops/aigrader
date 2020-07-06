def sublist(s_list):
    def sublist_generator(s_list):
        current_number = s_list[0]
        current_list = [current_number]
        for index in range(1, len(s_list)):
            new_number = s_list[index]
            if new_number >= current_number:
                current_list.append(new_number)
                current_number = new_number
            else:
                current_number = new_number
                yield tuple(current_list)
                current_list = [new_number]
    def generate_subsplits(s_list):
        subsplits = set()
        for i in range(len(s_list)):
            for j in range(len(s_list)):
                if i <= j:
                    subsplits.add(tuple(s_list[i:j + 1]))
        return subsplits
    set_of_subs = {x for x in sublist_generator(s_list)}
    set_of_subsets = {sub for x in set_of_subs for sub in generate_subsplits(x)}
    for i in set_of_subsets:
        yield i
def longest_common_list(s_list):
    correct_order = [x for x in sublist(s_list)]
    reverse_order = [x for x in sublist(s_list[::-1])]
    best_length = 0
    current_list = []
    for tuple in correct_order:
        if tuple in reverse_order and len(tuple) > best_length:
            current_list = list(tuple)
            best_length = len(tuple)
    return current_list
if __name__ == "__main__":
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1, 1, 2, 3]