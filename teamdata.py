import requests
import lxml.etree
import csv

url = 'https://nba.hupu.com/stats/teams'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

#使用lxml和XPath解析HTML文档
html_doc = lxml.etree.HTML(response.text)

#查找包含球队数据的表格行
trs = html_doc.xpath('//*[@id="data_js_sort"]/tbody/tr')

#定义新的表头行
new_header = ["排名", "球队", "投篮", "三分", "罚篮", "篮板","进攻","防守","助攻", "得分"]

#打开CSV文件进行写入
with open('team_stats.csv', 'w', newline='', encoding='utf-8') as f:
   csv_writer = csv.writer(f)

   # 写入新的表头行
   csv_writer.writerow(new_header)

   # 写入每行数据
   for i in range(2,31):
       csv_writer.writerow([
           trs[i].xpath('./td[1]/text()')[0],
           trs[i].xpath('./td[2]/a/text()')[0],
           round(float(trs[i].xpath("./td[3]/text()")[0].split("%")[0]) / 100, 3),
           round(float(trs[i].xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3),
           round(float(trs[i].xpath("./td[9]/text()")[0].split("%")[0]) / 100, 3),
           trs[i].xpath('./td[12]/text()')[0],
           trs[i].xpath('./td[13]/text()')[0],
           trs[i].xpath('./td[14]/text()')[0],
           trs[i].xpath('./td[15]/text()')[0],
           trs[i].xpath('./td[20]/text()')[0],
       ])



