def fib (limit) :
    '''
     I create two variables and set them equal to 0 and 1 since those numbers are the first two numbers in the fibonacci sequence.
     I then use a while loop that will run as long as i is <= limit which is 20 in this example.
     I use the yield kejword to make this a generator function and the variables are preserved.
     I then store i in a temporary variable and set i = j and j = tmp + i.
     This way i can generate my fibonacci sequence.
    ''' 
    i = 0
    j = 1
    while i <= limit:
        yield i
        tmp = i
        i = j
        j = tmp + i

def list_fib(limit) :
    
    return list(fib(limit))

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    print(list_fib(20))
    
    