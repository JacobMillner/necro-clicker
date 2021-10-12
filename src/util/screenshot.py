import numpy as np
import cv2
import pyautogui
   

def screenshot():
    # take screenshot using pyautogui
    image = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    return image