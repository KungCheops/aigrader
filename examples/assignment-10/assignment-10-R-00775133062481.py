def process(s):
    ds = []
    for a in s:
        ds.append(a)
    return ds


def occurrences(ds, queries):
    result = []
    for x in queries:
        a = []
        for position, item in enumerate(ds):
            if item == x:
                a.append(position)
        result.append(a)
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
