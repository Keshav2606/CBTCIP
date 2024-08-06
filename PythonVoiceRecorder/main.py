import sounddevice as sd;
from wavio import write;

frequency = 48000;

duration = int(input("Enter the duration of recording: "))

recording = sd.rec(frequency * duration, frequency, channels=2)

sd.wait()

try:
    with open("recording_count.txt", mode='r') as file:
        count = int(file.readline())
except:
    count = 0;
finally:
    with open("recording_count.txt", mode='w') as file:
        count += 1
        file.write(str(count))


write(f"recording{count}.wav", recording, frequency, sampwidth=2)

