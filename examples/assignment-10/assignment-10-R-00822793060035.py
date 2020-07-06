def process(s):
    ds = {}
    for pos, char in enumerate(s):
        if char not in ds:
            ds[char] = [pos]
        else:
            ds[char].append(pos)
    return ds


def occurrences(ds, queries):
    result = []
    for q in queries:
        if q in ds:
            result.append(ds[q])
        else:
            result.append([0])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
