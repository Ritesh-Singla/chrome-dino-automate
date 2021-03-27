import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

# def isCollide(data):
#     for i in range(130,175):
#         for j in range(300,370):
#             if data[i,j]< 100:
#                 return True
    # return False

if __name__ == "__main__":
    #print("Dino game is aboutr to start in 3 seconds")
    time.sleep(1)
    #hit('up')

    # while True:
    image  = ImageGrab.grab().convert('L')
    data = image.load()  
    # if isCollide(data):
    #     hit("up")                         
    # print(asarray(image))
    for i in range(220,250):
        for j in range(322,380):
            data[i,j]=140

    # for i in range(165,200):
    #     for j in range(250,322):
    #         data[i,j]=70

    image.show()
