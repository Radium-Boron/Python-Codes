#install pyautogui using pip
#make a file named as script where your spamming material is located
import pyautogui, time
time.sleep(5)
f = open("script", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter"
