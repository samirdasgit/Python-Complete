import pyttsx3
from datetime import datetime

def timeGreeting():
  hour = datetime.now().hour
  if 5 <= hour < 12:
    return "Good Morning"
  elif 12 <= hour < 17:
    return "Good Afternoon"
  elif 17 <= hour < 21:
    return "Good Evening"
  else:
    return "Good Night"

yourName=input("Enter your name: ")
outputMessage=timeGreeting()," ",yourName
engine = pyttsx3.init()
engine.say(outputMessage)
engine.runAndWait()