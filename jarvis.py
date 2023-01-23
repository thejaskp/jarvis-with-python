import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init()
voice = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voice[0].id)  # NOQA


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# convert voice into text
def takecommand():  # NOQA
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=6)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')  # NOQA
        print(f"you said: {query}")

    except Exception as e:
        speak("Say that again please, sir...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good morning captain...")
    elif 12 <= hour < 18:
        speak("good afternoon captain...")
    else:
        speak("good evening captain...")
    speak("I am jarvis, tell me how can I help you ")


# to send mail
def sendEmail(to, content):  # NOQA
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<mail>@gmail.com', '<password>')
    server.sendmail('<your email>', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    # if 1:
    while True:

        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"  # NOQA
            os.startfile(npath)

        elif "open movies" in query:
            mpath = "D:\\media\\movies\\Movies"
            os.startfile(mpath)

        elif "play" and "random movie" in query:
            mpath = "D:\\media\\movies\\Movies"
            movies = os.listdir(mpath)
            nos = 0
            for root_dir, cur_dir, files in os.walk(r'D:\\media\\movies\\Movies'):
                nos += len(files)
            num = random.randint(0, nos - 1)
            os.startfile(os.path.join(mpath, movies[num]))

        elif " open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)  # NOQA
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)  # NOQA
                k = cv2.waitKey(50)  # NOQA
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()  # NOQA

        elif "play" and "music" in query:
            music_dir = "C:\\Users\\ASUS\\Music"
            songs = os.listdir(music_dir)

            nos = 0
            for root_dir, cur_dir, files in os.walk(r'C:\\Users\\ASUS\\Music'):
                nos += len(files)
            num = random.randint(0, nos - 1)
            os.startfile(os.path.join(music_dir, songs[num]))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "ip location" in query:
            ip = get("https://api.ipify.org").text
            ipl = get(f"http://www.geoplugin.net/json.gp?ip={ip}")
            speak(f"your location is {ipl}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia" + results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("What should I search, sir...")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            speak("To whom, sir...")
            name = takecommand().lower().replace(" ", "")
            if name == 'amma':
                name = "<number>"
            elif name == 'anagha':
                name = "<number>"
            elif name == 'ananthu':
                name = "<number>"
            elif name == 'zidan':
                name = "<number>"
            speak("What is the message, sir...")
            msg = takecommand().lower()
            speak("in which hour, sir...")
            hour = int(takecommand().lower())
            speak("minute?...")
            minute = int(takecommand().lower())
            kit.sendwhatmsg(f"+91{name}", f"{msg}", hour, minute, 15, True, 5)

        elif "play song on youtube" in query:
            speak("What do you like to hear, sir...")
            song_name = takecommand().lower()
            kit.playonyt(f"{song_name}")

        elif "play" and "on youtube" in query:
            song_name = query.split("on youtube")[0].split("play")[1]
            kit.playonyt(f"{song_name}")

        elif "send email" in query:
            try:
                speak("to whom sir...")
                to = takecommand().lower().replace(" ", "")
                speak("what should I send?")
                content = takecommand().lower()
                sendEmail(to, content)
                speak(f"Email has been sent to {to}")

            except Exception as e:
                print(e)
                speak("an error has been occurred")

        elif "what" and "time" and "now" in query:
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            second = int(datetime.datetime.now().second)
            if hour < 12:
                ext = "AM"
            ext = "PM"
            if hour > 12:
                hour = hour - 12
            speak(f"It is now {hour} {ext}, {minute} minutes and {second} seconds, captain...")

        elif 'no thanks' or 'back off' or 'shut up' in query:
            speak("see you soon Captain, have a good day")
            sys.exit()

        speak("Captain, do you have any other work")
