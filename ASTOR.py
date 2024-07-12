import pyttsx3
from email import message
import imp
import sys
from time import time
from weakref import WeakKeyDictionary
import pyttsx3
from requests.api import head
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import pywhatkit
import pyjokes
import smtplib
import requests
from requests import get
import random
import pyautogui
import speedtest
from email.message import EmailMessage
from wikipedia import exceptions
import time 
import PyPDF2
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ASTORGUI import Ui_ASTOR


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour <18 :
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else :
        print("Good Evening!")
        speak("Good Evening!")
    
    print("I am your Astor, How may help you!")
    speak("I am your Astor, How may help you!")

def send_email(receiver , subject , message):
    server =smtplib.SMTP('smtp.gmail.com',587)
    #server.ehlo()
    server.starttls()
    server.login('prathamdg20comp@student.mess.ac.in', '2020HE0287')
    email =EmailMessage()
    email['From']='prathamdg20comp@student.mes.ac.in'
    email['To']= receiver
    email['Subject']= subject 
    email.set_content(message)
    server.send_message(email)
    #server.close()

def news():
    main_url ='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f12d3c8b057a47a89fabaacf6591ca66'
    main_page =requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day =["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('dlcoa.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(f"Total number of pages in this book {pages} ")
    speak(f"Total number of pages in this book {pages} ")
    print("sir please enter the page number i have to read")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            #r.pause_threshold = 1
            audio = r.listen(source)
            
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)

            print("Say that again please...")
            return "None"
        return query 

    def TaskExecution(self):
        if __name__ == "__main__":
            wishMe()
        #while True:
            self.query = self.takeCommand().lower()
    
            if 'wikipedia' in self.query:
                print('Searching Wikipedia...')
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                print("According to wikipedia")
                speak("According to wikipedia")
                print(results)
                speak(results) 

            elif 'read pdf' in self.query:
                pdf_reader()
            
            elif 'who made you' in self.query:
                print("I was born when many bright minds came together to create an Assistant, just for you")
                speak("I was born when many bright minds came together to create an Assistant, just for you")

            elif 'where do you live' in self.query:
                print("So, turn left from paanwaala and then go straight till you see a Banyan tree. just kidding ,i live in the cloud")
                speak("So, turn left from paanwaala and then go straight till you see a Banyan tree. just kidding ,i live in the cloud")
            
            elif 'what can you do for me' in self.query:
                print("Theres a lot, you can try saying thing like play song, open whatsapp or tell todays news")
                speak("Theres a lot, you can try saying thing like play song, open whatsapp or tell todays news")    
            
            elif 'hello' in self.query:
                print("Namaste!")
                speak("Namaste!") 

            elif 'how are you' in self.query:
                print("i am feeling all charged up, ready to go!")
                speak("i am feeling all charged up, ready to go!")

            elif 'open youtube' in self.query:
                print("sir, what should i search on youtube")
                speak("sir, what should i search on youtube")
                self.query =self.takeCommand().lower()
                speak("searching..." + self.query)
                webbrowser.open("www.youtube.com/"+f"{self.query}")

            elif 'open google' in self.query:
                print("sir, what should i search on google")
                speak("sir, what should i search on google")
                self.query =self.takeCommand().lower()
                speak("searching..." + self.query)
                webbrowser.open(f"{self.query}")

            elif 'open twitter' in self.query:
                speak("opening...")
                webbrowser.open("www.twitter.com")

            elif 'open instagram' in self.query:
                speak("opening...")
                webbrowser.open("www.instagram.com")

            elif 'open whatsapp' in self.query:
                speak("opening...")
                webbrowser.open('https://web.whatsapp.com/')

            elif 'open facebook' in self.query:
                speak("opening...")
                webbrowser.open("www.facebook.com")

            elif 'open gmail' in self.query:
                speak("opening...")
                webbrowser.open("www.gmail.com")

            elif 'open meet' in self.query:
                speak("opening...")
                webbrowser.open("https://meet.google.com/?pli=1")
            
            elif 'open classroom' in self.query:
                speak ("opening...")
                webbrowser.open("www.classroom.google.com")

            elif 'open online compiler' in self.query:
                speak ("opening...")
                webbrowser.open("www.programiz.com/c-programming/online-compiler")

            elif 'play music' in self.query:
                music_dir = 'C://Users//Asus//Music'
                songs = os.listdir(music_dir)
                speak('playing...')
                rd =random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif 'play video' in self.query:
                video_dir ='C://Users//Asus//Videos'
                video =os.listdir(video_dir)
                speak('playing...')
                rd =random.choice(video)
                os.startfile(os.path.join(video_dir, rd))

            elif 'play'in self.query:
                song = self.query.replace('play','')
                speak('playing' + song + 'on youtube')
                pywhatkit.playonyt(song)

            elif 'jokes' in self.query:
                speak(pyjokes.get_joke())
            
            elif 'open vs code' in self.query:
                codepath ="C:\\Users\\SAHIL GAIKWAD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
                speak('opening...')
                os.startfile(codepath)

            elif 'open chrome' in self.query:
                chromepath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                speak('opening...')
                os.startfile(chromepath) 

            elif 'open notepad' in self.query:
                npath ="C:\\Windows\\system32\\notepad.exe"
                speak('opening...')
                os.startfile(npath)

            elif 'open command prompt' in self.query:
                speak('opening...')
                os.system('start cmd')

            elif 'open camera' in self.query:
                speak('opening...')
                cap =cv2.VideoCapture(0)
                while True:
                    ret ,img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==0:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")

            elif 'send message' in self.query:
                self.query =self.takeCommand().lower()
                print("sir ,what should i send ")
                speak("sir ,what should i send ")
                speak("sending.." + self.query)
                pywhatkit.sendwhatmsg("+919168432382",f"{self.query}",14,30)
                pywhatkit.sendwhatmsg()

            elif 'send email' in self.query:   
                email_list ={
        'pratham':'pratham.goverkar21@gmail.com',
        'ramsha' :'ramshabeg2018@gmail.com',
        'darshan':'darshanmhatre06@gmail.com',
        'nishant':'nishantkeni4@gmail.com',
        'riya'   :'riyanarayan945@gmail.com',
        'sahana' :'sahanakumbar205@gmail.com',
        'ekta mam': 'eukey@mes.ac.in'
        }
                def get_email_info():
                    print("to whom you want to send email")
                    speak("to whom you want to send email")
                    name = self.takeCommand().lower()
                    receiver = email_list[name]
                    print(receiver)
                    print("what is the subject of your eamil ?")
                    speak("what is the subject of your eamil ?")
                    subject =self.takeCommand().lower()
                    print("tell me what message should i send ?")
                    speak("tell me what message should i send ?")
                    message =self.takeCommand().lower()
                    send_email(receiver , subject , message)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                    print("Do you want to send more email...?")
                    speak("Do you want to send more email...?")
                    send_more = self.takeCommand().lower()
                    if 'yes' in send_more:
                        get_email_info()        
                get_email_info()
            
            elif 'the time is' in self.query:
                strTime=datetime.datetime.now().strftime("%I:%M:%S %p")
                print(strTime)
                speak('sir ,the current time is' + strTime)
            
            elif 'tell me the news' in self.query:
                speak("please wait sir , i am fetching the latest news")
                news()

            elif 'internet speed' in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                print(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            elif 'increase the volume' in self.query:
                print("increasing the volume")
                speak("increasing the volume")
                pyautogui.press("volumeup")
            elif 'decrease the volume' in self.query:
                print("decreasing the volume")
                speak("decreasing the volume")
                pyautogui.press("volumedown")
            elif 'volume mute'in self.query:
                print("Muting the volume")
                speak("Muting the volume")
                pyautogui.press("volumemute")
            
            elif 'take a screenshot' in self.query:
                print("sir please tell me the name for this screenshot file")
                speak("sir please tell me the name for this screenshot file")
                name =self.takeCommand().lower()
                print("sir please hold the screen for few seconds, i am taking screenshot")
                speak("sir please hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img =pyautogui.screenshot()
                img.save(f"{name}.png")
                print("i am done, the screenshot is saved in our main folder")
                speak("i am done, the screenshot is saved in our main folder")
            
            elif 'what is my location' in self.query:
                print("wait sir, let me check your location")
                speak("wait sir, let me check your location")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state = geo_data['state']
                    country = geo_data['country']
                    print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    print("sorry sir, due to network issue i am not able to find your location") 
                    speak("sorry sir, due to network issue i am not able to find your location")
                    pass

            elif 'open virtual mouse' in self.query:
                print('opening virtual mouse...')
                speak('opening virtual mouse...')
                import AiVirtualMouse

            elif 'open virtual mouse' in self.query:
                print('opening virtual painter...')
                speak('opening virtual painter...')
                import AiVirtualPainter

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ASTOR()
        self.ui.setupUi(self)
        self.ui.RUN.clicked.connect(self.startTask)
        self.ui.EXIT.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Asus/Downloads/RECO.gif")
        self.ui.Background.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/Asus/Downloads/initalising.gif")
        self.ui.initating.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/Asus/Downloads/FACE ID.gif")
        self.ui.Faceid.setMovie(self.ui.movie)
        self.ui.movie.start()
        #timer = QTimer(self)
        #timer.timeout.connect(self.showTime)
        #timer.start(1000)
        startExecution.start()

app = QApplication(sys.argv)
astor = Main()
astor.show()
exit(app.exec_())