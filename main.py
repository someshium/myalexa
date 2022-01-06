import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(command):
    engine.say(command)
    engine.runAndWait()

def hear():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                    finalcommand = command.replace('alexa','')
                    print(finalcommand)

    except:
        pass

    return finalcommand

def run_alexa():
   command =  hear()
   if 'play' in command:
       song= command.replace('play','')
       talk('playing'+song)
       pywhatkit.playonyt(song)

   if 'time' in command:
       time = datetime.datetime.now().strftime('%I:%M %p')
       talk(time)

   elif 'tell me about' in command:
       command = command.replace('tell me about','')
       info = wikipedia.summary(command,1)
       print(info)
       talk(info)

   elif 'Who is your boss' in command:
       talk('I am the boss')

   elif 'who is ur friend' in command:
       talk('Its one and only somesh')

   elif 'open' in command:
       command = command.replace('open','')
       if 'chrome' in command:
           os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
       elif 'brave' in command:
           os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
       elif 'vs code' in command:
           os.startfile('C:/Users/somes/AppData/Local/Programs/Microsoft VS Code/Code.exe')
       elif 'notepad' in command:
           os.system('notepad')


while True:
    run_alexa()


