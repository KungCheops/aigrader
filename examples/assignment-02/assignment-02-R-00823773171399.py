def encode_list(s_list):
    i = 0
    while i < len(s_list):
        j = i + 1
        while j < len(s_list) and s_list[i] == s_list[j]:
            j += 1
        yield [s_list[i], j-i]
        i = j
def create_list(s_list):
    return [x for x in encode_list(s_list)]
def test_integers():
    actual = create_list([1, 1, 1, 2, 3, 3, 4, 4, 5, 1, 1, 7, 5])
    expected = [[1, 3], [2, 1], [3, 2], [4, 2], [5, 1], [1, 2], [7, 1], [5, 1]]
    assert actual == expected
    print("SUCCESS for test_integers()")
def test_characters():
    actual = create_list(["a", "a", "a", "b", "c", "c", "d", "d", "e", "a", "a", "g", "e"])
    expected = [["a", 3], ["b", 1], ["c", 2], ["d", 2], ["e", 1], ["a", 2], ["g", 1], ["e", 1]]
    assert actual == expected
    print("SUCCESS for test_characters()")
if __name__ == "__main__":
    test_integers()
    test_characters()