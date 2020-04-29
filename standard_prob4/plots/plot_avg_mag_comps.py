import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('field2_table.txt')

t = data[:, 0]
mx = data[:, 1]
my = data[:, 2]
mz = data[:, 3]


plt.figure()

plt.plot(t, mx, 'r')
plt.plot(t, my, 'g')
plt.plot(t, mz, 'b')
plt.legend(['Mx', 'My', 'Mz'])

#Field 1 Limiting Values
plt.axhline(-0.985964, color = 'r', linestyle = '--')
plt.axhline(-0.172186, color = 'g', linestyle = '--')
plt.axhline(0, color = 'b', linestyle = '--')

plt.xlabel('Time (s)')
plt.ylabel('M/Ms')
plt.title('Average Magnetization Components')

plt.show()



