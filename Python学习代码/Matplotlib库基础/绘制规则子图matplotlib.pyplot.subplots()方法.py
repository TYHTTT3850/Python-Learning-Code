import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('pgf') #修改绘图后端以确保中文支持，但pgf不支持交互式绘图，所以只能通过保存的方式绘制。
plt.rc('text', usetex=True) #启用tex渲染

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

"""--------------------绘制2×2的子图--------------------"""
fig, axs = plt.subplots(2, 2) #fig代表整个绘图窗口，axs是由所有子图的位置组成的数组
# 第一行第一列子图
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Subplot 1', fontsize=12,fontproperties='Times New Roman') #为每个子图加标题并设置字号和字体
axs[0, 0].set_xlabel('$x$')
axs[0, 0].set_ylabel('$y$')

# 第一行第二列子图
axs[0, 1].plot(x, -y)
axs[0, 1].set_title('Subplot 2', fontsize=12,fontproperties='Times New Roman')
axs[0, 1].set_xlabel('$x$')
axs[0, 1].set_ylabel('$y$')

# 第二行第一列子图
axs[1, 0].plot(-x, y)
axs[1, 0].set_title('Subplot 3', fontsize=12,fontproperties='Times New Roman')
axs[1, 0].set_xlabel('$x$')
axs[1, 0].set_ylabel('$y$')

# 第二行第二列子图
axs[1, 1].plot(-x, -y)
axs[1, 1].set_title('Subplot 4', fontsize=12,fontproperties='Times New Roman')
axs[1, 1].set_xlabel('$x$')
axs[1, 1].set_ylabel('$y$')

# 图片整体设置项
plt.subplots_adjust(hspace=0.5) #调整子图间的垂直方向间距
plt.subplots_adjust(wspace=0.5) #调整子图间的水平方向间距
fig.suptitle("规则子图绘制",fontproperties='SimSun') #设置图片总标题并指定中文字体为宋体，否则出错
fig.savefig('规则子图.pdf', format='pdf')