import matplotlib.pyplot as plt
import numpy as np

"""Loading Data"""

data = np.loadtxt('field1_spatial_mag_data.csv', delimiter = ',')
triple_Ny, Nx = np.shape(data) # Number of points along X and Y directions
Ny = int(triple_Ny/3)

Mx = data[0:Ny, :]
My = data[Ny:2*Ny, :]
Mz = data[2*Ny:3*Ny, :]

x_vec = np.linspace(0, 500e-9, Nx)
y_vec = np.linspace(0, 125e-9, Ny)
X, Y = np.meshgrid(x_vec, y_vec)

"""Component Plots"""

plt.figure()
plt.imshow(Mx)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('X-component')
plt.show()


plt.figure()
plt.imshow(My)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Y-component')
plt.show()

plt.figure()
plt.imshow(Mz)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Z-component')
plt.show()
