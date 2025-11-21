import pyautogui as p
import time
time.sleep(2)
x,y=277,330
p.moveTo(x,y)

greenColor=(30,151,80)

while(True):
    if p.pixel(x,y)==greenColor:
        p.click()
    