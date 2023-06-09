import matplotlib.pyplot as plt
import numpy as np
import csv

# 图上的中文和负号正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据文件
def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        team_data = {}
        for row in reader:
            season = row["赛季"]
            if  int(season) >=2017 and int(season) <= 2022:
                team = row["赛季"]
                data = [
                    float(row["投篮"]),
                    float(row["三分"]),
                    float(row["罚球"]),
                    float(row["篮板"]),
                    float(row["助攻"]),
                    float(row["抢断"]),
                    float(row["盖帽"]),
                    float(row["失误"]),
                    float(row["犯规"]),
                ]
                team_data[team] = data
        return team_data

# 数据文件路径
file_path = "StephenCurry.csv"

# 读取数据
team_data = read_data(file_path)

# 轴标签
labels = ["投篮", "三分", "罚球","篮板","助攻","抢断","盖帽","失误","犯规"]

# 标题
title = "库里赛季能力分析雷达图"

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

# 将第一个标签放到最后，以使雷达图闭合
labels.append(labels[0])
angles.append(angles[0])

# 绘制雷达图
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
ax.set_title(title, pad=30, fontsize=25,c = 'pink',loc = 'center')

for team, data in team_data.items():
    # 将数据复制一份，以使雷达图闭合
    data = data + [data[0]]
    ax.plot(angles, data, label=team)

''' # 在雷达图上添加标签
    for label, angle, data_point in zip( angles, data):
        ax.annotate(
            label,
            xy=(angle, data_point),
            xytext=(angle, data_point + 0.1),  # 调整标签的位置
            ha='center',
            va='center',
            fontsize=8
        )'''

# 设置刻度标签
ax.set_xticks(angles)
ax.set_xticklabels(labels)

# 添加图例
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1))

# 显示图形
plt.show()
