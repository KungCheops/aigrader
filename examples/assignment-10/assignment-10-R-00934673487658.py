def process(s):
    ds = {}
    for i, c in enumerate(s):
        if c not in ds:
            ds[c] = []
        ds[c].append(i)
    return ds


def occurrences(ds, queries):
    return [ds.get(character, []) for character in queries]


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('🍢🍢🍢🍢not_emojis🚨', ['🚨', '🍢']) == [[14], [0, 1, 2, 3]]
    assert run('', ['🚨', '🍢']) == [[], []]
    assert run('string', []) == []
    assert run('', []) == []
