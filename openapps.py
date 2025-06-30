import pyautogui
import subprocess
import time

def main():
    apps = ["notepad.exe", "cmd.exe", "calculator.exe"]

    for app in apps:
        try:
            subprocess.Popen(app)
            time.sleep(2)
        except FileNotFoundError:
            print(f"{app} not found.")

    # Give time to load before closing
    time.sleep(5)

    for _ in apps:
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)

if __name__ == "__main__":
    main()
