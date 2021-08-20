# Assignment 2: Order of growth
# Graph the functions 1, n, n^2, sqrt(n), n log n, n^3, 2^n using python
# by: Pranpreya Samasutthi (st122602)

import matplotlib.pyplot as plt
import numpy as np
np.seterr(over='ignore')  # completely remove the runtimeWarning

x = np.logspace(0, 15, 100, dtype=np.float64)  # module 'numpy' has no attribute 'float128'
y_1 = np.ones(100)  # Return a new array of given shape and type, filled with ones. y =[1, 1, 1, ..., 1]
y_n = x
y_square = x * x
y_squareroot = np.sqrt(x)
y_nlogn = x * np.log(x)
y_cube = x ** 3
y_2n = 2 ** x

fig = plt.figure()
p = fig.add_subplot(1, 1, 1)
p.set_yscale('log')
p.set_xscale('log')
p.set_xlim(1, 10**15)   # x axis is from 0 - 10^15
p.set_ylim(1, 10**19)   # y axis is from 0 - 10^19
p.plot(x, y_1, label='1')
p.plot(x, y_n, label='n')
p.plot(x, y_square, label='n^2')
p.plot(x, y_squareroot, label='sqrt(n)')
p.plot(x, y_nlogn, label='n log n')
p.plot(x, y_cube, label='n^3')
p.plot(x, y_2n, label='2^n')
plt.title('Order of growth')
plt.legend()
plt.show()
