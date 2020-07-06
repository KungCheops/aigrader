# Scaffold for solution to DIT873 / DAT346, Programming task 1
def fib (limit) :
    x = 0
    y= 1
    while x < limit:

       yield x
       x , y = y , x + y
    return x

def list_fib(limit) :
    li = []
    fi = fib(limit)
    for i in fi:
        li.append(i)
    return li

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
