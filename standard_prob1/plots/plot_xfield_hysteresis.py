import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('table.txt')
data = np.loadtxt('xfield_sweep_table.txt')

t = data[:, 0]
Mx = data[:, 1]
My = data[:, 2]
Mz = data[:, 3]
Bx_ext = data[:, 4]
By_ext = data[:, 5]
Bz_ext = data[:, 6]


B_ext = np.sqrt(Bx_ext**2 + By_ext**2 + Bz_ext**2)*np.sign(Bx_ext)

plt.figure()
plt.xlabel(r'$B_x$ (T)', fontsize = 20)
plt.ylabel(r'$M_x/M_s$', fontsize = 20)
plt.title(r'Field Sweep along Long Axis', fontsize = 25)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

Mx_virgin = Mx[0:75]
Bx_ext_virgin = Bx_ext[0:75]
Mx = Mx[75:len(Mx)]
Bx_ext = Bx_ext[75:len(Bx_ext)]

plt.plot(Bx_ext_virgin, Mx_virgin, 'bo', fillstyle='none')
plt.plot(Bx_ext, Mx, 'bo')
plt.plot(Bx_ext, Mx, 'b')
plt.xlim(-0.05, 0.05)
plt.show()


#plt.figure()
#plt.xlabel('By')
#plt.ylabel('My')
#plt.title('Y-Component')
#plt.plot(By_ext, My, 'bo')
#plt.show()
#
