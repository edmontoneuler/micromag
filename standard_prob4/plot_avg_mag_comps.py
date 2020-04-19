import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('field1_table.txt')

t = data[:, 0]
mx = data[:, 1]
my = data[:, 2]
mz = data[:, 3]


plt.figure()

plt.plot(t, mx, 'r')
plt.plot(t, my, 'b')
plt.plot(t, mz, 'g')
plt.legend(['Mx', 'My', 'Mz'])

plt.xlabel('Time (s)')
plt.ylabel('M/Ms')
plt.title('Average Magnetization Components')

plt.show()



