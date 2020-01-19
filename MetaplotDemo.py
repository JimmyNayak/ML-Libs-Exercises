import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

# data = np.linspace(0, 10, 100)
# print(data)
#
# plt.plot(data, data, label='Linear')
# plt.legend()
# plt.show()


# x = [590, 150, 455, 890, 200, 300, 100, 500, 400, 255, 380]
# y = [11, 54, 23, 15, 82, 77, 95, 36, 45, 75, 19]
#
# plt.scatter(x, y)
# plt.show()


#  Histogram

data = np.random.normal(5.0,3.0,100)
pl.hist(data)
pl.xlabel('Data')
pl.show()
