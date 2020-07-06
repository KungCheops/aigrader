def process(s):
    ds = {}
    for i, j in enumerate(s):
        if j in ds.keys():
            ds[j] = ds[j] + [i]
        else:
            ds[j] = [i]
    return ds


def occurrences(ds, queries):
    result = [ds[i] for i in queries]
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
