from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="This is the first project of mine",lang=language,slow=False)
sp.save(audio)
playsound(audio)  
print("Audio Just Played")
