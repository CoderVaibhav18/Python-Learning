# import pyttsx3

# names = ["Vaibhav", "Raj",  "Samay"]
# engine = pyttsx3.init()  

# for name in names:
#   engine.say(f"Shoutout to {name}")  
#   engine.runAndWait()  
  
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Vaibhav", "Raj",  "Samay"]

for name in names:
  text = f"Shoutout to {name}"
  speaker.Speak(text)
