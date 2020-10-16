from pyttsx3 import *
import webbrowser
from PyDictionary import PyDictionary
import wikipedia
import webbrowser
import random 
import os
import time
import psutil
import platform

#URLs for websites to open:
netflix = "https://www.google.com/search?q=netflix&"
music = "https://music.amazon.in/home"
news = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
youtube = "https://w/ww.youtube.com/"
github = "https://github.com/settings/profile"
amazon = "https://www.amazon.in/"
swiggy = "https://www.swiggy.com/"

os.system("clear")

x=0
cu_time = time.localtime(time.time())
converter = init()

converter.setProperty('rate', 170) 
converter.setProperty('volume', 2.0)
cur_time = time.localtime(time.time())

if cur_time[3] >= 0 and cur_time[3] < 12:
    converter.say("Good Morning Sir")
    converter.runAndWait()

elif cur_time[3] >= 12 and cur_time[3] < 18 or ((cu_time[4] > 0 and cu_time[4] < 59) and cur_time[3] == 18):
    converter.say("Good Afternoon Sir")
    converter.runAndWait()

elif cur_time[3] > 18 or ((cu_time[4] > 0 and cu_time[4] < 59) and cur_time[3] == 18):
    converter.say("Good Evening Sir")
    converter.runAndWait()
converter.say("What would you like me to do?")
converter.runAndWait()
data = input("OLIVER:What would you like me to do?\n")

while True:
    if "music" in data:
        converter.say("Oppening music")
        converter.runAndWait()
        print("Oppening music")

        time.sleep(0.5)
        os.system("open Msuic")

    elif "news" in data:
        converter.say("Here are the top stories.")
        converter.runAndWait()
        print("Here are the top stories.")

        time.sleep(0.5)
        webbrowser.open(news)

    elif "youtube" in data:
        converter.say("Oppening youtube.")
        convertor.runAndWait()
        print("Oppening youtube.")

        webbrowser.open(netflix)

    elif "netflix" in data:
        converter.say("Oppening Netflix.")
        converter.runAndWait()
        print("Oppening Netflix.")

        webbrowser.open(netflix)

    elif "github" in data:
        converter.say("Oppneing Github")
        converter.runAndWait()
        print("Oppening Github")

        webbrowser.open(github)
    
    elif "shop" in data:
        converter.say("oppening amazon")
        converter.runAndWait()
        print("Oppening Amazon")

        webbrowser.open(amazon)
    
    elif "atom" in data:
        converter.say("oppening atom.I.O")
        converter.runAndWait()
        print("Oppening Atom.I.O")

        os.system("atom")

    elif "food" in data:
        converter.say("oppening swiggy")
        converter.runAndWait()
        print("Oppening Swiggy.")

        webbrowser.open(swiggy)

    else:
        converter.say("i do not know that")
        converter.runAndWait()
        print("ULTRON:I do not know that.")
