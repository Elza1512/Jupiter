import math
import numpy as np
import matplotlib.pyplot as plt

# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

sps = [-12, -18, 5, 10, -30]
x_lim = [-100, 100]

x = np.arange(x_lim[0], x_lim[1], 0.1)

def func(x, a, b, c, d, e):
    return a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e

#print(func(x[0], *sps))
#print(func(x[1], *sps))

x_ch = []
func_dir = -1

color = 'b'
def ch_color():
    global color
    if color == 'b':
        color = 'y'
    else:
        color = 'b'
    return color

for i in range(len(x)-1):
    if func_dir == -1:
        if func(x[i], *sps) < func(x[i + 1], *sps):
            x_ch.append((x[i], func(x[i], *sps)))
            func_dir = 1
    else:
        if func(x[i], *sps) > func(x[i + 1], *sps):
            x_ch.append((x[i], func(x[i], *sps)))
            func_dir = -1

print(x_ch)
print(len(x_ch))

def roots(x, list_roots):
    for i in x:
        if (func(i, *sps) > 0 and func(i-0.01, *sps) <0) or (func(i, *sps) < 0 and func(i-0.01, *sps) >0):
            list_roots.append(round(i,4))
    return list_roots

list_roots = []

roots(x, list_roots)
print(list_roots)

x_range = np.arange(x_lim[0], x_ch[0][0], 0.1)
plt.plot(x_range, func(x_range, *sps), ch_color())
for i in range(len(x_ch)-1):
    x_range = np.arange(x_ch[i][0], x_ch[i+1][0], 0.1)
    plt.plot(x_range, func(x_range, *sps), ch_color())
x_range = np.arange(x_ch[len(x_ch)-1][0], x_lim[1], 0.1)
plt.plot(x_range, func(x_range, *sps), ch_color())
plt.show()

