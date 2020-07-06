def process(s):
    ds = {}
    for i, c in enumerate(s):
        ds.setdefault(c, []).append(i)
    return ds


def occurrences(ds, queries):
    l = []
    for c in queries:
        l.append(ds[c])
    return l


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('hejhopp', ['e', 'o', 'p']) == [[1], [4], [5, 6]]
