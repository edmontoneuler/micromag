import numpy as np
import matplotlib.pyplot as plt

def load_sp2_data(filename = 'table.txt'):


    data = np.loadtxt('table.txt')

    d_ratio = data[:, 0]
    mx_remnant = data[:, 1]
    my_remnant = data[:, 2]
    coercivity = data[:, 3]

    return d_ratio, mx_remnant, my_remnant, coercivity

d_ratio, mx_remnant, my_remnant, coercivity = load_sp2_data()

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

def plot_remnant_xmag():
    """
    Plots the remnant magnetization along the x-axis
    as a function of system size. 
    """
    plt.figure()
    plt.plot(d_ratio, mx_remnant, 'ko')
    plt.xlabel(r'$d/l_{ex}$', fontsize = 20)
    plt.ylabel(r'$M_{rx}/M_s$', fontsize = 20)
    plt.title(r'Remnant magnetization along $x$', fontsize=25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.show()

def plot_remnant_ymag():
    """
    Plots the remnant magnetization along the y-axis
    as a function of system size
    """
    plt.figure()
    plt.plot(d_ratio, my_remnant, 'ko')
    plt.xlabel(r'$d/l_{ex}$', fontsize = 20)
    plt.ylabel(r'$M_{ry}/M_s$', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Remnant magnetization along $y$', fontsize =25)
    plt.show()

def plot_coercivity():
    """
    Plots the coercivity of the SP2 geometry to 
    applied fields along the [111] direction. 
    """
    plt.figure()
    plt.plot(d_ratio, coercivity, 'ko')
    plt.xlabel(r'$d/l_{ex}$', fontsize = 20)
    plt.ylabel(r'$|H_c|/M_s$', fontsize = 20)
    plt.ylim(0.04, 0.07)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Coercivity', fontsize =25)
    plt.show()

if __name__ == "__main__":
    plot_remnant_xmag()
    plot_remnant_ymag()
    plot_coercivity()
