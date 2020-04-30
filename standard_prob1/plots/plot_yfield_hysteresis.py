import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('table.txt')
data = np.loadtxt('yfield_sweep_table.txt')

t = data[:, 0]
Mx = data[:, 1]
My = data[:, 2]
Mz = data[:, 3]
Bx_ext = data[:, 4]
By_ext = data[:, 5]
Bz_ext = data[:, 6]


B_ext = np.sqrt(Bx_ext**2 + By_ext**2 + Bz_ext**2)*np.sign(Bx_ext)

plt.figure()
plt.xlabel(r'$B_y$ (T)', fontsize = 20)
plt.ylabel(r'$M_y/M_s$', fontsize = 20)
plt.title(r'Field Sweep along Short Axis', fontsize = 25)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

My_virgin = My[0:75]
By_ext_virgin = By_ext[0:75]
My = My[75:len(My)]
By_ext = By_ext[75:len(By_ext)]

plt.plot(By_ext_virgin, My_virgin, 'bo', fillstyle='none')
plt.plot(By_ext, My, 'bo')
plt.plot(By_ext, My, 'b')
plt.xlim(-0.05, 0.05)
plt.show()

