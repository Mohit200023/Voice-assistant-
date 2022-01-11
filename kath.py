
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys 

#voice setting 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#functions 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good morning,Boss')
    elif hour>=12 and hour<18:
        speak('GOOd afternoon,Boss')
    else:
        speak('good evening,Boss')
    speak("I am kath") 
 
 #takecommand
  
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('listening.... ')
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said:{query}\n')
    except Exception as e:
        speak('say that again boss ')
        return "None"


if __name__=='__main__':
    clear = lambda: os.system('cls')
    
    wishme()
    while True:
        query = takeCommand()
                
                                                #wikipedia
        if 'Wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences =2)
            speak('According to wikipedia')
            speak(result)
                                                    #time getting statment
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime('%:H%:M%:S')  
            speak(f'Boss, the time is {strTime}')
        
                                         #for entertainment
        
        elif 'how are you ' in query:
            speak('I am good how are you? ')
        elif'I am fine' in query:
            speak('thats good ')
        elif 'What is your name' in query:
            speak('My name is kath')
        elif'Who created you' in query:
            speak ('My boss mohit created me for his personal projects. and i glad to be a aprt of his work ')
        elif'describe your  self ' in query:
            speak('i am voice assitant created in python conting different type of library like time,wikipedia,web browser etc.')
        elif'would you like be my friend' in query :
            speak('i am your friend and my name is kath')
        elif'how was your day'in query:
            speak(' Just waiting to help you BOSS and talking to you make my day good ')
        elif'hows you  doing ' in query:
            speak('nothing much just waiting to help my boss')
        
                                    
                                    #to make it sleep 
        
        elif 'you can sleep now 'in query:
            speak('okay Boss you can call me when ever you want')
            sys.exit                   
        




            