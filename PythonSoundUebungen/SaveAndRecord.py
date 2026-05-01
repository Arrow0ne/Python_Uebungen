import sounddevice as sd
import numpy as np
from pydub import AudioSegment

duration = 5
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1

# Recording Audio
print("Do you want to record an Audio?")
inp1 = input("Yes or No: ")
if inp1.lower() == "yes":
    print("Recording for 5 seconds...")
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
else:
    exit()

# Saving Audio
print("Do you want to save your Audio?")
inp2 = input("Yes or No: ")
if inp2.lower() == "yes":
    print("Name your Audio: ")
    soundname = input()

    # Convert to 16-bit and export as real MP3
    audio_int16 = (myrecording * 32767).astype(np.int16)
    audio_segment = AudioSegment(
        audio_int16.tobytes(),
        frame_rate=fs,
        sample_width=2,
        channels=1
    )
    audio_segment.export(soundname + ".mp3", format="mp3")
    print(f"Saved as {soundname}.mp3")
else:
    exit()