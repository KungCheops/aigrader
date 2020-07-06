# Scaffold for solution to DIT873 / DAT346, Programming task 1

def fib (limit) :
    a,b = 0, 1
    
    for i in range(0, limit): 
        yield a
        a, b = b, a + b
    return
#G = fib(5)
#print (list(G))

def list_fib(limit) :
    list = [0]
    x,y=0,1

    while y<limit:
            x, y = y, x + y
            list.append(x);
           
    return list
# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
     assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
