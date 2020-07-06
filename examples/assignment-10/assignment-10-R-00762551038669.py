def process(s):
    ds = []
    for letter in s:
        ds.append(letter)
    return ds


def occurrences(ds, queries):
    result = []
    for letter in queries:
        templist = []
        counter = 0
        for letter2 in ds:
            if letter == letter2:
                templist.append(counter)
            counter += 1
        result.append(templist)
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('Boston', ['B', 'o', 's']) == [[0], [1, 4], [2]]
