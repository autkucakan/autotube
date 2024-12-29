import tkinter as tk
import pyautogui
import time

def autoyt():
    time.sleep(5)
    pyautogui.moveTo(600, 0, duration=2)
    pyautogui.moveTo(600, 55, duration=2)
    time.sleep(2)
    pyautogui.click(button='middle')

root = tk.Tk()
root.title("Auto Youtube")

buttonStart = tk.Button(root, text="Start", command=autoyt)
buttonStop = tk.Button(root, text="Stop", command=exit)
buttonStart.pack(padx=80, pady=20)
buttonStop.pack(padx=80, pady=20)

root.mainloop()