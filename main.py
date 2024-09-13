import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)  


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
            return command.lower()
        except Exception as e:
            print("Sorry, I didn't catch that.")
            return None

def run_jurvis():
    speak("Hello Souvick Kumar Halder, I am Jurvis. How can I assist you today?")
    
    while True:
        command = listen_command()

        if command is None:
            continue

        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%H:%M')
            speak(f"The time is {current_time}")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'play music' in command:
            music_dir = 'C:\\Users\\User\\Music'  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that. Please repeat.")

if __name__ == "__main__":
    run_jurvis()
