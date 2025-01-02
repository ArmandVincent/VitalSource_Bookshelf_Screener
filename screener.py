import pyautogui
import time
import keyboard


def main():

    # Please check that you have done every pre requisite before.
    
    # This first block of code gives you the time to open the book as full screen

    time.sleep(5) #Change here the time you need to switch to Bookshelf
    pyautogui.press('f3')
    time.sleep(3)

    x1, y1 = 963, 978 # Here you should probably change the coordinates where it clicks
    x, y = 10, 10
    pyautogui.moveTo(x1, y1)
    pyautogui.scroll(-500)
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')

    for i in range(921): #number of pages - 2, you probably should check if there is no duplicata at the end

        # Stop the screening if p is pressed (spam it)
        if keyboard.is_pressed('p'):
            print("Programme arrêté par l'utilisateur.")
            break
        pyautogui.moveTo(x, y)
        time.sleep(0.2)
        pyautogui.press('f3')
        time.sleep(3)
        pyautogui.moveTo(x1, y1)
        pyautogui.scroll(-500)
        pyautogui.moveTo(x1, y1)
        pyautogui.click(button='left')

# Then go to pdfer.py to make it a pdf

if __name__ == "__main__":
    main()