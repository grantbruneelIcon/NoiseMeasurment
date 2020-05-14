import playsound as ps

# Plays the sound from the wave file
# Nothing special really
def main():
    name = input("name of file to play: ")
    ps.playsound(name + '.wav')
