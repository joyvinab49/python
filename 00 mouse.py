# from pykeyboard import *
from pymouse import *
import time
import pythoncom
import PyHook3 as pyHook


m = PyMouse()
# k = PyKeyboard()

target_num = int(input(">>>一共有几个键："))
target_mouse = []
# num = int(input(">>>要按的键有几个："))
# num_list = []
# count = []
# while num > 0:
#     num_list.append(int(input(">>>")) - 1)
#     count.append(int(input(">>>次数：")))
#     num -= 1


def contin(x, y):
    while count > 0:
        print("12322")
        time.sleep(1)
        print("555")
        m.click(x, y)
        print("1231")
        print(m.position())
        # k.type_string('123456')
        # k.tap_key(k.enter_key)
        count -= 1


def onMouseEvent(event):
    print(event.Position)
    print("abc")
    # contin(event.Position[0],event.Position[1])
    target_mouse.append(event.Position)
    print("def")
    print(target_mouse)
    keyboard_hook = True
    print("--------------")
    pyHook.HookManager().UnhookMouse()
    return True


def main():
    hm = pyHook.HookManager()
    print("454")
    hm.MouseAllButtonsDown = onMouseEvent
    print("333")
    # hm.MouseAllButtonsUp = onMouseEvent
    # print("564")
    hm.HookMouse()
    print("3ds")
    pythoncom.PumpMessages()
    print("12341")


if __name__ == "__main__":
    # while target_num > 0:
    #     print("aaa")
    #     target_num -= 1

    main()
