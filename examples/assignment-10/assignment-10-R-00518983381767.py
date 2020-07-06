def process(s):
    ds = dict()
    ls = list(s)
    i = 0
    for character in ls:
        if character in ds:
            ds[character].append(i)
        else:
            ds[character] = [i]
        i += 1
    return ds


def occurrences(ds, queries):
    result = []
    for character in queries:
        if character in ds:
            result.append(ds[character])
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
