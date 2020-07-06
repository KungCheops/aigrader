def process(s):
    ds = []
    for i in range(len(s)):
        ds.append(s[i])
    return ds


def occurrences(ds, queries):
    result = []
    for c in queries:
        q = []
        for i in range(len(ds)):
            if ds[i] == c:
                q.append(i)
        result.append(q)
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('', [' ', 'i']) == [[], []]
    assert run('hello world', ['h', ' ', 'l']) == [[0], [5], [2, 3, 9]]
