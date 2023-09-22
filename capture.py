import keyboard
from PIL import ImageGrab
import time
import os
from plyer import notification


def capture(hotkey, directory, notify=False):
    print(f"started to capture with hotkey({hotkey})")

    while True:
        try:
            keyboard.wait(hotkey)
            screenshot = ImageGrab.grab()
            currentTime = time.strftime("%Y%m%d%H%M%S")
            fileName = currentTime
            filePath = f"{directory}\\{fileName}.png"

            counter = 1
            while os.path.exists(filePath):
                fileName = f"{currentTime}_{counter}.png"
                counter += 1
                filePath = f"{directory}\\{fileName}.png"

            screenshot.save(filePath, "PNG")

            print(f"Saved to: {os.path.abspath(filePath)}")

            if notify:
                notification.notify(
                    title='Capture',
                    message=f'Captured a screenshot at {os.path.abspath(filePath)}',
                    app_name="capture",
                    timeout=1,
                )

        except Exception as e:
            print(f"Error: {e}")


def getDirectoryConfig():
    f = open("./dir.txt", "r")
    directory = f.readline()
    f.close()

    if not directory:
        directory = f'{os.environ["userprofile"]}\\Pictures'

    return directory


def getHotkeyConfig():
    f = open("./hotkey.txt", "r")
    directory = f.readline()
    f.close()

    return directory


def changeDirectoryNormalize(directory):
    if directory[-1] == "\\":
        directory = directory[:-1]
    return directory


if __name__ == "__main__":
    directory = ""
    if os.path.exists("./dir.txt"):
        directory = getDirectoryConfig()
        print("detected directory:", os.path.abspath(directory))
    else:
        directory = input("input image directory: ")

    directory = changeDirectoryNormalize(directory)
    capture(getHotkeyConfig(), directory)
