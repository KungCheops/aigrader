def process(s):
    ds = {}
    counter = 0
    for ch in s:
        if ch in ds.keys():
            ds[ch].append(counter)
        else:
            ds[ch] = [counter]
        counter += 1
    return ds


def occurrences(ds, queries):
    result = []
    for c in queries:
        if c in ds.keys():
            result.append(ds[c])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
