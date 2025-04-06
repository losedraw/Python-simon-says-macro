import time
import pyautogui
import keyboard

class simonSays:
    def __init__(self):
        self.start_macro = False
        self.click_order_storage: list[tuple] = []
        self.click_memo: list[tuple] = []
        self.coords_color: dict[tuple: tuple] = {}

    def determine_coords(self):
        print('Hover your mouse over any button (prefferably in the center of it). Press "p" to record its coordinates. Do this in total 4 times.')
        for color in range(0, 4):
            while True:
                if keyboard.is_pressed('p'):
                    self.coords_color[tuple(pyautogui.position())] = pyautogui.pixel(tuple(pyautogui.position())[0], tuple(pyautogui.position())[1])
                    print(tuple(pyautogui.position()))
                    time.sleep(0.25)
                    break
        print('Are you satisfied with these coordinates? Press "r" to reselect, or press "c" to confirm the coordinates.')

    def color_checker(self):
        start_time = time.time()
        while True:
            for coords, color in self.coords_color.items():
                if pyautogui.pixel(coords[0], coords[1]) != color:
                    self.click_memo.append((coords[0], coords[1]))
                    start_time = time.time()
                    continue
            if time.time() - start_time >= 1.2:
                break

    def click_func(self):
        self.click_order_storage.append(self.click_memo[-1])
        for i in self.click_order_storage:
            time.sleep(0.3)
            pyautogui.click(i)
        self.click_memo = []

macro = simonSays()
macro.determine_coords()

while True:
    if keyboard.is_pressed('r'):
        macro.coords_color.clear()
        macro.determine_coords()
    if keyboard.is_pressed('c'):
        print('Press "o" to start')
        break

while True:
    if keyboard.is_pressed('o'):
        macro.start_macro = True
    if macro.start_macro == True:
        macro.color_checker()
        macro.click_func()
