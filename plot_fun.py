# Given function plot in range (-20, 20), lets plot the function first
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x1**2 + x2**2

x1 = np.linspace(-20., 20., 20)
x2 = np.linspace(-20., 20., 20)
z = f(x)
fig, ax = plt.subplots(1, 1, figsize=(5, 4), dpi=100)
plt.grid()
plt.plot(x1, z,label='Given function')
plt.legend(loc=1)
plt.show()
