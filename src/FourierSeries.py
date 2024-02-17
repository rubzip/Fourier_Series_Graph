import numpy as np
from matplotlib import pyplot as plt
import csv


def load_signal(filename):
    """
    Imports a signal from a TSV file.
    """
    with open(filename) as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        n = 0
        array = []
        for row in tsv_reader:
            if n > 0:
                array.append(int(row[0]) + 1j * int(row[1]))
            n += 1
        
        if array[0]!=array[-1]:
            array.append(array[0])
        
        v = np.array(array)
        mask = (np.zeros(v.shape)==0)
        mask[1:] = np.diff(v)!=0 # This mask filter consecutive repeated elements [0,0,0,1,1,0] -> [0,1,0]

        return v[mask]


def draw_signal(signal, fname, color):
    """
    Saves a drawing in fname path.
    """
    plt.figure(figsize = (8,6)) 
    plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False) 
    plt.plot(signal.real, -signal.imag, color=color)
    plt.savefig(fname)


class FourierSeries:
    def __init__(self, N: int, signal: np.array):
        """
        N degree Fourier Series.

        Parameters
        ----------
        N : int
            Fourier Series degree.
        signal : np.array
            Discretized signal in complex numbers. I'm considering the same time gap between each i and i+1 indexes. Shape (T, 1).
        """
        self.N = N
        self.signal = signal
        self.T = len(signal)

        self.coefs = 1j * np.zeros(2 * N + 1)
        for i in range(2 * N + 1):
            n = i - N
            arguments = -2j * np.pi * n * np.arange(self.T) / self.T
            self.coefs[i] = np.dot(signal, np.exp(arguments)) / self.T

        self.modules = np.absolute(self.coefs)

    def predict(self, time: np.array) -> np.array:
        """
        Takes an array of time and predicts the signal in each time.

        Parameters
        ----------
        time : np.array
            Array with time values. Shape (m, 1).

        Returns
        -------
        signal : np.array
            Returns the predicted signal (complex). Shape (m, 1).
        """
        m = len(time)
        signal = np.zeros(m) * 1j
        for i in range(m):
            arguments = (
                -2j * np.pi * (np.arange(2 * self.N + 1) - self.N) * time[i] / self.T
            )
            signal[i] = np.dot(self.coefs, np.exp(arguments))

        return signal

    def generate_animation(self, time: np.array):
        m = len(time)
        animation = np.zeros((m, self.N * 2 + 1)) * 1j
        for i in range(m):
            arguments = (
                -2j * np.pi* (np.arange(2 * self.N + 1) - self.N) * time[i] / self.T
            )
            animation[i, :] = self.coefs * np.exp(arguments)

        for j in range(self.N * 2):
            animation[:, j + 1] += animation[:, j]

        return animation