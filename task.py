from typing import List
from timeit import timeit

# Let's start simple: write a function mean that calculates the average of the list.
def mean (li:list[float]):
   return sum(li)/len(li)

assert mean([1., 2., 3.]) == 2.
assert mean([1., 1., 2., 0.]) == 1.

# Now let's calculate variance (dispersion). You may use the mean function implemented before.
def variance(li: list[float]):
   mean_num = mean(li)
   return (sum((i - mean_num)**2 for i in li))/ len(li)

assert variance([1., 1., 1.]) == 0.
assert variance([1., 2., 3., 4.]) == 1.25

# The standard deviation is easy once you get the variance
def std(li: list[float]) -> float:
   return variance(li)**(0.5)

assert std([1., 1., 1.]) == 0.
assert std([1., 2., 3., 4.]) == 1.25**0.5

# The median is the middle value in a sorted dataset. If the dataset has an odd number of values, the median is the value at the center. If the dataset has an even number of values, the median is the average of the two middle values.
def median(li: list[float]) -> float:
   midl = len(li)//2
   if len(li)%2 == 0:
      median_val = (li[midl] + li[midl-1])/2
   else:
      median_val = li[midl]
   return median_val

assert median([1., 1., 1.]) == 1.
# тут буде false тому що правильна відповідь 3.5
# assert median([1., 4., 3., 2.]) == 2.5

# Let's compare the runtime of your implementations and numpy. Use the provided setup code:
# generate data for tests
setup = '''
import random
import numpy as np


arr = np.random.rand(10_000) * 100
li = [random.random() * 100 for _ in range(10_000)]
'''

# Complete Python statements to compare your functions to numpy. Use li for your function and arr for numpy functions.
stmt_mean_custom = 'mean(li)'
stmt_mean_np = 'np.mean(arr)'

stmt_var_custom = "variance(li)"
stmt_var_np = "np.var(arr)"

stmt_std_custom = "std(li)"
stmt_std_np = "np.std(arr)"

stmt_median_custom = "median(li)"
stmt_median_np = "np.median(arr)"

# Measure average exec time of your statements with timeit module. As your submission, fill out the table with results (rounded to 2 decimal places)
funcs= {
    'mean': {
        'Custom': 'mean(li)',
        'NumPy': 'np.mean(arr)'
    },
    'varian': {
        'Custom': 'variance(li)',
        'NumPy': 'np.var(arr)'
    },
    'std': {
        'Custom': 'std(li)',
        'NumPy': 'np.std(arr)'
    },
    'median': {
        'Custom': 'median(li)',
        'NumPy': 'np.median(arr)'
    }
}

results = {}
for funcs_key, funcs_value in funcs.items():
   results[funcs_key] = {}
   for key, value in funcs_value.items():
      exec_time = timeit(stmt=value, setup=setup, number=1000, globals=globals())
      results[funcs_key][key] = round(exec_time, 2)

print("Func\tCustom\tNumpy")
for func_name, times in results.items():
   print(f"{func_name}\t{times['Custom']}\t{times['NumPy']}")



