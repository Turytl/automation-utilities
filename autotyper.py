import pyautogui
import time

# How long
ask = int(input("Enter the time in seconds: "))

# To switch to the next window
time.sleep(5)

def auto_type(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(0.05)
    pyautogui.press('enter')

for i in range(ask):
    auto_type("Hello World")
