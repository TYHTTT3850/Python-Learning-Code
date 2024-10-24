"""
面向对象风格的绘图步骤：
1、使用 plt.figure()或 plt.subplots()方法创建 Figure对象。
   plt.figure()方法可以设置图形的尺寸、分辨率等参数。

2、通过 Figure对象的 add_subplot()或 add_axes()方法创建 Axes对象。
   add_subplot()方法通常用于创建常规的网格布局，而 add_axes()方法则可以创建任意位置和大小的 Axes对象。

3、绘制数据，Axes对象的 plot()方法。

4、设置图形属性

5、显示或保存图形
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. 创建 Figure 对象
fig = plt.figure()

# 2. 添加 Axes 对象
axe1 = fig.add_axes([0.15, 0.1, 0.8, 0.8]) #数值分别对应[left, bottom, width, height]
"""
left: Axes 左下角的 x 坐标(相对于 Figure 宽度，范围从 0 到 1)
bottom: Axes 左下角的 y 坐标(相对于 Figure 高度，范围从 0 到 1)
width: Axes 的宽度(相对于 Figure 宽度，范围从 0 到 1)
height: Axes 的高度(相对于 Figure 高度，范围从 0 到 1)
"""

# 3. 绘制数据
x = np.linspace(0, 10, 100)
axe1.plot(x, np.sin(x), label='sin(x)', color='blue')
axe1.plot(x, np.cos(x), label='cos(x)', color='red')

# 4. 设置图形属性
axe1.set_title('Sine Function', fontsize=16)  # 设置标题
axe1.set_xlabel('X-axis', fontsize=12)  # 设置 X 轴标签
axe1.set_ylabel('Y-axis', fontsize=12)  # 设置 Y 轴标签
axe1.legend()  # 添加图例
axe1.grid(True)  # 显示网格

# 5. 显示或保存图形
plt.show()  # 显示图形