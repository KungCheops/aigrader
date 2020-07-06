def process(s):
    ds = {}
    if isinstance(s, str):
        for idx, val in enumerate(s):
            if val not in ds:
                ds[val] = []
            ds[val].append(idx)
    else:
        print('Please enter a valid string.')
    return ds


def occurrences(ds, queries):
    result = []
    for query in queries:
        if query in ds:
            result.append(ds[query])
        else:
            print('The character in the query is not in the string.')
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('abracadabra', ['a', 'b', 'r']) == [[0, 3, 5, 7, 10], [1, 8],
        [2, 9]]
