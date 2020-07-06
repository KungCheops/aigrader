def process(s):
    """
    Transforms a string into lower case letters.
    Returns a dict with letters as keys and a corresponding list with
    positional occurences as values.
    """
    s = s.lower()
    ds = {}
    for i, c in enumerate(s):
        if not c in ds.keys():
            ds[c] = [i]
        else:
            ds[c].append(i)
    return ds


def occurrences(ds, queries):
    """
    Transforms the 1 character queries into lower case and fetches
    the occurence list from the ds-dict.
    """
    result = []
    for c in queries:
        try:
            result.append(ds[c.lower()])
        except KeyError:
            if len(c) == 0:
                print(f'A query is empty')
            elif len(c) > 1:
                print(f'The query {c} has more then one character')
            else:
                print(f'The character {c} does not exist in the string.')
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('miSSissippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('miSSissippi', ['S', 'I']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('hej håpp', ['å', 'p']) == [[5], [6, 7]]
    assert run('', ['']) == []
    assert run('fffF', ['s']) == []
