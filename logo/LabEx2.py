import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.01, 0.01)
y = x*x - x - 6
plt.plot(x, y)
plt.grid(True)
plt.show()