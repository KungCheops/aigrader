def process(s):
    ds = {}
    for idx, val in enumerate(s):
        if val not in ds:
            ds[val] = []
        ds[val].append(idx)
    return ds


def occurrences(ds, queries):
    result = []
    for query in queries:
        result.append(ds[query])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
