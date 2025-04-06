# Python-simon-says-macro
A Python automation bot that plays browser-based Simon Says games using pixel detection and PyAutoGUI.

# Features
- Lets user select coordinates for buttons in any order
- Should work on any simon says game online

# Requirements
Install pyautogui and keyboard
```shell
pip install pyautogui keyboard
```
# Usage
Run the program
```shell
python macro.py
```
Recommended website:
https://freesimon.org/#google_vignette
- Press start and wait for the first light to finish blinking.
- Hover over a simon says button, then press 'p' to enter the coordinate. Do this for all the other buttons.
- Press 'r' to reset the coordinate selction process, or press 'c' to confirm coordinate selection.
- Press quit, then start the game again. Wait until the screen is no longer black, then press 'o' to start the program.

Additional notes:
- You can adjust the delay in from 1.2 to 2 seconds if it recognises one light blink as two blinks
```python
if time.time() - start_time >= 1.2:
  break
# line 31-32
```

- If for some reason, your simon says has more than four buttons, you can adjust the number of coordinates the program will check by adjusting the range
```python
for color in range(0, 4):
# line 14, change 4 into e.g. 5 or 6
```
