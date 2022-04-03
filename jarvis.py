
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib #for sending email


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id) #0->zira(women) 1->david(men)
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afterNoon")

    else:
        speak("good eveninig")


    speak("hey!! i'am Pinto,How may i help you Faazil")


def takeCommand():
    #it takes microPhone inputs from the user and returns  string outPut
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #seconds of non speaking audio before actual audio is considered complete ...
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,Language='en-in')
        print("user said..",query)

    except Exception as e:
        # print(e)
        print("pardon but...can u please..say that again")
        return "None"
    return query
# def sendEmail:
    #   server = smptplib.SMTP('smtp.gmail.com',587)
    #   server.ehlo()
    #   server.starttls()
    #   server.login('giveEmail'.'password')


if __name__ == "__main__":
    # speak("faazil is a good coder")
    wishMe()
    # while True: //will listen every time
    if 1:   #will listen only once
        query = takeCommand().lower()
    #logic to execute task based on query
        if 'wikipedia' in query:
           speak('searching wikipedia....')
           query = query.replace("wikipedia","")
           results  = wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackOverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # elif 'email to fazil' in query:
        #     try:
        #         speak("what should i say?")
        #         content=takeCommand()
        #         to = "mohammeddfazil196@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry Bhai i cannot send this email")
 
            #could ad more task like play music etc
    