def process(s):
    ds = {}
    for index, char in enumerate(s):
        if char not in ds:
            positions = []
            ds[char] = positions
        ds[char].append(index)
    return ds


def occurrences(ds, queries):
    result = []
    for key in queries:
        if key in ds:
            result.append(ds[key])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
