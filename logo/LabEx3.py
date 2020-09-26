import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.01, 0.01)
y = np.log((x * x + 1) * np.exp((-1) * (np.abs(x) / 10))) / np.log(1 + np.tan(1 / (1 + np.sin(x) * np.sin(x))))
plt.plot(x, y)
plt.show()
