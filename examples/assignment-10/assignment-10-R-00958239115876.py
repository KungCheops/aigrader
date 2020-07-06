def process(s):
    ds = {}
    for index, value in enumerate(s):
        if value in ds.keys():
            ds[value].append(index)
        else:
            ds[value] = [index]
    return ds


def occurrences(ds, queries):
    result = []
    for value in queries:
        if value in ds.keys():
            result.append(ds[value])
        else:
            return 0
    return result


def run(s, query):
    return occurrences(process(s), query)


run('mississippi', ['a'])
if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('hello', ['h', 'l']) == [[0], [2, 3]]
    assert run('mississippi', ['a']) == 0
    assert run('', ['h']) == 0
