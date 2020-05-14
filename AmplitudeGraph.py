from scipy.io import wavfile
import math as m
import matplotlib.pyplot as plt

# Creates the graph of the wav file
# Used in All.py
def graphThis(name):
    sample, data = wavfile.read(name + ".wav")
    newData = []
    for i in range(500, len(data)):
        if data[i] != 0:
            newData.append(10 * m.log10(abs(data[i] / (10 ** -8.5))))

    p1 = plt.plot(newData)

    # ......  Horizontal Line  ...........
    length = len(newData)
    plt.hlines(80, -length * 0.1, length * 1.1, 'red')
    return p1

# Returns the graph already made with the red Horizontal line.
def graph():
    name = input("File to name to display: ")
    return graphThis(name)



