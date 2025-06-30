import pyautogui 
import time

variable = False

def moveMouse():
    pyautogui.moveRel(5, 0, duration=0.1)
    pyautogui.moveRel(0, 5, duration=0.1)
    time.sleep(10)

ask = input("Do you want to move mouse? y/n")

if ask == "y":
    variable = True
elif ask == "n":
    print("okay")
else:
    print("Invalid input")

while variable:
    moveMouse()
