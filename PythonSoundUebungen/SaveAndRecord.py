import sounddevice as sd
from scipy.io.wavfile import write

duration = 5
fs = 44100
sd.default.samplerate = fs  
sd.default.channels = 1

#Recording Audio

print("Do you want to record an Audio?")
inp1 = input("Yes or No: ")
if(inp1.lower() == "yes"):
    print("Recording for 5 seconds...")
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
else:
    exit()

#Saving Audio

print("Do you want to save your Audio?")
inp2 = input("Yes or No: ")
if(inp2.lower() == "yes"):
    print("Name your Audio: ")
    inp3 = input()
    soundname = inp3
    write(soundname + ".mp3", fs, myrecording)