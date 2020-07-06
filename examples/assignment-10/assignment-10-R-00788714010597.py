def process(s):
    ds = dict()
    s = s.lower()
    for i in range(len(s)):
        if s[i] in ds.keys():
            ds[s[i]].append(i)
        else:
            ds.update({s[i]: [i]})
    return ds


def occurrences(ds, queries):
    result = []
    for j in queries:
        result.append(ds[j])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
