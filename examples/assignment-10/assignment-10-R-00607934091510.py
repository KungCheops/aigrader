def process(s):
    ds = {}
    for key, value in enumerate(s):
        if value not in ds:
            ds[value] = []
        ds[value].append(key)
    return ds


def occurrences(ds, queries):
    result = []
    for c in queries:
        result.append(ds[c])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    print(run('mississippi', ['s', 'i']))
