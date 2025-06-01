import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener

ACTIVATE_KEY = KeyCode(char="+")
DEACTIVATE_KEY = KeyCode(char="!")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(3)

def toggle_event(key):
    global clicking
    if key == ACTIVATE_KEY:
        clicking = True
    if key == DEACTIVATE_KEY:
        clicking = False

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()