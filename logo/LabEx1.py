import numpy as np

x = input()
x = np.log(np.exp( 1 / (np.sin(x)+1) ) / ( 1.25 + np.exp( (-15) * np.log(x) ) ) ) / np.log(1 + x * x)
print(x)