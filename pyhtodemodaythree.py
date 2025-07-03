import pyautogui
import time

def open_browser():
    print("Opening browser...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('chrome', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)  # Give time for Chrome to open

def search_in_browser(query):
    print("Searching on Google...")
    pyautogui.write("India vs England Cricket match")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(640, 669, duration=0.5)
    pyautogui.click()   
    time.sleep(3)  # Wait for search results to load

def click_first_link():
    print("Clicking first search result...")
    # Move to typical first result position on 1080p screen
    pyautogui.moveTo(608, 583, duration=0.5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(672, 456, duration=0.5)
    pyautogui.click()

# Main flow
open_browser()
click_first_link()
search_in_browser("India vs England Cricket match")

