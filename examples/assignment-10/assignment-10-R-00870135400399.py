def process(s):
    ds = {}
    for i, c in enumerate(s):
        if not c in ds.keys():
            ds[c] = [i]
        else:
            ds[c].append(i)
    return ds


def occurrences(ds, queries):
    result = []
    for a in queries:
        result.append(ds[a])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
