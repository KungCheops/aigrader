import string


def process(s):
    s = s.lower()
    charList = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [
        ], [], [], [], [], [], [], [], [], [], []
    i = 0
    for char in string.ascii_lowercase:
        j = 0
        for c in s:
            if char == c:
                charList[i].append(j)
            j += 1
        i += 1
    return charList


def occurrences(ds, queries):
    result = []
    for i in range(len(queries)):
        j = 0
        for char in string.ascii_lowercase:
            if queries[i] == char:
                result.append(ds[j])
                break
            j += 1
    return result


def run(s, query):
    return occurrences(process(s), query)


if __name__ == '__main__':
    assert run('mississippi', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
    assert run('MississippI', ['s', 'i']) == [[2, 3, 5, 6], [1, 4, 7, 10]]
