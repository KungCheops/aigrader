def process(s):
    ds = {}
    c = 0
    for i in s:
        if i in ds:
            ds[i] = ds.get(i) + [c]
        else:
            ds[i] = [c]
        c += 1
    return ds


def occurrences(ds, queries):
    result = []
    for i in queries:
        a = ds.get(i)
        result.append(a)
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('m', ['m', 'i']) == [[0], None]
