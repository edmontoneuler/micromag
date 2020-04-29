import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    plot_field1_comps()
    plot_field2_comps()


