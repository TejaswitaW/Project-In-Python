import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

r=sr.Recognizer()

option=0



def speak(audio):
    '''Function for speaking'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
    speak("I am Anna Sir. Please tell me how may I help you")
    speak("Please choose any option from following")
    speak("First option is for opening wikipedia")
    speak("Second option is for youtube ")
    speak("Third option is for opening google")
    speak("Fourth option is for the time")
    speak("Fifth option is for opening code blocks")
    speak("Sixth option is to send Email")
    speak("Seventh option is to exit")
    speak("If you want to listen again Enter 0")
    speak("Enter your option please")
 

def takeCommand(audio):
    '''It takes microphone input from the user and returns string output'''

    with sr.AudioFile(audio) as source:
        print("Listening...")
        audio = r.record(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio)

    except Exception as e:
        print("Say that again please...")  
        return "None"
    except OSError as e:
        print("I know")
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tejaswitawakhure@gmail.com', 'XXXXXXXXX')
    server.sendmail('teajswitawakhure@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        option=int(input("Please enter your option"))
        if option==1:
            query = takeCommand("WaveForWikipedia.wav").lower()
        elif option==2:
            query = takeCommand("WaveForYouTube.wav").lower()
        elif option==3:
            query = takeCommand("WaveForGoogle.wav").lower()
        elif option==4:
            query = takeCommand("WaveForTheTime.wav").lower()
        elif option==5:
            query = takeCommand("WaveForOpenCode.wav").lower()
        elif option==6:
            query = takeCommand("WaveForEmail.wav").lower()
        elif option==7:
            query=takeCommand("WaveForQuit.wav").lower()
        elif option==0:
            wishMe()
            

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
           

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is")
            speak(strTime)

        elif 'open code block' in query:
            codePath = "C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand("WaveForEmailContent.wav")
                to = "tejaswitawakhure@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry!!!!. I am not able to send this email")
                
        elif 'quit' in query:
            os._exit(0)
