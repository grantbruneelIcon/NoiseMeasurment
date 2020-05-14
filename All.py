import Record as rec
import AmplitudeGraph as amp
import Frequency as freq
import matplotlib.pyplot as plt

# Record and save a graph of sound
# show is whether or not to display the graph after recording
def record_and_graph(show=False):
    name = input("Name to save files as: ")
    time = input("Time of sample to take in seconds: ")
    rec.recordThis(name, int(time))

    plt.subplot(211)
    plt.title("Decibel Level")
    amp.graphThis(name)

    plt.subplot(212)
    plt.title("Frequency Graph")
    freq.frequencyThis(name)

    plt.tight_layout()
    save(name)
    if show:
        plt.show()

# Creates a graph from an already existing wav file
def no_record(show=False):
    name = input("Name of file to read: ")

    plt.subplot(211)
    plt.title("Decibel Level")
    amp.graphThis(name)

    plt.subplot(212)
    plt.title("Frequency Graph")
    freq.frequencyThis(name)

    plt.tight_layout()
    save(name)
    if show:
        plt.show()

# Saves the figure as name.png
def save(name):
    plt.savefig(name + ".png")

