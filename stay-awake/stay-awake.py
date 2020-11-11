#!/usr/bin/python
import pyautogui
import time

pyautogui.FAILSAFE = False

print("#############################################################")
print("         Your Wish Is My Command")
print("         I Will Be Awake So That You Do Not Have To")
print("         See You On The Other Side")
print("##############################################################")

# All supported keys:
# print(pyautogui.KEYBOARD_KEYS)
# print(pyautogui.KEY_NAMES)

while True:
    time.sleep(30)
    for i in range(0, 100):
        pyautogui.moveTo(200, i*4)

    pyautogui.press('shift')
    pyautogui.click()
    # pyautogui.typewrite("   ") # 3 spaces
    # pyautogui.press('backspace') # backspace 3 times
    # pyautogui.press('backspace')
    # pyautogui.press('backspace')
