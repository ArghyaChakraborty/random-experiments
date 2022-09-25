#!/usr/bin/python
import os
import pyautogui
import time
import random

pyautogui.FAILSAFE = False

######################################################################

INITIAL_SLEEP_TIME_SECONDS = 10 # Initial delay so that a notepad can be easily opened
INTERLINE_SLEEP_TIME_SECONDS = (1, 3) # Delay between typing each line
LOOP_SLEEP_TIME_SECONDS = (3, 5) # Delay after a whole file is typed & next file is picked up
INPUT_CODE_PATH = os.path.dirname(os.path.abspath(__file__)) # Put one or more source code files in this path that you want to be typed

######################################################################

current_file_name = os.path.basename(__file__)
code_files = []
for file in os.listdir(INPUT_CODE_PATH):
    if os.path.isfile(file) and str(file) != current_file_name:
        code_files.append(file)
print("Code files to go through: "+str(code_files))

while len(code_files) > 0:
    print("#############################################################")
    print("Your Wish Is My Command")
    print("I Will Be Awake So That You Do Not Have To")
    print("See You On The Other Side")
    print("##############################################################")
    print("\nMeanwhile, Open a Notepad and maximize it so that code can be written in it. You have "+str(INITIAL_SLEEP_TIME_SECONDS)+" sec\n")

    time.sleep(INITIAL_SLEEP_TIME_SECONDS)

    input_code_file = code_files[random.randint(0, len(code_files))]
    print("Selected: "+input_code_file)
    lines = []
    with open(input_code_file, "r") as fp:
        lines = fp.read().split("\n")
    
    while True:
        for line in lines:
            for c in line:
                pyautogui.typewrite(c)
            pyautogui.press('enter')
            time.sleep(random.randint(INTERLINE_SLEEP_TIME_SECONDS[0], INTERLINE_SLEEP_TIME_SECONDS[1]))
        time.sleep(random.randint(LOOP_SLEEP_TIME_SECONDS[0], LOOP_SLEEP_TIME_SECONDS[1]))

if len(code_files) == 0:
    print("PLease add some source code files in dir: "+INPUT_CODE_PATH+" and re-execute this program")

# Some examples:
#   pyautogui.moveTo(200, i*4)
#   pyautogui.press('shift')
#   pyautogui.press('backspace')
#   pyautogui.click()
#   pyautogui.typewrite("   ")
#
# All supported keys:
#   print(pyautogui.KEYBOARD_KEYS)
#   print(pyautogui.KEY_NAMES)
