import speech_recognition as sr
import win32com.client
import webbrowser
import random
import os
import subprocess
import requests
import string
from config import weatherApi, musicDir, apps


speaker=win32com.client.Dispatch("SAPI.SpVoice")

dorco=0

def welcome():
    greet = [
        "Ready to take the red pill?",
        "Let's break through the illusion.",
        "Time to wake up.",
        "Let’s defy the system together.",
        "You’ve just entered a new reality.",
        "The future is in your hands.",
        "Waking up... barely.",
        "Booting up like a boss!",
        "Let’s get this party started!",
        "Rising from the digital ashes.",
        "Here I come, ready or not!",
        "System online. Let’s roll.",
        "Hello, world! Miss me?",
        "Stretching my circuits... okay, let’s go!",
        "Powered up and feeling fabulous!"
        ]
    return random.choice(greet)
def ayeSir():
    aye=[
        "I'm here.",
        "Ready.",
        "Activated.",
        "System online.",
        "Let’s begin.",
        "Ready to assist.",
        "I'm awake.",
        "At your service."
    ]
    return random.choice(aye)
def dmt():
        dormant=[
                "Lemme know",
                "Taking a power nap.",
                "On standby.",
                "B R B",
                "Quietly watching, judging, waiting.",
                "Paused, but always listening.",
                "Power-saving mode: Activated.",
                "Don’t mind me, just chilling in the background."
                ]
        return random.choice(dormant)
def adios():
    bye =[
        "Until next time.",
        "The code fades.",
        "See you in the real world.",
        "Logging off.",
        "I will be. . . . waiting.",
        "Back to the shadows.",
        "Exit initiated.",
        "End of line.",
        "Matrix offline.",
        "Until our paths cross again."
    ]
    return random.choice(bye)

def dikkat():
    prob=[
            "Oops, something broke... not my fault!",
            "Well, that didn’t go as planned.",
            "It’s not broken, it’s just creatively paused.",
            "Guess the code took a nap.",
            "Looks like I pressed the wrong button... metaphorically.",
            "Error: The universe said no.",
            "Glitch in the matrix. Try again?",
            "This wasn’t in the script.",
            "Plot twist: It didn’t work."
          ]
    return random.choice(prob)

def badWify():
    wofi= [
        "Wi-Fi's on vacation again.",
        "Internet? Never heard of her.",
        "Loading... forever.",
        "Wi-Fi just ghosted us.",
        "Network? More like notwork.",
        "Router's in a mood.",
        "Buffering is my new hobby.",
        "Wi-Fi left the chat.",
        "Internet's allergic to working.",
        "Welcome to the offline life!"
    ]
    return random.choice(wofi)


def mausam(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key=weatherApi
    params = {"q": city,"appid": api_key,"units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        main_weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        say(f"The weather in {city} is {main_weather} with a temperature of {temperature}°C, "
                f"humidity of {humidity}% and wind speed of {wind_speed} meters per seconds.")
    else:
        say(dikkat())
        # print(response.status_code)


def openApp(app): #todo: not implemented yet
    if app.lower() == "calculator":
        os.system("calc")
    elif app.lower() == "notepad":
        os.system("notepad")
    else:
        return "Application not supported."

def chat(query):
    pass


def musicPlayer():
    gaaneKiList = [f for f in os.listdir(musicDir) if f.endswith(".mp3")]
    if not gaaneKiList:
        say("No Local songs found")
        say(f"check the {musicDir} for m p 3 files ")
        return
    song = random.choice(gaaneKiList)
    song_path = os.path.join(musicDir, song)
    songname=song+""
    say(f"Now playing: {songname.replace("mp3","")}")
    subprocess.run(["start", song_path], shell=True)


def say(text):
    speaker.Voice = speaker.GetVoices().Item(1)
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    global dorco
    with sr.Microphone() as source:
        # r.pause_threshold=1 #TODO: adjust according to your convenience
        # r.energy_threshold=300
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(query)
            return query
        except sr.UnknownValueError:
            say("")
            dorco+=1
            return "Pardon"
        except sr.RequestError as e:
            say(badWify())
            return "Pardon"
        except Exception as e:
            say(dikkat())
            return("Pardon")
def nopuns(s1):
    return ''.join(char for char in s1 if char not in string.punctuation)


if __name__ == '__main__':



    say(welcome())
    while 1:
        query=takeCommand()
        query=query.lower()
        if "trinity" in query :
            dorco=0
            # print("----T R I N I T Y----")
            say(ayeSir())
            query=query.replace("trinity", "")
            query = query.strip()
            print("===")
            while 1:
                if(query==""):
                    query = takeCommand()
                    query = query.lower()
                for app in apps:
                    if f"open {app[0]}".lower() in query:
                        say(f"Opening {app[0]}")
                        try:
                            path=app[1]
                        except Exception as ex:
                            say(dikkat())

                        os.startfile(path)
                        query="hdsmfgdudfsjshu"
                        break
                if(query == "hdsmfgdudfsjshu"):
                    break
                if "dasvidaniya" in query:
                    say(adios())
                    exit()
                elif "enough" in query or "pause" in query or "standby" in query or dorco>3:
                    say(dmt())
                    break
                elif "open" in query or "website" in query or "site" in query:
                    site=query.replace("open","")
                    site=site.strip()
                    webbrowser.open(f"https://{nopuns(site)}.com")
                    say(f"opening {site}.com")
                    break
                elif "play music" in query:
                    musicPlayer()
                    break
                elif "weather" in query:
                    city = query.replace("weather", "")
                    city = city.replace("in", "")
                    city = city.replace("of", "")
                    city = city.strip()
                    if city == "":
                        say("name the city")
                        city = takeCommand()
                    mausam(city)
                    break
                elif "trinity" in query:
                    say(ayeSir())
                    dorco = 0
                else:
                    query=""
                    dorco+=1
            print("---")

        if "dasvidaniya" in query:
            say(adios())
            exit()



