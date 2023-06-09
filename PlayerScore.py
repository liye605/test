import csv
import lxml.etree
import requests

#以浏览器的身份发送请求
url = 'https://nba.hupu.com/stats/players'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}
response = requests.get(url,headers=headers)
print(response.text)
response.encoding = 'utf-8'
#if response.ok:
#    print("请求成功")
#else:
#    print("请求失败")

#用lxml和XPath进行解析XML文件
html_doc = response.text
tree = lxml.etree.HTML(html_doc)

#将需要解析的链接整合成一个列表
htmls = ["https://nba.hupu.com"+tree.xpath("/html/body/div[3]/div[4]/div/div/span[1]/a/@href")[0]]            #得分

#对于每个链接取得相应的数据（用for循环获取）
for href in htmls:
    print(href)  #打印出相应的网址
    resp = requests.get(href)
    resp.encoding = 'utf-8'
    kidhtml = lxml.etree.HTML(resp.text)
    trs = kidhtml.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr")  #解析整个表

    if href == htmls[0]:
        f1 = open("Score.csv", 'w', newline="", encoding='utf-8')
        table_writer = csv.writer(f1)

        #选择需要的列
        table_writer.writerow([trs[0].xpath("./td[2]/text()")[0],
                             trs[0].xpath("./td[3]/text()")[0],
                               trs[0].xpath("./td[4]/text()")[0],
                             trs[0].xpath("./td[6]/text()")[0],
                               trs[0].xpath("./td[8]/text()")[0],
                             trs[0].xpath("./td[10]/text()")[0],
                               trs[0].xpath("./td[11]/text()")[0],
                             trs[0].xpath("./td[12]/text()")[0]])

        for tr in trs[1:]:
            name = tr.xpath("./td[2]/a/text()")[0]
            team = tr.xpath("./td[3]/a/text()")[0]
            score = tr.xpath("./td[4]/text()")[0]
            hitPossibility = round(float(tr.xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3)   #调整百分数
            threeHitPossibility = round(float(tr.xpath("./td[8]/text()")[0].split("%")[0]) / 100, 3)
            twoHitPossibility = round(float(tr.xpath("./td[10]/text()")[0].split("%")[0]) / 100, 3)
            times = tr.xpath("./td[11]/text()")[0]
            time = tr.xpath("./td[12]/text()")[0]

            table_writer.writerow([ name, team, score, hitPossibility, threeHitPossibility, twoHitPossibility,times,time])

'''
            if (i < 5):

                resp1 = requests.get(tr.xpath("./td[2]/a/@href")[0])
                print(resp1)
                resp1.encoding = 'utf-8'
                kidhtml1 = lxml.etree.HTML(resp1.text)

                trss = kidhtml1.xpath(
                    "/html/body/div[3]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr   ")

                f2 = open('ScoreFouth.csv', 'a', newline="", encoding='utf-8')
                csv_writerr = csv.writer(f2)

                name = kidhtml1.xpath("/html/body/div[3]/div[3]/div[1]/div[1]")

                if (j == 0):
                    j = j + 1
                    csv_writerr.writerow(
                        ["球员", trss[1].xpath("./td[15]/text()")[0], trss[1].xpath("./td[4]/text()")[0],
                         trss[1].xpath("./td[6]/text()")[0], trss[1].xpath("./td[8]/text()")[0],
                         trss[1].xpath("./td[9]/text()")[0], trss[1].xpath("./td[10]/text()")[0],
                         trss[1].xpath("./td[11]/text()")[0], trss[1].xpath("./td[12]/text()")[0]])

                csv_writerr.writerow([name[0].xpath("./h2/text()")[0], trss[2].xpath("./td[15]/text()")[0],
                                      round(float(trss[2].xpath("./td[4]/text()")[0].split("%")[0]) / 100, 3),
                                      round(float(trss[2].xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3),
                                      round(float(trss[2].xpath("./td[8]/text()")[0].split("%")[0]) / 100, 3),
                                      trss[2].xpath("./td[9]/text()")[0], trss[2].xpath("./td[10]/text()")[0],
                                      trss[2].xpath("./td[11]/text()")[0], trss[2].xpath("./td[12]/text()")[0]])

    if href == htmls[1]:
        f2 = open("ThreeBall.csv", 'w', newline="", encoding='utf-8')
        table_writer1 = csv.writer(f2)

        #选择需要的列
        table_writer1.writerow([trs[0].xpath("./td[1]/text()")[0], trs[0].xpath("./td[2]/text()")[0],
                             trs[0].xpath("./td[3]/text()")[0], trs[0].xpath("./td[4]/text()")[0],
                             trs[0].xpath("./td[6]/text()")[0], trs[0].xpath("./td[8]/text()")[0],
                             trs[0].xpath("./td[10]/text()")[0], trs[0].xpath("./td[11]/text()")[0],
                             trs[0].xpath("./td[12]/text()")[0]])

        i = 0
        j = 0
        for tr in trs[1:]:
            i = i+1
            id = tr.xpath("./td[1]/text()")[0]
            name = tr.xpath("./td[2]/a/text()")[0]
            team = tr.xpath("./td[3]/a/text()")[0]
            score = tr.xpath("./td[4]/text()")[0]
            hitPossibility = round(float(tr.xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3)   #调整百分数
            threeHitPossibility = round(float(tr.xpath("./td[8]/text()")[0].split("%")[0]) / 100, 3)
            twoHitPossibility = round(float(tr.xpath("./td[10]/text()")[0].split("%")[0]) / 100, 3)
            times = tr.xpath("./td[11]/text()")[0]
            time = tr.xpath("./td[12]/text()")[0]

            table_writer.writerow([id, name, team, score, hitPossibility, threeHitPossibility, twoHitPossibility,times,time])
'''
