import matplotlib.pyplot as plt
import numpy as np

def load_sp1_scalar_data(filename='field1_table.txt'):
    """
    Returns the spatially averaged magnetization 
    components, and the external field components, 
    as functions of time.
    """

    data = np.loadtxt(filename)

    t = data[:, 0]
    mx = data[:, 1]
    my = data[:, 2]
    mz = data[:, 3]
    Bx = data[:, 4]
    By  = data[:, 5]
    Bz  = data[:, 6]

    return t, mx, my, mz, Bx, By, Bz

def load_sp1_spatial_data(filename='xfield_sat.csv', thinning=16):

    """
    Loads a snapshot of the magnetization of the Standard Problem 1 sample.
    This data is then 'thinned out' so that an intelligible vector plot 
    of the in-plane magnetization can be made. 
    """

    data = np.loadtxt(filename, delimiter = ',')
    triple_Ny, Nx = np.shape(data) # Number of points along X and Y directions
    Ny = int(triple_Ny/3)

    Mx = data[0:Ny, :]
    My = data[Ny:2*Ny, :]
    Mz = data[2*Ny:3*Ny, :]

    # Geometry of x and y grids is specific to SP1
    x_vec = np.linspace(0, 2e-6, Nx)
    y_vec = np.linspace(0, 1e-6, Ny)
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
    #I = plt.imshow(Mz,extent=[np.min(X),np.max(X),np.min(Y),np.max(Y)])
    Q = plt.quiver(X,Y,Mx,My)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    #cbar = plt.colorbar(orientation='horizontal')
    #cbar.set_label('Mz')
    #plt.clim(np.min(Mz), np.max(Mz))    


def plot_xfield_hysteresis():

    t, Mx, My, Mz, Bx_ext, By_ext, Bz_ext = load_sp1_scalar_data('xfield_sweep_table.txt')
    
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

def plot_yfield_hysteresis():

    t, Mx, My, Mz, Bx_ext, By_ext, Bz_ext = load_sp1_scalar_data('yfield_sweep_table.txt')
    
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

def plot_xfield_initial_mag():
    """
    Plots magnetic state prior to the start of the
    hysteresis loop
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('xfield_initial.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Initial Magnetization')
    plt.show()

def plot_xfield_sat_plus():
    
    """
    Plots the magnetization of the sample at its most saturated along
    the positive x-axis, i.e at maximum field.
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('xfield_sat_plus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Near-Saturation')
    plt.show()

def plot_xfield_zero_plus():
    """
    Plots the magnetization of the sample at zero field, after having 
    been magnetized along the postive x-axis. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('xfield_zero_plus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Zero Field')
    plt.show()

def plot_xfield_sat_minus():
    """
    Plots the magnetization at its most saturated along the
    negative x-axis, i.e when the field is at its most negative. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('xfield_sat_minus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Near-Saturation')
    plt.show()

def plot_xfield_zero_minus():
    """
    Plots the magnetization at zero field, after having been saturated 
    along the negative x-axis. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('xfield_zero_minus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Zero Field')
    plt.show()

def plot_yfield_initial():
    """
    Plots magnetic state prior to the start of the
    hysteresis loop
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('yfield_initial.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Initial Magnetization')
    plt.show()

def plot_yfield_sat_plus():
    
    """
    Plots the magnetization of the sample at its most saturated along
    the positive y-axis, i.e at maximum field.
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('yfield_sat_plus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Near-Saturation')
    plt.show()

def plot_yfield_zero_plus():
    """
    Plots the magnetization of the sample at zero field, after having 
    been magnetized along the postive y-axis. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('yfield_zero_plus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Zero Field')
    plt.show()

def plot_yfield_sat_minus():
    """
    Plots the magnetization at its most saturated along the
    negative y-axis, i.e when the field is at its most negative. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('yfield_sat_minus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Near-Saturation')
    plt.show()

def plot_yfield_zero_minus():
    """
    Plots the magnetization at zero field, after having been saturated 
    along the negative y-axis. 
    """
    X, Y, Mx, My, Mz = load_sp1_spatial_data('yfield_zero_minus.csv')
    make_inplane_magplot(X, Y, Mx, My, Mz)
    plt.title('Magnetization at Zero Field')
    plt.show()


if __name__ == "__main__":
    plot_xfield_hysteresis()
    plot_yfield_hysteresis()

    #plot_xfield_sat_plus()
    #plot_xfield_zero_plus()
    #plot_xfield_sat_minus()
    #plot_xfield_zero_minus()
        
    #plot_yfield_sat_plus()
    #plot_yfield_zero_plus()
    #plot_yfield_sat_minus()
    #plot_yfield_zero_minus()
