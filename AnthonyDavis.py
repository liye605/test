import requests
import csv
import lxml.etree

url = 'https://nba.hupu.com/players/anthonydavis-3638.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 使用lxml和XPath解析HTML文档
html_doc = lxml.etree.HTML(response.text)

# 查找包含库里赛季数据的表格行
trs = html_doc.xpath("/html/body/div[3]/div[3]/div[1]/div[3]/div[3]/div/div/div[1]/table[2]/tbody/tr")

# 定义新的表头行
new_header = [
    "赛季","时间", "投篮", "三分", "罚球", "篮板", "助攻", "抢断", "盖帽", "失误","犯规","得分"
]

# 打开CSV文件进行写入
with open('AnthonyDavis.csv', 'w', newline="", encoding='utf-8') as f1:
    csv_writer = csv.writer(f1)

    # 写入新的表头行
    csv_writer.writerow(new_header)

    # 写入每行数据
    for i in range(1, 13):
        csv_writer.writerow([
            trs[i].xpath("./td[1]/text()")[0],
            trs[i].xpath("./td[5]/text()")[0],
            trs[i].xpath("./td[6]/text()")[0].split('-')[0],
            trs[i].xpath("./td[8]/text()")[0].split('-')[0],
            trs[i].xpath("./td[10]/text()")[0].split('-')[0],
            trs[i].xpath("./td[12]/text()")[0],
            trs[i].xpath("./td[13]/text()")[0],
            trs[i].xpath("./td[14]/text()")[0],
            trs[i].xpath("./td[15]/text()")[0],
            trs[i].xpath("./td[16]/text()")[0],
            trs[i].xpath("./td[17]/text()")[0],
            trs[i].xpath("./td[18]/text()")[0]
        ])

