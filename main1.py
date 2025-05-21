import tkinter as tk
from assistant_gui import AIChatbotAssistant
import threading
import time

def run_main_loop(assistant):
    # Simulate your vehicle AI loop
    objects = ["car", "pedestrian", "sign", "tree"]
    for i in range(20):
        detected = objects[i % len(objects)]
        map_info = f"{i%6} dynamic obstacles"
        assistant.update_status(detected, map_info)
        time.sleep(2)

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    assistant = AIChatbotAssistant(root)

    # Start simulation in another thread
    threading.Thread(target=run_main_loop, args=(assistant,), daemon=True).start()

    root.mainloop()
