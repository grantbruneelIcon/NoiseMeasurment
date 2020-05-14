import sounddevice as sd
from scipy.io.wavfile import write

# To record without doing any graphing, use this
def record():
    time = int(input("Time in seconds to record: "))
    fileName = input("Name to save the recording as: ")
    recordThis(fileName, time)

# This is used in the All.py 
# Records and saves a file for time seconds as fileName.wav
def recordThis(fileName, time):
    # defaults
    rate = 22100
    frame = time * rate

    sound = sd.rec(frame, rate, 1)
    print("Recording...")
    sd.wait()
    print("Recording done")
    write(fileName + ".wav", rate, sound)
    print("File saved as: " + fileName + ".wav")
