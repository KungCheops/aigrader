#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Scaffold for solution to DIT873 / DAT346, Programming task 1
def fib (limit) :
    a, b = 0, 1 
    for i in range(0,limit): 
        yield a
        a,b = b, a+b 
    
def list_fib(limit):
    return [x for x in fib(limit) if x < limit]

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]


# In[ ]:




