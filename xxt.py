# -*- coding=utf-8 -*-
"""
Time:        2022/12/19 16:30
Version:     V 0.0.4
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
import requests


def get_task():
    txt_file = open("task.txt", "r", encoding="utf-8")
    lines = txt_file.readlines()
    task_list = []
    for i in range(len(lines) - 2):
        part = lines[i + 2].replace("\n", "")
        play_key = lines[0].replace("\n", "")
        replay_key = lines[1].replace("\n", "")
        task_list.append("img/" + part)
        task_list.append("img/" + play_key)
        task_list.append("img/" + replay_key)
    play_key_path = task_list[1]
    replay_key_path = task_list[2]
    return task_list, play_key_path, replay_key_path


def click(img, play_key_path, replay_key_path):
    while True:
        if not os.path.exists(img):
            print("找不到" + img + "文件")
            input("请输入任意内容后按回车键退出\n")
            exit()
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, interval=0.2, duration=0.5, button="left")
            break
        else:
            if img == replay_key_path:
                print("等待播放完毕")
                time.sleep(1)
            elif img == play_key_path:
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
    if not os.path.exists("img"):
        print("找不到img文件夹")
        input("请输入任意内容后按回车键退出\n")
        exit()
    if not os.path.exists("task.txt"):
        print("找不到task.txt文件")
        input("请输入任意内容后按回车键退出\n")
        exit()
    task_list, play_key_path, replay_key_path = get_task()
    i = 0
    while i < len(task_list):
        img = task_list[i]
        click(img, play_key_path, replay_key_path)
        print("点击", img)
        i += 1


def welcome():
    print("欢迎使用本程序，技术支持与意见反馈请关注微信公众号“geeklanyu”或联系邮箱“silence2021silence@163.com”")
    print("免责声明：本程序仅供学习、研究与娱乐使用，使用本程序违反相关法律或相关规章制度的与作者无关，禁止用于任何商业用途。")
    text = input("请输入“同意”或“不同意”后按回车键\n")
    if text != "同意":
        exit()
    version = "v0.0.4"
    new_version = requests.get("https://zhangkelan.com/xxt-update.html").text
    if version != new_version:
        print("本程序有新版本，请前往https://gitee.com/silence2021silence/下载最新版本")
        input("请输入任意内容后按回车键退出\n")
        exit()


if __name__ == "__main__":
    welcome()
    main()
