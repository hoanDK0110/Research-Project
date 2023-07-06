import matplotlib.pyplot as plt
import numpy as np

loaded_data = np.loadtxt('data_reward.txt')
loaded_data_2d = np.reshape(loaded_data, (loaded_data.shape[0], -1))
x = np.arange(5000)
y = loaded_data_2d[x]

plt.scatter(x, y)
plt.show()