import time
import os
from PIL import Image
import pytesseract
import pyautogui as p
from pathlib import Path

file_destination=Path("D:\Computer-Benchmark\Scripts\Typing\Capture.PNG")
file_destination.unlink(missing_ok=True)

img_box=(197,393,1148,519)

def read_png(file_path):
    if not os.path.exists(file_path):
        print("File does not exist")
        return
    try:
        img=Image.open(file_path)
        text=pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Exception {e}")

text=read_png('D:\Computer-Benchmark\Scripts\Typing\Capture.PNG')
p.moveTo(195,339,duration=2)
p.click()
p.typewrite(text)
