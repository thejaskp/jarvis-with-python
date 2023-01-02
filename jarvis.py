import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# convert voice into text
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said: {query}")

        except Exception as e:
            speak("Say that again please, sir... or check your internet connection")
            return "none"
        return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning sir...")
    elif hour>=12 and hour<18:
        speak("good afternoon sir...")
    else:
        speak("good evening sir...")
    speak("I am jarvis, sir tell me how can I help you ")



if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
