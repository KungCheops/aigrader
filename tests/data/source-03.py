def fib(limit):
    curr = 1
    prev = 0
    a = prev
    while prev <= limit:
        yield prev
        curr = prev + curr
        prev = curr - prev

def list_fib(limit):
    list = []
    next = 1
    if limit >= 0:
        list.append(0)
    if limit >= 1:
        list.append(1)
    while next <= limit:
        list.append(next)
        next = list[-1] + list[-2]
    return list

if __name__ == "__main__":
    for num in fib(20):
        print(num)
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
