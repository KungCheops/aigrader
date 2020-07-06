def indexString(s, k):
    ds = {}
    if s == None or s == '':
        print('Invalid Input: s is empty or none')
        return ds
    if k == None or k < 1 or k > len(s):
        print('Invalid Input: Enter a valid k value')
        return ds
    for index, letter in enumerate(s):
        final_string = ''
        final_string = letter
        inner_start_idx = index + 1
        inner_end_idx = index + k - 1
        if inner_start_idx <= len(s) and inner_end_idx <= len(s) - 1:
            for i in range(inner_start_idx, inner_end_idx + 1):
                final_string = final_string + s[i]
            if final_string in list(ds.keys()):
                ds[final_string] = ds[final_string] + 1
            else:
                ds[final_string] = 1
    return ds


def query(ds, q):
    if q == None:
        print('Invalid input: q is none')
        return 0
    if ds == None:
        print('Invalid input: ds is none')
        return 0
    list_of_keys = list(ds.keys())
    if q in list_of_keys:
        return ds[q]
    else:
        return 0


def frequentKmer(s, k, t):
    kmers = []
    if t == None:
        print('Invalid input: t cannot be None')
        return kmers
    ds = indexString(s, k)
    list_of_keys = list(ds.keys())
    for key in list_of_keys:
        if ds[key] >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
