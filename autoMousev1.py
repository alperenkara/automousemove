import pyautogui
import time 
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
start = time.time()
try:
    while True:
        for i in range(1):
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)
except pyautogui.FailSafeException:
    end = time.time()
    pyautogui.alert('You spent {} minutes'.format(round((end-start)/60,2)))
