import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('table.txt')

t = data[:, 0]
Mx = data[:, 1]
My = data[:, 2]
Mz = data[:, 3]
Bx_ext = data[:, 4]
By_ext = data[:, 5]
Bz_ext = data[:, 6]


B_ext = np.sqrt(Bx_ext**2 + By_ext**2 + Bz_ext**2)*np.sign(Bx_ext)


plt.xlabel('Bx')
plt.ylabel('Mx')
plt.title('X-Component')

plt.plot(Bx_ext, My, 'b')

plt.show()


