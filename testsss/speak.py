import pyttsx3
sound = pyttsx3.init()
sound.setProperty('rate',110)

sound.say(f"beelee ayeleyesh")
sound.runAndWait()
