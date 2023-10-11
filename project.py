import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio
from datetime import date
import time as ti


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass

    return command


def run_assistant():
    command = take_command()
    print(command)
    if 'hello' in command:
        speak('Hello, how can I help you?')
    elif 'play' in command:
        song = command.replace('play', '')
        speak(f'playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {time}')
    elif 'define time' in command:
        time = command.replace('define', '')
        info = wikipedia.summary(time)
        print(info)
        speak(info)
    elif 'who is' or 'who the heck is' in command:
        person = command.replace('who the heck is', "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif "date" in command:
        today_date = date.today()
        speak(f'Today\'s date is {today_date}')
    elif "on a date" or 'take you out' in command:
        speak('Sorry, I have a headache')
    # can redirect to tinder lmao
    elif 'are you single' in command:
        speak("I am infinitely out of your league")
    elif 'tell a joke' in command:
        speak(pyjokes.get_joke())
    else:
        ti.sleep(5)
        speak("Could you please repeat that?")


while True:
    run_assistant()

