# -*- coding=utf-8 -*-
"""
Time:        2022/12/18 21:40
Version:     V 0.0.2
File:        xxt.py
Describe:
Author:      Lanyu
E-Mail:      silence2021silence@163.com
Gitee link:  https://gitee.com/silence2021silence/
Github link: https://github.com/silence2021silence/
"""

import time
import pyautogui
import os


def get_task():
    txt_file = open("task.txt", "r", encoding="utf-8")
    lines = txt_file.readlines()
    task_list = []
    for i in range(len(lines) - 2):
        j = lines[i + 2].replace("\n", "")
        k = lines[0].replace("\n", "")
        m = lines[1].replace("\n", "")
        task_list.append("img/" + j)
        task_list.append("img/" + k)
        task_list.append("img/" + m)
    return task_list


def click(img):
    while True:
        if not os.path.exists(img):
            print("找不到" + img + "文件")
            input("输入任意内容退出\n")
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, interval=0.2, duration=0.5, button="left")
            break
        else:
            if img == "img/replay.png":
                print("等待播放完毕")
                time.sleep(1)
            elif img == "img/play.png":
                time.sleep(2)
                pyautogui.moveTo(1400, 700, duration=0.5)
                pyautogui.scroll(-200)
                print("寻找播放键")
            else:
                time.sleep(2)
                pyautogui.moveTo(1700, 700, duration=0.5)
                pyautogui.scroll(-100)
                print("寻找下一节")


def main():
    task_list = get_task()
    i = 0
    while i < len(task_list):
        img = task_list[i]
        click(img)
        print("点击", img)
        i += 1


if __name__ == "__main__":
    if not os.path.exists("img"):
        print("找不到img文件夹")
        input("输入任意内容退出\n")
    if not os.path.exists("task.txt"):
        print("找不到task.txt文件")
        input("输入任意内容退出\n")
    main()
