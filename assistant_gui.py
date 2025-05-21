import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import threading

class AIChatbotAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Autonomous Vehicle Assistant")
        self.detected_object = "None"
        self.map_status = "No obstacles"

        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        self.build_gui()

    def build_gui(self):
        self.status_label = tk.Label(self.root, text="System Status: Running", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.object_label = tk.Label(self.root, text=f"Detected Object: {self.detected_object}", font=("Arial", 12))
        self.object_label.pack()

        self.map_label = tk.Label(self.root, text=f"Map Status: {self.map_status}", font=("Arial", 12))
        self.map_label.pack()

        self.listen_button = tk.Button(self.root, text="🎙️ Voice Command", command=self.listen_command)
        self.listen_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.quit_button.pack()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_command(self):
        def threaded_listen():
            self.speak("I'm listening.")
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source, timeout=5)
                    command = self.recognizer.recognize_google(audio).lower()
                    self.process_command(command)
            except:
                self.speak("Sorry, I didn't catch that.")

        threading.Thread(target=threaded_listen).start()

    def process_command(self, command):
        print(f"[Command]: {command}")
        response = "I didn't understand."

        if "object" in command:
            response = f"The latest detected object is {self.detected_object}."
        elif "map" in command:
            response = f"The map shows: {self.map_status}."
        elif "stop" in command or "exit" in command:
            response = "Stopping the system."
            self.speak(response)
            self.root.quit()
            return
        elif "status" in command:
            response = "The system is running and monitoring surroundings."

        self.speak(response)

    # Simulate updates (from main loop or sensors)
    def update_status(self, object_name, map_text):
        self.detected_object = object_name
        self.map_status = map_text
        self.object_label.config(text=f"Detected Object: {self.detected_object}")
        self.map_label.config(text=f"Map Status: {self.map_status}")

