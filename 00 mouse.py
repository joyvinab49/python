from pykeyboard import *
from pymouse import *
import time
import pythoncom
import pyHook


m = PyMouse()
k = PyKeyboard()


def contin(xy):
    count = int(input(">>>"))
    while count > 0:
        time.sleep(1)
        m.click(xy[0], xy[1])
        print(m.position())
        # k.type_string('123456')
        # k.tap_key(k.enter_key)
        count -= 1


def onMouseEvent(event):
    print(event.Position)
    contin(event.Position)
    return True


def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAllButtonsDown = onMouseEvent
    # hm.MouseAllButtonsUp = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
