import matplotlib.pyplot as plt
import numpy as np
import skimage.measure

"""Loading Data"""

data = np.loadtxt('field2_spatial_mag_data.csv', delimiter = ',')
triple_Ny, Nx = np.shape(data) # Number of points along X and Y directions
Ny = int(triple_Ny/3)

Mx = data[0:Ny, :]
My = data[Ny:2*Ny, :]
Mz = data[2*Ny:3*Ny, :]

x_vec = np.linspace(0, 500e-9, Nx)
y_vec = np.linspace(0, 125e-9, Ny)
X, Y = np.meshgrid(x_vec, y_vec)


"""Thin out data"""

n = 5 #keep every nth data point
X_thin = X[::n, ::n]
Y_thin = Y[::n, ::n]
Mx_thin = Mx[::n, ::n]
My_thin = My[::n, ::n]
Mz_thin = Mz[::n, ::n]

def make_inplane_magplot(X, Y, Mx, My, colordata=np.ones_like(X)):

    fig = plt.figure()
    I = plt.imshow(colordata,extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)])
    Q = plt.quiver(X,Y,Mx,My)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    cbar = plt.colorbar(orientation='horizontal')
    cbar.set_label('Mz')
    plt.clim(np.min(colordata), np.max(colordata))    
    plt.show()
    
    
make_inplane_magplot(X_thin, Y_thin, Mx_thin, My_thin, colordata=Mz_thin)
