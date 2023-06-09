import pandas as pd
import matplotlib.pyplot as plt

# 图上的中文和负号正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV文件
data = pd.read_csv('team_stats.csv')

# 选择需要调整的数据列
selected_columns = ['投篮', '三分', '罚篮','篮板', '进攻','防守','助攻','得分']

# 对数据列进行缩放
scaled_data = data[selected_columns].copy()
scaled_data[['投篮', '三分','罚篮']] *= 100
scaled_data[['得分']] -=70
scaled_data[['罚篮']] -=35
scaled_data[['进攻']] +=20

# 绘制箱型图并设置方框填充颜色和中位数线属性
plt.figure(figsize=(10, 8))
boxprops = dict(facecolor='lightblue')  # 设置方框填充颜色
medianprops = dict(color='red', linewidth=2)  # 设置中位数线颜色为红色，线宽为2

# 绘制箱型图，设置方框填充颜色和中位数线属性
boxplot = plt.boxplot(scaled_data.values, patch_artist=True, medianprops=medianprops,labels = selected_columns)
# 调整横轴标签的字体大小
plt.xticks(fontsize=15)

# 设置方框填充颜色
for patch in boxplot['boxes']:
    patch.set_facecolor('lightblue')
plt.xlabel('指标',fontsize=18)
plt.ylabel('数值',fontsize=18)
plt.title('球队数据箱型图',pad=30, fontsize=25,c = 'k',loc = 'center')
plt.show()
