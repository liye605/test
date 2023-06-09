import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn import preprocessing

# 图上的中文和负号正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取球员数据
players = pd.read_csv("Score.csv", encoding='utf-8')

# 数据标准化处理
X = preprocessing.minmax_scale(players[['得分', '罚球命中率', '命中率', '三分命中率']])
X = pd.DataFrame(X, columns=['得分', '罚球命中率', '命中率', '三分命中率'])

# 构造自定义函数，用于绘制不同k值和对应总的簇内离差平方和的折线图
def plot_k_sse(X, clusters):
    K = range(1, clusters+1)
    TSSE = []
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        SSE = kmeans.inertia_
        TSSE.append(SSE)

    plt.plot(K, TSSE, 'b^-')
    plt.xlabel('簇的个数')
    plt.ylabel('簇内离差平方和之和')
    plt.show()

# 绘制不同k值和对应总的簇内离差平方和的折线图
plot_k_sse(X, 15)

# 构造自定义函数，用于绘制不同k值和对应轮廓系数的折线图
def plot_k_silhouette(X, clusters):
    K = range(2, clusters+1)
    S = []
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=10)
        kmeans.fit(X)
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X, labels)
        S.append(silhouette_avg)

    plt.plot(K, S, 'b^-')
    plt.xlabel('簇的个数')
    plt.ylabel('轮廓系数')
    plt.show()

# 绘制不同k值和对应轮廓系数的折线图
plot_k_silhouette(X, 10)

# 将球员数据集聚为4类
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
players['cluster'] = kmeans.labels_
# 构建空列表，用于存储三个簇的簇中心
centers = []
for i in players.cluster.unique():
    centers.append(players.loc[players.cluster == i,['得分','罚球命中率','命中率','三分命中率']].mean())
# 将列表转换为数组，便于后面的索引取数
centers = np.array(centers)

markers = ['^', 's', 'o', 'D']  # 每个簇中心对应的形状

for i in range(4):
    cluster_players = players[players['cluster'] == i]
    plt.scatter(players['得分'], players['命中率'], c=players['cluster'],cmap='viridis', alpha=0.8)
    plt.scatter(centers[i, 0], centers[i, 2], c='pink', marker=markers[i], s=180)
plt.xlabel('得分')
plt.ylabel('命中率')
plt.legend()
plt.show()

# 打印每个簇的球员信息
for i in range(4):
    cluster_players = players[players['cluster'] == i]
    print(f"Cluster {i+1}:\n{cluster_players}\n")
