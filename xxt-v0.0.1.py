# -*- coding=utf-8 -*-
"""
Time:        2023/3/27 19:40
Version:     V 0.0.1
File:        xxt-v0.0.1.py
Describe:    
Author:      Lanyu
E-Mail:      silence2021silence@163.com
Github link: https://github.com/silence2021silence/
Gitee link:  https://gitee.com/silence2021silence/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import time


def click(xpath):
    while True:
        try:
            driver.find_element(By.XPATH, value=xpath).click()
        except:
            time.sleep(0.1)
        else:
            break


def find(xpath):
    while True:
        try:
            element = driver.find_elements(By.XPATH, value=xpath)
        except:
            time.sleep(0.1)
        else:
            break
    return element


def get_length(xpath):
    while True:
        html = driver.page_source
        tree = etree.HTML(html)
        length_str = tree.xpath(xpath)[0]
        h_m_s = [int(i) for i in length_str.split(":")]
        # 转换为秒
        if len(h_m_s) == 3:
            s = int(h_m_s[0]) * 3600 + int(h_m_s[1]) * 60 + int(h_m_s[2])
            if s != 0:
                print("视频时长获取完毕")
                return s
        elif len(h_m_s) == 2:
            s = int(h_m_s[0]) * 60 + int(h_m_s[1])
            if s != 0:
                print("视频时长获取完毕")
                return s


driver = webdriver.Chrome()
driver.get("http://i.mooc.chaoxing.com/space")
input("登录完成并打开课程后按回车")
# 切句柄
windows = driver.window_handles
driver.switch_to.window(windows[-1])

html = driver.page_source
tree = etree.HTML(html)
# 获取章节
parts_obj = tree.xpath("//div[@id='coursetree']/ul//ul/li/div")

parts = []
for i in parts_obj:
    # 章节名
    part_name = "".join(i.xpath("span[1]//text()"))
    try:
        # 任务点数
        task_points = i.xpath("span[2]/span[@class='orangeNew']/text()")[0]
    except IndexError:
        task_points = 0
        part_id = 0
    else:
        # 章节id
        part_id = i.xpath("@id")[0]
        task_points = int(task_points)
    parts.append([part_name, task_points, part_id])

for i in parts:
    if i[1] != 0:
        print("正在处理 [{}]，共[{}]个任务点".format(i[0], i[1]))
        # 点击章节
        click("//div[@id='{}']".format(i[2]))
        time.sleep(2)
        # 切入iframe
        driver.switch_to.frame(find("//iframe[@id='iframe']")[0])
        # 获取未完成的视频所属的框架
        # 框架selenium对象
        # 过滤已完成的视频和播放不了的视频
        iframe_s_objs = find("//div[@class='ans-attach-ct'][@id]/iframe[@class='ans-attach-online ans-insertvideo-online']")
        for j in iframe_s_objs:
            # 切入iframe
            driver.switch_to.frame(j)
            # 点击播放
            click("//button[@title='播放视频']")
            # 获取视频长度并等待
            print("等待播放完毕")
            time.sleep(get_length("//span[@class='vjs-duration-display']/text()"))
            time.sleep(5)
            # 切出iframe
            driver.switch_to.parent_frame()
        # 切出iframe
        driver.switch_to.parent_frame()
        print("[{}] 处理完毕".format(i[0]))
