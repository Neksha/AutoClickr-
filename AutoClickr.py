import tkinter as tk
import pyautogui
import time
from pynput import keyboard

def start_autoclicker(delay, stop_key):
    def on_press(key):
        if key == stop_key:
            return False
    with keyboard.Listener(on_press=on_press) as listener:
        while listener.running:
            pyautogui.click()
            time.sleep(delay/1000) # delay is in milliseconds, so we divide by 1000 to convert to seconds

def stop_autoclicker():
    exit()

window = tk.Tk()

speed_scale = tk.Scale(window, from_=1, to=500, orient=tk.HORIZONTAL, label="Click Delay (ms)")
speed_scale.pack()

stop_key_entry = tk.Entry(window, width=10)
stop_key_entry.insert(0, "esc") # default stop key is "esc"
stop_key_entry.pack()

start_button = tk.Button(window, text="Start", command=lambda: start_autoclicker(speed_scale.get(), stop_key_entry.get()))
start_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_autoclicker)
stop_button.pack()

window.mainloop()

#by soleous aka neksha
