import subprocess
import wolframalpha
import pyttsx3
import pywhatkit
import json
import speech_recognition as sr
from PyDictionary import PyDictionary
import datetime
import wikipedia
import speedtest
import webbrowser
import os
import randfacts
import pyjokes
import ctypes
import time
import requests
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak("I am lara, your virtual assistant")


def usrname():
    speak("Welcome")
    speak("How can i Help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query


def getThing(query):
    wordList = query.split()  # splits the text to words

    for j in range(0, len(wordList)):
        if j + 3 <= len(wordList) - 1 and wordList[j].lower() == 'what' and wordList[j + 1].lower() == 'is':
            return wordList[j + 2] + ' ' + wordList[j + 3]


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any 
    # command before execution of this python file 
    clear()
    wishMe()
    usrname()

    while True:
        query = takeCommand().lower()

        # All the commands said by user will be 
        # stored here in 'query' and will be 
        # converted to lower case for easily 
        # recognition of command 
        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'join a meeting' in query:
            speak('alright enter your meeting code')
            a = input("Alright enter your meeting code:")
            speak('alright opening google meet')
            webbrowser.open('https://meet.google.com/' + a)

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("thats great to hear")

        elif 'where am i' in query:
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            a = data['city']
            b = data['region']
            print(a, b)
            speak('you are currently in' + ' ' + a + ' ' + b)

        elif 'what is' in query or "what's" in query:
            if 'time' in query:
                t = time.localtime()
                current_time = time.strftime("%I:%M %p", t)
                response = 'the current time is ' + current_time

            elif 'date' in query:
                mydate = datetime.datetime.now()
                a = mydate.strftime("%B")
                b = mydate.strftime("%d")
                c = mydate.strftime("%Y")
                print("Today is", b, "of", a, c)
                speak("Today is " + b + " of " + a + c)

            elif 'news' in query:

                try:
                    jsonObj = urlopen(
                        '''http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=5bad7ddd7071437cbc2ab53a97dd7584''')
                    data = json.load(jsonObj)
                    i = 1

                    print("Here are some top news from the Google News India")
                    speak('here are some top news from the Google News India')
                    print('''========================= Google News India ======================''' + '\n')

                    for item in data['articles']:

                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                        if i == 6:
                            break
                        else:
                            continue
                except Exception as e:

                    print(str(e))

            elif 'meaning of the word' in query:
                word = query.replace('what is the meaning of the word', "")
                dictionary = PyDictionary()
                print(dictionary.meaning(word))
                speak(dictionary.meaning(word))

            elif "your name" in query:
                print("My name is Lara and I am at your service")
                speak("My name is Lara and I am at your service")

            elif "is my location" in query:
                res = requests.get('https://ipinfo.io/')
                data = res.json()
                a = data['city']
                b = data['region']
                print(a, b)
                speak('you are currently in' + ' ' + a + ' ' + b)

            elif "current weather" in query or "weather" in query:
                api_key = "f1d85dd9243dda66f4afefab98323879"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                res = requests.get('https://ipinfo.io/')
                data = res.json()
                a = data['city']
                city_name = a
                complete_url = base_url + "q=" + city_name + "&appid=" + api_key
                response = requests.get(complete_url)
                x = response.json()

                if response.status_code == 200:
                    main = x["main"]
                    current_temperature = main["temp"]
                    celsius = int(current_temperature - 273.15)
                    current_pressure = main["pressure"]
                    current_humidiy = main["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in degree celsius) = " + str(
                        celsius) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                    speak('the temperature in' + ' ' + city_name + ' ' + 'is' + ' ' + str(celsius) + 'degree celsius')
                    speak('you will be having' + ' ' + str(weather_description) + ' ' + 'in' + ' ' + a)

                else:
                    speak(" City Not Found ")

            else:
                thing = getThing(query)
                wiki = wikipedia.summary(thing, sentences=2)
                print(wiki)
                speak(wiki)


        elif 'exit' in query or 'you can leave' in query:
            print("See ya later😊")
            speak("See ya later")
            break

        elif "who made you" in query or "who created you" in query:
            print("I was designed by a group of young intelligent students.")
            speak("I was designed by a group of young intelligent students.")

        elif 'play song' in query or 'play song' in query:
            a = query.replace('play song', "")
            print("Playing music ", a, "from youtube")
            speak('playing music' + ' ' + a + ' ' + 'from youtube')
            pywhatkit.playonyt(a)

        elif 'joke' in query:
            speak("Alright, here's one")
            z = pyjokes.get_joke()
            print(z)
            speak(z)

        elif 'search' in query:
            v = query.replace('search', "")
            speak("Searching your queries on google")
            print("Searching...")
            pywhatkit.search(v)


        elif "why do you exist" in query:
            print("I exist because to assist human beings in every aspect")
            speak("I exist because to assist human beings in every aspect")

        elif "who are you" in query:
            print("I am just like you, without a physical body")
            speak("I am just like you, without a physical body")

        elif "who am i" in query:
            print("If you talk then definitely you are a human.")
            speak("If you talk then definitely you are a human.")

        elif "bmi" in query:
            speak("To calculate your B M I, please provide your height in metres")
            print("Height(in metres):")
            Height = float(takeCommand())
            speak("please provide your weight in kilograms")
            print("weight(in kilograms):")
            weight = int(takeCommand())
            BMI = int(weight / Height ** 2)
            speak("Your bmi is:" + str(BMI))
            if BMI <= 18:
                speak("You are underweight, so try to eat more and stay healthy")
            elif BMI > 18 and BMI <= 25:
                speak("You are normal, Good job")
            elif BMI > 25 and BMI <= 30:
                speak("You are overweight")
            elif BMI > 30 and BMI <= 35:
                speak("You are obese")
            elif BMI > 35:
                speak("You are extremely obese")
            else:
                speak("Sorry, couldn't calculate BMI")

        elif 'network speed' in query or 'speed test' in query:
            st = speedtest.Speedtest()
            stdl = st.download()
            stup = st.upload()

            speak("you are having a download speed of" + int(stdl))
            speak("you are having an upload speed of" + int(stdl))


        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=5bad7ddd7071437cbc2ab53a97dd7584''')
                data = json.load(jsonObj)
                i = 1

                print("Here are some top news from the Google News India")
                speak('here are some top news from the Google News India')
                print('''========================= Google News India ======================''' + '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if i == 6:
                        break
                    else:
                        continue
            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'I will fail today' in query or "I'll fail today" in query:
            speak("It often happens haha")

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown.exe /s /t 00")

        elif 'fact' in query:
            speak("alright here's a fact for you")
            v = randfacts.getFact()
            print(v)
            speak(v)

        elif 'What all can you do' in query:
            print("I am capable of doing many things like getting weather information, news, jokes and much more")
            speak('I am capable of doing many things like getting weather information, news, jokes and much more')

        elif "don't listen" in query or "stop listening" in query:
            print("For how long do you want me to stop from listening?")
            speak("for how long do you want me to stop from listening?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Here's what i found")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('Lara.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% I:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Lara.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak(query)
            speak("How are you")

        elif "are you better than alexa" in query:
            print("I might say no but i am trying my level best to be better than alexa")
            speak('I might say no but i am trying my level best to be better than alexa')

        elif "which is your favourite colour" in query:
            print("I like the colour blue")
            speak('I like the colour blue')

        elif "can you change your voice" in query:
            print("Hmm..May be you should contact my developer")
            speak('Hmm..May be you should contact my developer')

        elif "is my internet connected" in query:
            print("If I respond then your system is definitely connected to internet")
            speak('if i respond then your system is definitely connected to internet')

        # most asked question from google Assistant 
        elif "will you be my girlfriend" in query:
            speak("Umm...I'm not sure, may be you should give me some time")

        elif "will you marry me" in query:
            print("If I were a human then i would have thought about it")
            speak('If I were a human then i would have thought about it')

        elif "how are you" in query:
            speak("I'm fine, thanks for asking")

        elif "i love you" in query:
            print("that's so sweet💕")
            speak("that's so sweet")

        elif "which is" in query:
            client = wolframalpha.Client("E9QJTG-3R93TJ33H3")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

                # elif "" in query:
            # Command go here 
            # For adding more commands
