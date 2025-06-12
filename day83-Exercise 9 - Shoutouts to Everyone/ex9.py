import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Vaibhav", "Raj",  "Samay"]

for name in names:
  text = f"Shoutout to {name}"
  speaker.Speak(text)
