a = int(input('Give limit: '))
# this is the function use for loop instead of generator
def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L

print(list(fab(a)))   

# the generator fib function
def fib(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 
''' 
I am not sure what does limit means so i create another
fib function return fib series smaller than the limit
'''
num = int(input('Give amount: '))
def fib2(limit): 
    a, b = 1, 1 
    while b < limit: 
        yield b 
        # print b 
        a, b = b, a + b 
for n in fib2(num): 
  print(n)  

'''
To printout the list,
f = fib(limit)
f.next()
for example
f = fib(5)
>>> f.next() 
1 
>>> f.next() 
1 
>>> f.next() 
2 
>>> f.next() 
3 
>>> f.next() 
5 
>>> f.next() 

'''

