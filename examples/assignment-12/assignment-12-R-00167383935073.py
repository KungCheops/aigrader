"""
Implement the body of a Python function which takes a string as input and counts the frequency of substrings of k consecutive characters . 
In particular, implement a function indexString(s, k), which takes a string and k as the input and returns a data structure of counts, query(ds, q), 
which given such a data structure returns the number of occurrences of q in s, 
and frequentKmer(s, k, t) which returns a list of all substrings of k consecutive characters which appear at least t times in s.
"""


def indexString(s, k):
    ds = {}
    for i in range(0, len(s) - k + 1):
        substr = s[i:i + k]
        ds[substr] = ds.get(substr, 0) + 1
    return ds


def query(ds, q):
    return ds.get(q, 0)


def frequentKmer(s, k, t):
    if t < 0:
        raise Exception('Invalid value provided')
    return [sub for sub, count in indexString(s, k).items() if count >= t]


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert query(indexString('AAAAA', 3), '') == 0
    assert query(indexString('', 3), '') == 0
    assert query(indexString('AAAAA', 10), 'AAA') == 0
    assert query(indexString('AAAAA', -1), 'AAA') == 0
    assert frequentKmer('aaaabbaabb', 2, 2) == ['aa', 'ab', 'bb']
    assert frequentKmer('aaaabbaabb', 2, 0) == ['aa', 'ab', 'bb', 'ba']
