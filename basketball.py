from matplotlib import pyplot as plt
from matplotlib.patches import Arc,Circle,Rectangle

# 图上的中文和负号正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

def draw_ball_field(color='pink',lw=2):

    #绘制篮球场

    #新建一个大小为(6,6)的绘图窗口
    plt.figure(figsize=(6,6))
    #获得当前的Axes对象ax,进行绘图
    ax=plt.gca()

    #对篮球场进行底色填充
    lines_outer_rec=Rectangle(xy=(-250,-47.5),width=500,height=470,linewidth=lw,color='white',fill=True)
    #设置篮球场填充图层为最底层
    lines_outer_rec.set_zorder(0)
    #将rec添加进ax
    ax.add_patch(lines_outer_rec)

    #绘制篮筐,半径为7.5
    circle_ball=Circle(xy=(0,0),radius=7.5,linewidth=lw,color=color,fill=False)
    #将circle添加进ax
    ax.add_patch(circle_ball)

    #绘制篮板,尺寸为(60,1)
    plate=Rectangle(xy=(-30,-7.5),width=60,height=-1,linewidth=lw,color=color,fill=False)
    #将rec添加进ax
    ax.add_patch(plate)

    #绘制2分区的外框线,尺寸为(160,190)
    outer_rec=Rectangle(xy=(-80,-47.5),width=160,height=190,linewidth=lw,color=color,fill=False)
    #将rec添加进ax
    ax.add_patch(outer_rec)

    #绘制罚球区域圆圈,半径为80
    circle_punish=Circle(xy=(0,142.5),radius=80,linewidth=lw,color=color,fill=False)
    #将circle添加进ax
    ax.add_patch(circle_punish)

    #绘制三分线的左边线
    three_left_rec=Rectangle(xy=(-220,-47.5),width=0,height=140,linewidth=lw,color=color,fill=False)
    #将rec添加进ax
    ax.add_patch(three_left_rec)

    #绘制三分线的右边线
    three_right_rec=Rectangle(xy=(220,-47.5),width=0,height=140,linewidth=lw,color=color,fill=False)
    #将rec添加进ax
    ax.add_patch(three_right_rec)

    #绘制三分线的圆弧,圆心为(0,0),半径为238.66,起始角度为22.8,结束角度为157.2
    three_arc=Arc(xy=(0,0),width=477.32,height=477.32,theta1=22.8,theta2=157.2,linewidth=lw,color=color,fill=False)
    #将arc添加进ax
    ax.add_patch(three_arc)

    #绘制中场处的外半圆,半径为60
    center_outer_arc=Arc(xy=(0,422.5),width=120,height=120,theta1=180,theta2=0,linewidth=lw,color=color,fill=False)
    #将arc添加进ax
    ax.add_patch(center_outer_arc)

    #绘制中场处的内半圆,半径为20
    center_inner_arc=Arc(xy=(0,422.5),width=40,height=40,theta1=180,theta2=0,linewidth=lw,color=color,fill=False)
    #将arc添加进ax
    ax.add_patch(center_inner_arc)

    #绘制篮球场外框线,尺寸为(500,470)
    lines_outer_rec=Rectangle(xy=(-250,-47.5),width=500,height=470,linewidth=lw,color=color,fill=False)
    #将rec添加进ax
    ax.add_patch(lines_outer_rec)

    return ax

axs=draw_ball_field(color='pink',lw=2)

#设置坐标轴范围
axs.set_xlim(-250,250)
axs.set_ylim(422.5,-47.5)
#消除坐标轴刻度
axs.set_xticks([])
axs.set_yticks([])
#添加备注信息
plt.annotate('NBA球场半场图',xy=(100,160),xytext=(138,418))
plt.show()