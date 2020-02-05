#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# @Description: 机械工业出版社PDF下载，参考：https://github.com/Echowxsy/CMPEDUDownload
# @PreInstall: 
# @Author : https://www.bajins.com
# @File : cmpedu.py
# @Version: 1.0.0
# @Time : 2020/2/5 15:26
# @Project: reptile-python
# @Package: 
# @Software: PyCharm
import os
import re

import requests

catgories = {
    "AA01": "机械基础",
    "AA02": "机械设计",
    "AA03": "五金",
    "AA04": "工业设计",
    "AA05": "机械加工",
    "AA06": "数控技术",
    "AA07": "金属焊接\\切割与粘接",
    "AA08": "机电一体化",
    "AA09": "塑性成形",
    "AA10": "模具",
    "AA11": "铸造",
    "AA12": "锻压",
    "AA13": "热处理",
    "AA14": "机械设备与维修\\其他辅助工艺设备",
    "AA15": "表面工程",
    "AA16": "通用机械",
    "AA17": "专用机械",
    "AA18": "材料",
    "AA19": "检测技术",
    "AA20": "工程软件应用",
    "AA21": "生产管理及设备管理",
    "AA22": "能源与动力工程",
    "AA23": "制冷与空调",
    "AA24": "工业工程",
    "AA25": "机械工程其他",
    "AA26": "其他",
    "AB01": "电子电工技术综合",
    "AB02": "电工技术",
    "AB03": "电力系统",
    "AB04": "新能源",
    "AB05": "电子技术",
    "AB06": "电气自动化",
    "AB07": "通信工程",
    "AB08": "家用电器及办公设备",
    "AB09": "仪器仪表及检测技术",
    "AB10": "其他",
    "AG01": "化工技术",
    "AR02": "其他",
    "AN01": "养殖",
    "AN02": "种植",
    "AN04": "其他",
    "AC01": "英文原版书",
    "AC02": "计算机科学",
    "AC03": "计算机理论",
    "AC04": "软件工程",
    "AC05": "程序设计",
    "AC06": "计算机 网络",
    "AC07": "数据库",
    "AC08": "操作系统",
    "AC09": "家庭与办公用书",
    "AC10": "CAD CAM CAE",
    "AC11": "图形图像及多媒体",
    "AC12": "网络与通信",
    "AC13": "网站开发",
    "AC14": "Internet",
    "AC15": "计算机及网络设备",
    "AC16": "计算机硬件技术",
    "AC17": "考试认证",
    "AC18": "人工智能",
    "AC19": "大数据",
    "AC20": "云计算",
    "AC21": "物联网",
    "AC22": "ERP",
    "AC23": "其他",
    "HH01": "英语",
    "HH02": "各类词典",
    "HH03": "小语种",
    "HI01": "文化教育",
    "HM01": "考研",
    "HM02": "MBA",
    "HM03": "英语考级",
    "HM05": "出国英语考试",
    "HM07": "托福",
    "HM08": "雅思",
    "HM09": "职称",
    "HM10": "考博",
    "HM12": "财经类考试",
    "HM14": "心理咨询师考试",
    "HM16": "其他",
    "ZZ01": "其他",
    "AP01": "机械基础",
    "AP02": "机械工程",
    "AP03": "电工电子",
    "AP05": "汽车\\摩托车\\自行车",
    "AP10": "考证鉴定教材",
    "AP11": "其他",
    "AD01": "汽车研发技术",
    "AD02": "汽车销售",
    "AD03": "汽车管理",
    "AD04": "汽车维修",
    "AD05": "汽车生活",
    "AD06": "汽车文化",
    "AD07": "汽车考试",
    "AD09": "摩托车",
    "AD10": "电动自行车",
    "AD11": "大交通",
    "AD12": "其他",
    "AF01": "建筑理论",
    "AF02": "建筑设计",
    "AF03": "建筑表现",
    "AF04": "建筑文化",
    "AF05": "城市规划",
    "AF06": "装饰装修",
    "AF07": "建筑材料",
    "AF08": "园林景观",
    "AF09": "建筑结构",
    "AF10": "地基与基础",
    "AF11": "建筑施工",
    "AF12": "建筑管理",
    "AF13": "建筑造价",
    "AF14": "建筑设备",
    "AF15": "交通工程",
    "AF16": "房地产开发与管理",
    "AF17": "建筑考试",
    "AF18": "其他",
    "EE01": "经济",
    "EE02": "管理",
    "EE03": "营销",
    "EE04": "文化与传播",
    "EE05": "其他",
    "EZ01": "社科类专著",
    "EZ02": "社科类大众读物",
    "EZ03": "其他",
    "EV01": "心理学",
    "EV02": "人生哲理",
    "EV03": "其他",
    "ET01": "美术学",
    "ET02": "书法绘画",
    "ET06": "摄影",
    "ET08": "其他",
    "EU01": "文学",
    "KK02": "科普读物",
    "ZA01": "中国科技奖励年鉴",
    "ZA02": "中国机械工业年鉴",
    "ZA03": "中国农业机械工业年鉴",
    "ZA04": "中国电器工业年鉴",
    "ZA05": "中国机床工具工业年鉴",
    "ZA06": "中国工程机械工业年鉴",
    "ZA07": "中国通用机械工业年鉴",
    "ZA08": "中国重型机械工业年鉴",
    "ZA09": "中国机械通用零部件工业年鉴",
    "ZA10": "中国石油石化设备工业年鉴",
    "ZA11": "中国齿轮工业年鉴",
    "ZA12": "中国磨具工业年鉴",
    "ZA13": "中国塑料机械工业年鉴",
    "ZA14": "中国液压气动密封工业年鉴",
    "ZA15": "中国磨料磨具工业年鉴",
    "ZA16": "中国机电产品市场年鉴",
    "ZA17": "中国机械工业图鉴",
    "ZA18": "中国机械工业集团年鉴",
    "ZA19": "中国机械电子工业年鉴",
    "ZA20": "中国电池工业年鉴",
    "ZA21": "中国热处理行业年鉴",
    "ZA22": "中国工程机械年鉴",
    "ZA23": "中国农业机械年鉴",
    "ZB01": "机械工程手册",
    "ZB02": "电机工程手册",
    "ZB05": "电线电缆手册",
    "ZB06": "热处理手册",
    "ZB09": "建筑相关手册",
    "ZB11": "机械相关手册",
    "ZB12": "机电相关手册",
    "ZC01": "战略新兴产业研究与发展丛书",
    "ZC02": "国际电气工程先进技术译丛",
    "ZC03": "国际信息工程先进技术译丛",
    "ZC04": "国际制造业先进技术译丛",
    "ZC05": "国际环境工程先进技术译丛",
    "ZC06": "BIM思维与技术丛书",
    "ZC07": "汽车先进技术译丛",
    "ZC08": "汽车技术创新与研发系列丛书"
}
referer = "https://cmpebooks.s3.cn-north-1.amazonaws.com.cn/pdfReader/generic/build/pdf.worker.js"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/77.0.3865.75 Safari/537.36 "


def get_books():
    for category_code, category_name in catgories.items():
        if category_code[0] == "#":
            continue
        data = {"code": category_code, "page": 1, "limit": 1000, "px": "desc"}
        response = requests.post("http://ebooks.cmanuf.com/getBookCategoryInfo", data, timeout=15)
        if not response.status_code == 200:
            print(response.text)
            break
        for bookInfo in response.json()["module"]:
            cover = bookInfo["img"]
            if len(cover) <= 55 or "cmpebooks.s3.cn-north-1.amazonaws.com.cn" not in cover:
                continue
            cover = cover.replace("/Cover/", "/PDF/").replace("/cover/", "/pdf/")
            cover = re.sub(r"Cover1\.jpg|Cover2\.jpg|Cover2\.JPG", "2.pdf", cover)
            pdf_link = (re.sub(r"cover_front\.jpg|cover_front_L\.jpg", "L.pdf", cover))
            file_name = f'{(re.sub(r"  |/| ", "_", bookInfo["name"].strip()))}.pdf'
            print(pdf_link)
            print(file_name)
            directory = f"cmpedu/{category_code}-{category_name}"
            # 判断目录是否存在
            if not os.path.exists(directory):
                os.makedirs(directory)
            with requests.get(pdf_link, headers={'User-Agent': USER_AGENT, 'Referer': referer}) as rep:
                if not rep.status_code == 200:
                    print(rep.text)
                    break
                with open(filename, "wb") as f:
                    f.write(rep.content)


if __name__ == "__main__":
    # get_books()
    response = requests.get("https://raw.githubusercontent.com/Echowxsy/CMPEDUDownload/master/downloads.txt")
    for text in re.split(r"^h|\nh", response.text):
        arr = re.sub(r"\t|referer=|out=downloads", "", text).split("\n")
        if not arr or len(arr) == 0 or arr[0] == "" or len(arr[0]) == 0:
            continue
        pdf_link = f"h{arr[0]}"
        filename = f"cmpedu{arr[2]}"
        directory = filename[:filename.rfind("/")]
        print(filename)
        # 判断目录是否存在
        if not os.path.exists(directory):
            os.makedirs(directory)
        with requests.get(pdf_link, headers={'User-Agent': USER_AGENT, 'Referer': referer}) as rep:
            if not rep.status_code == 200:
                print(rep.text)
                break
            with open(filename, "wb") as f:
                f.write(rep.content)
