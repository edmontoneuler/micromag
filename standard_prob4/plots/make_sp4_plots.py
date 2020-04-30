import matplotlib.pyplot as plt
import numpy as np

def load_sp4_scalar_data(filename='field1_table.txt'):
    """
    Returns the spatially averaged magnetization 
    components as functions of time
    """

    data = np.loadtxt(filename)

    t = data[:, 0]
    mx = data[:, 1]
    my = data[:, 2]
    mz = data[:, 3]

    return t, mx, my, mz

def load_sp4_spatial_data(filename='field1_spatial_mag_data.csv', thinning=5):

    """
    Loads a snapshot of the magnetization of the Standard Problem 4 sample
    at the moment that its average magnetization along the x-axis switches
    sign, i.e at reversal. 
    This data is then 'thinned out' so that an intelligible vector plot 
    of the in-plane magnetization can be made. 
    """

    data = np.loadtxt(filename, delimiter = ',')
    triple_Ny, Nx = np.shape(data) # Number of points along X and Y directions
    Ny = int(triple_Ny/3)

    Mx = data[0:Ny, :]
    My = data[Ny:2*Ny, :]
    Mz = data[2*Ny:3*Ny, :]

    # Geometry of x and y grids is specific to SP4
    x_vec = np.linspace(0, 500e-9, Nx)
    y_vec = np.linspace(0, 125e-9, Ny)
    X, Y = np.meshgrid(x_vec, y_vec)


    n = thinning # Keep every n-th point
    X_thin = X[::n, ::n]
    Y_thin = Y[::n, ::n]
    Mx_thin = Mx[::n, ::n]
    My_thin = My[::n, ::n]
    Mz_thin = Mz[::n, ::n]

    return X_thin, Y_thin, Mx_thin, My_thin, Mz_thin

def make_inplane_magplot(X, Y, Mx, My,Mz):
    """
    Creates a vector plot of the x and y components of the magnetization, 
    and uses color to encode the z-component. 
    Assumes a thin film geometry, such that these quantities are defined 
    on 2D grids. 
    """
    fig = plt.figure()
    I = plt.imshow(Mz,extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)])
    Q = plt.quiver(X,Y,Mx,My)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    cbar = plt.colorbar(orientation='horizontal')
    cbar.set_label('Mz')
    plt.clim(np.min(Mz), np.max(Mz))    
    
def plot_field1_comps():

    t, mx, my, mz = load_sp4_scalar_data('field1_table.txt')

    plt.figure()
    plt.plot(t, mx, 'r')
    plt.plot(t, my, 'g')
    plt.plot(t, mz, 'b')
    plt.legend(['Mx', 'My', 'Mz'])

    #External Field Unit Vector
    plt.axhline(-0.985964, color = 'r', linestyle = '--')
    plt.axhline(0.172186, color = 'g', linestyle = '--')
    plt.axhline(0, color = 'b', linestyle = '--')

    plt.xlabel('Time (s)')
    plt.ylabel('M/Ms')
    plt.title('Average Magnetization Components')
    plt.show()

def plot_field2_comps():

    t, mx, my, mz = load_sp4_scalar_data('field2_table.txt')

    plt.figure()
    plt.plot(t, mx, 'r')
    plt.plot(t, my, 'g')
    plt.plot(t, mz, 'b')
    plt.legend(['Mx', 'My', 'Mz'])

    #External Field Unit Vector
    plt.axhline(-0.985964, color = 'r', linestyle = '--')
    plt.axhline(-0.172186, color = 'g', linestyle = '--')
    plt.axhline(0, color = 'b', linestyle = '--')

    plt.xlabel('Time (s)')
    plt.ylabel('M/Ms')
    plt.title('Average Magnetization Components')
    plt.show()

def plot_field1_spatial_mag():
    X, Y, Mx, My, Mz = load_sp4_spatial_data('field1_spatial_mag_data.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Reversal: Field 1')
    plt.show()

def plot_field2_spatial_mag():
    X, Y, Mx, My, Mz = load_sp4_spatial_data('field2_spatial_mag_data.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Reversal: Field 2')
    plt.show()


if __name__ == "__main__":
    plot_field1_comps()
    plot_field2_comps()
    plot_field1_spatial_mag()
    plot_field2_spatial_mag()
