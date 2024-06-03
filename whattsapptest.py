import pyautogui as pg
import time

time.sleep(5)
for i in range(5):
    pg.write("Hi")
    pg.press("enter")
