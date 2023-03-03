from PIL import ImageGrab
import keyboard
import pyautogui

def getPress(key: chr) -> bool:
    try:
        if keyboard.is_pressed(key):
           return True
        else:
            return False
    except:
        return False

def main():
    working = True
    position = pyautogui.position()

    while working:
        if getPress('s'):
            working = False
        if getPress('d'):
            position = pyautogui.position()
        if not getPress('w'):
            continue
        
        image = ImageGrab.grab(bbox=(position.x, position.y, position.x + 10, position.y + 1))

        isIntersect = False
        for i in range(10):
            if image.getpixel((i, 0))[0] < 100:
                isIntersect = True
                break
        
        if isIntersect:
            keyboard.press('space')
        else:
            keyboard.release('space')

if __name__ == "__main__":
    main()
