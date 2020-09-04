#CORONA update notifier.....
from plyer import notification   #pip install plyer
from covid import Covid          #pip install covid
import time
import pyttsx3                   #pip install pyttsx3


voice=pyttsx3.init('sapi5')    #sound API(application program interface)
voice_list=voice.getProperty('voices')
voice.setProperty('voices',voice_list[0].id)

def speak(text):
    voice.say(text)
    voice.runAndWait()

def notifyme(title, message):
    notification.notify(
        title= title,
        message = message,
        app_icon = 'E:\corona update\icon2.ico',
        timeout = 30)

def getData(x):
    covid=Covid()
    cases=covid.get_status_by_country_name(x)
    for x in cases:
        print(x,":",cases[x])
    return f"confirmed cases are : {cases.get('confirmed')} \n active cases are : {cases.get('active')} \n deaths are : {cases.get('deaths')}"
       
if __name__=="__main__":
    x='india'
    notifyme("COVID CASES LATEST UPDATE...!!!!!",getData(x))
    speak("COVID CASES LATEST UPDATE...!!!!!")
    speak(f"time now is{time.ctime()}")
    speak(getData(x))
    print(time.ctime())   