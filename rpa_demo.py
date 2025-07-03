import time
import pyautogui
# mouse Operations
#pyautogui.click(100,100)
#time.sleep(10)
#pyautogui.rightClick(100,100)
time.sleep(3)
#pyautogui.doubleClick(100,100)
x,y = pyautogui.position()
print(f'x:{x} , y:{y}')
#time.sleep(3)
#pyautogui.click(911,327)
#time.sleep(3)
#pyautogui.dragTo(100,100,200,200)
#pyautogui.scroll(500)
 
#keyboard operation
#pyautogui.write("Hi Naveen")
#pyautogui.typewrite("Hi Naveen")

#pyautogui.hotkey('ctrl','a')

#image
#imagelocate = pyautogui.locateOnScreen('copilotAI.png',confidence=0.8)
#print(imagelocate)
#time.sleep(3)
#pyautogui.click(pyautogui.center(imagelocate))
#print(pyautogui.size())
#ss = pyautogui.screenshot()
#ss.save("demo.png")