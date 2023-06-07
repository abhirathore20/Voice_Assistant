import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening.......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen()
        try:
            print("recognizing...")
            data = recognizer.recognixe_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
def speechtx(x):
    engine =pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()
speechtx("hello welcome to .....")

if __name__ =='__main__':
    while True :
    # if sptext().lower() =="hey Abhi" :
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is Assitant"
                speechtx(name)
            elif "How old are you" in data1:
                age = "I'am two years old"
                speechtx(age)
        
    # else:
    #     print("Thanks")
            elif 'now time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "web" in data1:
                webbrowser.open("https://www.google.com/")

            elif 'joke' in data1:
                joke_1 = pyjokes.get_jokes(language = "en",category= "neutral")
                print(joke_1)
                speechtx(joke_1)

            elif "play song" in data1:
                add = "address of file locsation"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))

            elif "exit" in data1:
                speechtx("Thank You")
                break 

            time.sleep(5)
