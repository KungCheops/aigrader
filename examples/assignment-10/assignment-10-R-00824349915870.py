def process(s):
    dss = []
    ds = []
    for i in range(len(s)):
        dss = [s[i], i]
        ds.append(dss)
    return ds


def occurrences(ds, queries):
    pos = []
    pdd = []
    for n in range(len(ds)):
        if ds[n][0] == queries[0]:
            pos.append(n)
        if ds[n][0] == queries[1]:
            pdd.append(n)
    result = [pos, pdd]
    return result


print(occurrences(process('mississippi'), ['s', 'i']))


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
