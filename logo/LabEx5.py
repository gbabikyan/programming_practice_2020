import matplotlib.pyplot as plt
import numpy as np

x = [1, 2.5, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
plt.plot(x, y, 'ro')
plt.plot(x, p_f(x), 'g')
plt.show()
