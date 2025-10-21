import pyautogui
import time
keyboard_chars = [
    # Lowercase letters
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',

    # Uppercase letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',

    # Numbers
    '0','1','2','3','4','5','6','7','8','9',

    # Punctuation and symbols
    '`','~','!','@','#','$','%','^','&','*','(',')','-','_',
    '=','+','[',']','{','}','\\','|',';',':',"'",'"',',','<',
    '.','>','/','?',
]

pyautogui.countdown(3)
print("Guessing...")
pyautogui.moveTo(630,1059,0.1)
pyautogui.click()

time.sleep(0.1)
password = ""
isGuessed = False
while isGuessed == False:
    for symbol in keyboard_chars:
        pyautogui.write(symbol)
        pyautogui.press("enter")
        if pyautogui.pixel(858,556) != (102,102,102) and pyautogui.pixel(858,556) != (101,101,101):
            isGuessed = True
            password = symbol
            break
            
print(f"The password is: \"{password}\"")



