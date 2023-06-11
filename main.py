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


def process_input_lie_biao(input_str):
    valid_chars = set("0123456789- ")

    # 检查输入的合法性
    if set(input_str) - valid_chars:
        print("输入的字符包含非法字符，请重新输入。")
        return None

    # 将输入的字符转换为一个列表
    items = input_str.split()
    result = []

    for item in items:
        if '-' in item:
            # 处理形如 "3-8" 的输入
            start, end = map(int, item.split('-'))
            # 保证start小于end
            if start > end:
                start, end = end, start
            result.extend(range(start, end + 1))
        else:
            # 处理单个数字的输入
            result.append(int(item))

    # 去重和排序
    result = sorted(set(result))

    return result


# 检查输入列表合法性
def check_input_list(input_list):
    illegal_numbers = [num for num in input_list if num < 1 or num > 20]

    if illegal_numbers:
        print("非法序列:", illegal_numbers)
        choice = input("请选择操作：输入1剔除非法数字并返回剩余数字列表，输入2返回 false。")

        if choice == "1":
            valid_numbers = [num for num in input_list if num >= 1 and num <= 20]
            print("剩余序列:", valid_numbers)
            return valid_numbers
        elif choice == "2":
            return None
        else:
            print("无效的选择！请更正！")
    else:
        print("更改序列:", input_list)
        return input_list


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
            print("第%s位雇员商品价格更改完毕" % (i + 1))
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.5)
            press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
            delay(0.5)
            press_key(hwnd, win32con.VK_NUMPAD9, 0.05)
            time.sleep(1.5)
            for j in range(0, i + 1):
                press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
                delay(0.1)
        press_key(hwnd, win32con.VK_NUMPAD7, 0.05)
        print("全部雇员商品价格更改完毕")
    elif mode == "2":
        press_key(hwnd, win32con.VK_NUMPAD2, 0.02)
        lie_biao = None
        while lie_biao is None:
            lie_biao = input("雇员有几件商品？请输入数字，或用形如“3-8 10 13-20”的形式指定更改物品：")
            lie_biao = process_input_lie_biao(lie_biao)
            if lie_biao is None:
                continue
            lie_biao = check_input_list(lie_biao)
        for i in range(1, lie_biao[-1] + 1):
            if i in lie_biao:
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
                win32print(pyperclip.paste(), 0, i - 1)
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
