import pyttsx3 
from datetime import datetime
import speech_recognition as sr




voiceid=1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[voiceid].id)
engine.setProperty('voice',voices[voiceid].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.now().strftime("%I %M %p")
    timespeak=f"The Time is {time}"
    speak(timespeak)
def date():
    year=datetime.now().strftime("%Y")
    month=datetime.now().strftime("%B")    
    day=datetime.now().strftime("%d")  
    date=f"Today's Date is {day} {month} {year}" 
    
    speak(date)
def wishMe():
    hour = int(datetime.now().hour)
    speak("Hello Sir!!")
    if hour>=0 and hour<12:
        speak("Good Morning !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!")
    else:
        speak("Good Evening!!")

    speak("I am SYNC. Please tell me how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User Asked: {query}\n")
        speak(f"User Asked: {query}\n")
    except Exception as e:
        print(e)
        
        print("Couldn't Recognise it Please Say it again..")
        speak("Couldn't Recognise it Please Say it again..")
        return "None"
    return query

# takeCommand()
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        g_path="C://Program Files//Google//Chrome//Application//chrome.exe %s"
        query=takeCommand().lower()
        if 'wikipedia'  in query or 'who is' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia","")
            query= query.replace("who is","")
            results= wikipedia.summary(query,sentences=2)
            print(f"Search Results for {query}")
            speak(f"Search Results for {query}")
            print(f"According to Wikipedia {results}\n")
            speak(f"According to Wikipedia {results}\n")

        elif 'open youtube' in query:
           g_path="C://Program Files//Google//Chrome//Application//chrome.exe %s"
           webbrowser. get(g_path).open_new("youtube.com")
        elif 'open google' in query:
            webbrowser. get(g_path).open_new("google.com")
        elif 'open whatsapp' in query:
            webbrowser. get(g_path).open_new("https://web.whatsapp.com/")
        elif 'what is' in query or 'search' in query or 'google' in query:
            query= query.replace("search","") 
            query= query.replace("google","") 
            webbrowser. get(g_path).open_new(f"https://www.google.com/search?q={query}")
        elif 'search youtube for' in query or 'youtube' in query:
            query= query.replace("search","") 
            query= query.replace("youtube","") 
            webbrowser. get(g_path).open_new(f"https://www.youtube.com/results?search_query={query}")
        elif 'play music' in query:
            music_dir ='C:\\Users\\Soumen-Riya-Tuku\\Desktop\\music'
            m_length= len(music_dir)
            songs=os.listdir(music_dir)
            music_random=random.randint(0,m_length-1)
            os.startfile((os.path.join(music_dir,songs[music_random])))        
        elif 'time' in query:
            time()