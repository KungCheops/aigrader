def process(s):
    ds = []
    for c in s:
        ds.append(c)
    return ds


def occurrences(ds, queries):
    result = []
    for q in queries:
        results = []
        for i, c in enumerate(ds):
            if c == q:
                results.append(i)
        result.append(results)
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
