import numpy as np

def Trapezoidal_integral(f,a,b,eps):#f:积分函数，a:积分下限，b:积分上限，eps:精度控制
    #初始化T1和T2
    T1 = (b-a)*(f(a)+f(b))/2
    T2 = 0

    #从分为2段区间的情况开始
    for i in range(1, int(1 / eps)+1):
        n = 2 ** i  #表示分段区间数
        h = (b - a) / n  #表示分段区间间隔

        # 分段梯形求积
        for t2 in range(0, n): #遍历所有分段区间
            T2 += h * (f(a + t2 * h) + f(a + (t2 + 1) * h)) / 2

        # 判断结果是否符合要求
        if np.abs(T2 - T1) < eps:
            return n, T2
            break #返回后退出循环
        elif i == int(1 / eps): #在最大分段区间数的情况下仍无满足要求的近似值，则返回此时的近似值
            return n, T2
        else:
            T1 = T2 #T2的值保存至T1
            T2 = 0 #重置T2的值
            continue

# 定义求积函数
def f(x):
    if x == 0:
        return 1
    else:
        return np.sin(x)/x

eps = 0.000001
n, I = Trapezoidal_integral(f,0,1,eps)
print(n,I)
