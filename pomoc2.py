import numpy as np
import matplotlib.pyplot as plt
from math import e
t = np.linspace(-2,2)
x = np.linspace(-2,2)
plt.plot(x,t**2*np.sin(t), label = "f(t)")
plt.plot(x,e**t, label = "g(t)")
plt.legend()
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title('Exercise 1')
plt.savefig("plot_zad1.png")
plt.show()