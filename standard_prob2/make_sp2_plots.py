import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('table.txt')

d_ratio = data[:, 0]
mx_remnant = data[:, 1]
my_remnant = data[:, 2]
coercivity = data[:, 3]


plt.figure()
plt.plot(d_ratio, mx_remnant, 'ko')
plt.xlabel('d/l_ex')
plt.ylabel('Remnant Mx')
plt.title('X-component')
plt.show()

plt.figure()
plt.plot(d_ratio, my_remnant, 'ko')
plt.xlabel('d/l_ex')
plt.ylabel('Remnant My')
plt.title('Y-component')
plt.show()

plt.figure()
plt.plot(d_ratio, coercivity, 'ko')
plt.xlabel('d/l_ex')
plt.ylabel('Coercitivy')
plt.title('Coercivity')
plt.show()

