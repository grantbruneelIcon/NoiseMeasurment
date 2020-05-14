import numpy.fft as fft
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Creates a frequency graph from the wav file name given
# This is used in All.py
def frequencyThis(name):
    freq, data = wavfile.read(name + ".wav")
    datafft = fft.fft(data)
    time = len(data) // freq
    newData = []
    for i in range(len(datafft) // 2):
        newData.append(datafft[i])

    plt.plot(newData)
    plt.xticks(range(0, len(newData), 1000 * time), range(0, len(newData) * time // 2, 1000))

    # Vertical line
    maxHZ = 1000
    plt.vlines(maxHZ * time, max(newData) * 1.1, min(newData) * 1.1, colors="red")

# This shows the frequuency plot alone. For use without the amplitude graph
def frequency():
    name = input("Name of file to graph amplitude: ")
    frequencyThis(name)
    plt.show()

