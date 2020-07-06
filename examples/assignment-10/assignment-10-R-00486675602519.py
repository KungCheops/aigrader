def process(s):
    s = s.lower()
    ds = {}
    for i in range(len(s)):
        if s[i] not in ds:
            ds[s[i]] = [i]
        else:
            ds[s[i]].append(i)
    return ds


def occurrences(ds, queries):
    result = []
    for c in queries:
        if c in ds:
            result.append(ds[c])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
