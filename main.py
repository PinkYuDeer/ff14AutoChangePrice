import time
import win32gui
import win32api
import win32con
import random
import pyperclip


def get_all_windows():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return hWnd_list


def get_mesh_windows(hwnd_list, name):
    for hWnd in hwnd_list:
        title = win32gui.GetWindowText(hWnd)
        classname = win32gui.GetClassName(hWnd)
        if classname.startswith("FFXIVGAME"):
            print("找到窗口：%s %s" % (title, classname))
            return hWnd
        if title.startswith(name):
            print("找到窗口：%s %s" % (title, classname))
            return hWnd
    return None


def delay(time_p):
    if time_p < 1:
        time_p = random.uniform(time_p * 0.8, time_p * 1.2)
    else:
        time_p = random.uniform(time_p - 0.05, time_p + 0.05)
    time.sleep(time_p)


def press_key(hwnd_p, key, time_p):
    win32api.PostMessage(hwnd_p, win32con.WM_KEYDOWN, key, 0)
    delay(time_p)
    win32api.PostMessage(hwnd_p, win32con.WM_KEYUP, key, 0)


def win32print(price, gu_yuan, shang_pin):
    for i in range(0, len(price)):
        win32api.PostMessage(hwnd, win32con.WM_CHAR, ord(price[i]), 0)
        delay(0.02)
    print("第%s位雇员第%s件商品更改价格为：%s" % (gu_yuan + 1, shang_pin + 1, price))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_cur = None
    hwnd = get_mesh_windows(get_all_windows(), "最终幻想XIV")
    while hwnd is None:
        print("未找到窗口")
        _exit = input("按回车键退出，或输入最终幻想的窗口名：")
        if _exit == "":
            exit()
        hwnd = get_mesh_windows(get_all_windows(), _exit)
    mode = input("传唤铃界面输入1；雇员出售列表界面输入2:")
    while mode != "1" and mode != "2":
        mode = input("输入错误，请重新输入：")
    if mode == "1":
        press_key(hwnd, win32con.VK_NUMPAD2, 0.05)
        _inputting = True
        while _inputting:
            LieBiao = input("雇员分别有几件商品？请输入数字，以空格隔开：")
            ListOfLieBiao = LieBiao.split(" ")
            GuYuan = len(ListOfLieBiao)
            if GuYuan > 9:
                print("雇员数量超过9位，请重新输入")
                continue
            # 判断ListOfLieBiao是否为数字，并且范围在0-20之间
            for i in range(0, GuYuan):
                if ListOfLieBiao[i].isdigit() is False:
                    print("输入错误，请输入数字")
                    break
                if int(ListOfLieBiao[i]) > 20:
                    print("商品数量超过20，请重新输入")
                    break
                if int(ListOfLieBiao[i]) < 0:
                    print("商品数量有误，请重新输入")
                    break
                if i == GuYuan - 1:
                    _inputting = False
        for i in range(0, int(GuYuan)):
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            time.sleep(1.5)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            delay(0.8)
            press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            time.sleep(1)
            for j in range(0, int(ListOfLieBiao[i])):
                press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
                delay(0.2)
                press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
                delay(0.3)
                press_key(hwnd, win32con.VK_NUMPAD8, 0.02)
                delay(0.1)
                press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
                delay(1)
                press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
                delay(0.1)
                if my_cur is None:
                    input("请将鼠标移动到价格位置上，按回车键继续")
                    my_cur = win32api.GetCursorPos()
                win32api.SetCursorPos(my_cur)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
                delay(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
                win32print(pyperclip.paste(), i, j)
                delay(0.1)
                press_key(hwnd, win32con.VK_RETURN, 0.05)
                delay(0.1)
                press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
                delay(0.1)
                press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
                delay(0.1)
                press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
                delay(0.1)
                press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
                delay(0.1)
            print("第%s位雇员商品价格更改完毕" % (i+1))
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.5)
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.5)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            time.sleep(1.5)
            for j in range(0, i+1):
                press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
                delay(0.1)
        press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
        print("全部雇员商品价格更改完毕")
    elif mode == "2":
        press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
        lie_biao = input("雇员有几件商品？请输入数字：")
        for i in range(0, int(lie_biao)):
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            delay(0.2)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            delay(0.3)
            press_key(hwnd, win32con.VK_NUMPAD8, 0.02)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            delay(1)
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.1)
            if my_cur is None:
                input("请将鼠标移动到价格位置上，按回车键继续")
                my_cur = win32api.GetCursorPos()
            win32api.SetCursorPos(my_cur)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
            delay(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
            win32print(pyperclip.paste(), 0, i)
            delay(0.1)
            press_key(hwnd, win32con.VK_RETURN, 0.05)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            delay(0.1)
            press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
            delay(0.1)
        print("全部商品价格更改完毕")
    input("按回车键退出")
    exit()
