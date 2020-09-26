import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.01, 0.01)
y = input()
with plt.xkcd():
    plt.plot(x, y)
    plt.show()
