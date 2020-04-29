import numpy as np
import matplotlib.pyplot as plt

def get_sp3_data(filename):
    data = np.loadtxt(filename)
    L = data[:, 0]
    mx = data[:, 1]
    my = data[:, 2]
    mz = data[:, 3]
    E_total = data[:, 4]
    E_exc = data[:, 5]
    E_demag = data[:, 6]
    E_aniso = data[:, 7]

    return L, mx, my, mz, E_total, E_exc, E_demag, E_aniso

L_flower, mx_flower, my_flower, mz_flower, E_flower, E_exc_flower, E_demag_flower, E_aniso_flower = get_sp3_data('flower.txt')
L_twisted, mx_twisted, my_twisted, mz_twisted, E_twisted, E_exc_twisted, E_demag_twisted, E_aniso_twisted = get_sp3_data('twisted_flower.txt')
L_vortex, mx_vortex, my_vortex, mz_vortex, E_vortex, E_exc_vortex, E_demag_vortex, E_aniso_vortex = get_sp3_data('vortex.txt')

def plot_total_energies():
    """
    Total energy density of all three states, 
    with vertical lines to indicate ground state
    transitions. 
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('Average Energy Density')
    plt.title('Energy Density vs. System Size')
    plt.plot(L_flower, E_flower/L_flower**3, 'r')
    plt.plot(L_twisted, E_twisted/L_twisted**3, 'b')
    plt.plot(L_vortex, E_vortex/L_vortex**3, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.axvline(8.14, color='k')
    plt.axvline(8.47, color='k')
    plt.axvline(8.445, color='k', linestyle='--')
    plt.show()

def plot_exchange_energies():
    """
    Exchange energy densities of all three states
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('Average Exchange Energy Density')
    plt.title('Exchange Energy Density vs. System Size')
    plt.plot(L_flower, E_exc_flower/L_flower**3, 'r')
    plt.plot(L_twisted, E_exc_twisted/L_twisted**3, 'b')
    plt.plot(L_vortex, E_exc_vortex/L_vortex**3, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.show()


def plot_demag_energies():

    """
    Demag energy densities of all three states
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('Average Demag Energy Density')
    plt.title('Demag Energy Density vs. System Size')
    plt.plot(L_flower, E_demag_flower/L_flower**3, 'r')
    plt.plot(L_twisted, E_demag_twisted/L_twisted**3, 'b')
    plt.plot(L_vortex, E_demag_vortex/L_vortex**3, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.show()

def plot_aniso_energies():
    """
    Anistropy energy densities of all three states
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('Average Anisotropy Energy Density')
    plt.title('Anisotropy Energy Density vs. System Size')
    plt.plot(L_flower, E_aniso_flower/L_flower**3, 'r')
    plt.plot(L_twisted, E_aniso_twisted/L_twisted**3, 'b')
    plt.plot(L_vortex, E_aniso_vortex/L_vortex**3, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.show()

def plot_average_mz():
    """
    Average magnetization along z-axis for all three states. 
    This plot makes clear the transition between the flower
    and twisted-flower states. 
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('Mz')
    plt.title('Average Mz vs. System Size')
    plt.plot(L_flower, mz_flower, 'r')
    plt.plot(L_twisted, mz_twisted, 'b')
    plt.plot(L_vortex, mz_vortex, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.show()

def plot_average_my():    
    """
    Average magnetization along y-axis for all three states. 
    """
    plt.figure()
    plt.xlabel('L')
    plt.ylabel('M')
    plt.title('Average My vs. System Size')
    plt.plot(L_flower, my_flower, 'r')
    plt.plot(L_twisted, my_twisted, 'b--')
    plt.plot(L_vortex, my_vortex, 'g')
    plt.legend(['Flower', 'Twisted Flower', 'Vortex'])
    plt.show()

if __name__ == "__main__":
    plot_total_energies()
    #plot_exchange_energies()
    #plot_demag_energies()
    #plot_aniso_energies()
    #plot_average_mz()
    #plot_average_my()
