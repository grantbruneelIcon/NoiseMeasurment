# Noise Measurement
Written by Grant Bruneel 
Last Edit 4/2/2020 by Grant Bruneel

Required Libraries:
-matplotlib
-sounddevice
-scipy
-playsound

Functions:
Most all useful functions have been written in All.py

1.  record_and_graph(show)
This will ask for a name and time to record the sound of the current microphone of the computer. A sound recording and graph of the
decibel and frequency level's are created.

 -Inputs:
boolean show; the default is False and the graph will not show after the graph is saved. True will pop up a window showing the graph

 -Termninal input:
Name to save the sound and graph files
Time in seconds to take the sample (The recording starts right after this is entered)

 -Outputs:
wav file recording of the sound
png file of the graph

2. no_record(show)
This allows you to choose a already recorded wav file to create a graph. To do this save the file in this folder and run this function.
** Note ** the decibel reading may be different as the setup is based on the microphone with the lenovo

 -Inputs:
boolean show; the default is False and the graph will not show after the graph is saved. True will pop up a window showing the graph

 -Terminal input:
Name of the sound file to be produced in a graph

 -Outputs:
png file of the sound graph

*Disclaimer*
 
The decibel levels are not exact but give a good estimate of how loud the sound recorded is. 
The frequency readings are also a good estimate, not exact.
