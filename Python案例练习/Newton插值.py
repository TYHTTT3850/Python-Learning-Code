"""
已知 ln(x) 在 0.4 0.5 0.6 0.7 0.8处的值，求在 0.54 处的近似值
"""

import numpy as np

# 取0.5，0.6，0.4三个点
diff_x = np.array([[0.5],[0.6],[0.4]])
diff_table = np.array([[-0.6931],[-0.5108],[-0.9163]])

# 下三角系数阵
A = np.tril(np.ones([len(diff_x),len(diff_x)]))
for i in range(1,len(diff_x)):
    for j in range(i,len(diff_x)):
        A[j,i] = (diff_x[j,0] - diff_x[i-1,0])*(A[j,i-1])

# 解出系数
a = np.linalg.solve(A,diff_table)

# 求近似值
x = 0.54
print(a[0]+a[1]*(x-diff_x[0])) # 线性插值
print(a[0]+a[1]*(x - diff_x[0])+a[2]*(x - diff_x[0])*(x - diff_x[1])) # 抛物线插值