def process(s):
    ds = {}
    s = s.lower()
    for l in s:
        ds[l] = [i for i, letter in enumerate(s) if letter == l]
    return ds


def occurrences(ds, queries):
    result = [ds[i] for i in queries]
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('aabbcc', ['a', 'b', 'c']) == [[0, 1], [2, 3], [4, 5]]
    assert run('AabBcC', ['a', 'b', 'c']) == [[0, 1], [2, 3], [4, 5]]
