import sympy
import numpy as np
import matplotlib.pyplot as plt


class TimeDelay:
    def __init__(self, tau):
        self.t = np.linspace(0, 10, 1000)
        self.x = np.sin(self.t)
        self.y = np.sin(self.t) * np.cos(tau) + np.cos(self.t) * np.sin(tau)
        self.tau = tau

    def plot(self):
        plt.plot(self.x, self.y)
        plt.xlabel(f'$x(t)$')
        plt.ylabel(f'$x(t+{self.tau})$')
        plt.xlim([-1.5, 1.5])
        plt.ylim([-1.5, 1.5])
        plt.show()

if __name__ == '__main__':
    TimeDelay(np.pi/6).plot()
