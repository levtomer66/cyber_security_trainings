# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
# driver = webdriver.Chrome(options=chrome_options)

import pyautogui
import time
pyautogui.PAUSE = 0.5

def search_and_click(text, with_align=False, rev=False):
    if rev:
        text = text[::-1]
    print("Ctrl+F")
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.3)
    print(f"Writing text: {text}")
    pyautogui.typewrite(text,interval=0.01,_pause=True)
    pyautogui.scroll(-5000)
    print(f"Pressing F7...")
    pyautogui.press('f7', _pause=True)
    if with_align:
         pyautogui.move(-40,0)
    print(f"Clicking...")
    pyautogui.click(_pause=True)

# def enter_story():
#     search_and_click("An interesting")
#     time.sleep(3)
    

def con_click(times=1, delay=3):
    first = True
    for i in range(times):
        print(f"Click number {i+1}/{times}")
        if first:
            search_and_click("Continue")
            first = False
        else:
            pyautogui.click()
        time.sleep(delay)

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position() 
print("Starting in 3...")
time.sleep(3)

# print("Entering story")
# enter_story()
con_click(5, 2)
search_and_click("She's Waiting for her friend.")
con_click(2, 1)
con_click(2, 2.5)
search_and_click("A ella le gusta")
con_click(4, 1.5)
search_and_click("propose to her boyfriend")
con_click(6, 2)
search_and_click("conoces a Leo", True)
con_click(6, 1.5)
search_and_click("That his girlfriend is going to propose to him.")
con_click(1, 1)
search_and_click("I am", rev=True)
search_and_click("Estoy", rev=True)

search_and_click("friend", rev=True)
search_and_click("amiga", rev=True)

search_and_click("Que", rev=True)
search_and_click("what", rev=True)

search_and_click("yo", rev=True)
search_and_click("Estoy", rev=True)

search_and_click("novio", rev=True)
search_and_click("boyfriend", rev=True)

search_and_click("muy", rev=True)
search_and_click("very", rev=True)

search_and_click("tan", rev=True)
search_and_click("so", rev=True)

search_and_click("conoces a", rev=True)
search_and_click("you know", rev=True)

search_and_click("Es", rev=True)
search_and_click("it's", rev=True)

search_and_click("fin de semana", rev=True)
search_and_click("weekend", rev=True)

search_and_click("esperando a", rev=True)
search_and_click("waiting for", rev=True)

search_and_click("esta", rev=True)
search_and_click("is", rev=True)

search_and_click("puedo", rev=True)
search_and_click("I can", rev=True)

search_and_click("the", rev=True)
search_and_click("el", rev=True)


search_and_click("romantic", rev=True)
search_and_click("romantico", rev=True)


search_and_click("De verdad", rev=True)
search_and_click("really", rev=True)

search_and_click("here", rev=True)
search_and_click("aqui", rev=True)

# pyautogui.click('An Interesting Conversation')           