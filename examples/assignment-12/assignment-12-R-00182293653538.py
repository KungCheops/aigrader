def indexString(s, k):
    endOfString = False
    ds = {}
    if k > len(s):
        print('K greater than string S')
        ds.append(('', 0))
        return ds
    startIndex = 0
    count = 1
    while endOfString == False:
        try:
            for i in s:
                endIndex = startIndex + k
                if endIndex > len(s):
                    endOfString = True
                    break
                substring = s[startIndex:endIndex]
                if substring in ds:
                    amount = ds[substring] + 1
                    ds[substring] = amount
                else:
                    ds[substring] = count
                startIndex += 1
        except IndexError:
            endOfString = True
    return ds


def query(ds, q):
    count = 0
    if q in ds:
        count = ds[q]
    else:
        count = 0
    return count


def frequentKmer(s, k, t):
    dict = indexString(s, k)
    kmers = []
    for i in dict:
        if dict[i] >= t:
            kmers.append(i)
    if kmers == []:
        kmers = ("No substrings of length: ' " + str(k) +
            " ' appearing in the string ' " + s +
            " ' equal or greater than ' " + str(t) + " ' times")
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
