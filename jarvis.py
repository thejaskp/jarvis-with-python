import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2

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
        speak("Say that again please, sir...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir...")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir...")
    else:
        speak("good evening sir...")
    speak("I am jarvis, sir tell me how can I help you ")


if __name__ == "__main__":
    wish()
    # while True:
    if 1:

        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open movies" in query:
            mpath = "D:\\media\\movies"
            os.startfile(mpath)

        elif " open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
