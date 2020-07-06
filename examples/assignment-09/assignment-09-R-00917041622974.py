import math
from GDPvsLE import *


def quartiles(l):
    l.sort()
    n = len(l)
    median = lambda nums: nums[(len(nums) - 1) // 2] if len(nums
        ) % 2 == 1 else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    divide_list = lambda nums: [nums[0:n // 2], nums[n // 2:n]
        ] if n % 2 == 0 else [nums[0:(n + 1) // 2], nums[(n - 1) // 2:n]]
    Q2 = median(l)
    Q1 = median(divide_list(l)[0])
    Q3 = median(divide_list(l)[1])
    return Q1, Q2, Q3


print(quartiles(gdp))
print(quartiles(le))
if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4]) == (1.5, 2.5, 3.5)
    assert quartiles([1, 2, 3, 4, 5, 6, 7]) == (2.5, 4, 5.5)
    assert quartiles([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == (1, 1, 1)
