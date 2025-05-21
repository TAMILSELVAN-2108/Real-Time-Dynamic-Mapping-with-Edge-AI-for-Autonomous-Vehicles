import speech_recognition as sr
import pyttsx3

def voice_chatbot():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.say("Hello, I'm your autonomous vehicle assistant.")
    engine.runAndWait()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            if "stop" in command:
                engine.say("Stopping the vehicle.")
                engine.runAndWait()
                break
        except:
            engine.say("Sorry, I didn't catch that.")
            engine.runAndWait()
