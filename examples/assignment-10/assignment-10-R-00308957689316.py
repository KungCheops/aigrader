"""
Spyder Editor

This is a temporary script file.
"""


def process(s):
    ds = dict()
    for key, val in enumerate(s):
        if val not in ds:
            ds[val] = []
        ds[val].append(key)
    return ds


def occurrences(ds, queries):
    result = []
    for c in queries:
        result.append(ds[c])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
