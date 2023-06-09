import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 图上的中文和负号正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据文件
curry_data = pd.read_csv("StephenCurry.csv")
durant_data = pd.read_csv("KevinDurant.csv")
james_data = pd.read_csv("LeBronJames.csv")
anthony_data = pd.read_csv("AnthonyDavis.csv")

# 提取2022年的数据
curry_data_2022 = curry_data[curry_data['赛季'] == 2022]
durant_data_2022 = durant_data[durant_data['赛季'] == 2022].tail(1)
james_data_2022 = james_data[james_data['赛季'] == 2022]
anthony_data_2022 = anthony_data[anthony_data['赛季'] == 2022]

# 合并四位球员的数据
merged_data = pd.concat([curry_data_2022, durant_data_2022, james_data_2022, anthony_data_2022])

# 选择需要的指标列
selected_columns = ["投篮", "三分", "罚球", "篮板", "助攻", "抢断", "盖帽", "失误", "犯规", "得分"]
selected_data = merged_data[selected_columns]

# 写入新文件
selected_data.to_csv("2022年球员数据.csv", index=False)

selected_data["得分"] = selected_data["得分"]-15
selected_data["盖帽"] = selected_data["盖帽"]*5
selected_data["抢断"] = selected_data["抢断"]*5
selected_data["犯规"] = selected_data["犯规"]*3
selected_data["失误"] = selected_data["失误"]*3
selected_data["三分"] = selected_data["三分"]*2

# 绘制第一个图
categories_1 = ['投篮', '三分', '罚球', '篮板']
num_players = len(selected_data)
bar_width = 0.2
index = np.arange(len(categories_1))

fig, ax = plt.subplots(figsize=(10, 8))

players = ["库里","杜兰特","詹姆斯","安东尼"]
for i in range(num_players):
    values = selected_data.iloc[i, :4].tolist()
    ax.bar(index + i * bar_width, values, bar_width,label=players[i])

# 设置x轴标签和标题
ax.set_xlabel('指标')
ax.set_ylabel('数值')
ax.set_title('2022年球员数据条形图1',pad=30, fontsize=25,c = 'k',loc = 'center')

# 设置刻度标签
ax.set_xticks(index + bar_width * (num_players - 1) / 2)
ax.set_xticklabels(categories_1)

# 添加图例
ax.legend()

# 展示第一个图
plt.show()

# 绘制第二个图
categories_2 = ['失误', '抢断', '犯规', '盖帽','助攻','得分']
index_2 = np.arange(len(categories_2))

fig, ax = plt.subplots(figsize=(10, 8))

players1 = ["库里","杜兰特","詹姆斯","安东尼"]
for i in range(num_players):
    values = selected_data.iloc[i, 4:].tolist()
    ax.bar(index_2 + i * bar_width, values, bar_width,label = players1[i])

# 设置x轴标签和标题
ax.set_xlabel('指标')
ax.set_ylabel('数值')
ax.set_title('2022年球员数据条形图2', pad=30, fontsize=25,c = 'k',loc = 'center')

# 设置刻度标签
ax.set_xticks(index_2 + bar_width * (num_players - 1) / 2)
ax.set_xticklabels(categories_2)

# 添加图例
ax.legend()

# 展示第二个图
plt.show()