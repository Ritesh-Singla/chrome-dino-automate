import pyautogui
from PIL import Image, ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
def isCollide(data):
    for i in range(235,290):
        for j in range(322,380):
            if data[i,j]<180 and data[i,j]>50:
                hit('up')
                return
    return
if __name__ == "__main__":
    print("Dino game is about to start in 3 seconds")
    time.sleep(3)
    hit('up')
    while True:
        image  = ImageGrab.grab().convert('L')
        data = image.load()  
        isCollide(data)
