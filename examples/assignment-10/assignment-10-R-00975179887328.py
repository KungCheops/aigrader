def process(s):
    s = list(s)
    ds = dict()
    for i in range(0, len(s)):
        c = s[i]
        ds[c] = ds.get(c, []) + [i]
    return ds


def occurrences(ds, queries):
    result = [ds.get(q) for q in queries]
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('maxmustermann', ['m', 'n', 'a']) == [[0, 3, 9], [11, 12], [
        1, 10]]
    assert run('test', []) == []
    assert run('test', ['x']) == [None]
    assert run('.test.', ['x', '.', 'y']) == [None, [0, 5], None]
