def indexString(s, k):
    ds = {}
    last_char = ''
    count = 0
    for current_char in s:
        if current_char == last_char:
            count += 1
            if count == k:
                if current_char * count in ds:
                    ds[current_char * count] += 1
                else:
                    ds[current_char * count] = 1
                count -= 1
        else:
            last_char = current_char
            count = 1
    return ds


def query(ds, q):
    return ds[q]


def frequentKmer(s, k, t):
    kmers = []
    for q, count in indexString(s, k).items():
        if count >= t:
            kmers.append(q)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert frequentKmer('aaaabbaaaabbbbbaaaabbbaba', 3, 2) == ['aaa', 'bbb']
