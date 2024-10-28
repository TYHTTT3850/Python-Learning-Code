import numpy as np

def Trapezoidal_integral(f,a,b,eps):#f:积分函数，a:积分下限，b:积分上限，eps:精度控制
    T = np.zeros(int(1/eps))
    T[1] = (b-a)*(f(a)+f(b))/2 #分段区间为1时积分近似值
    for i in range(1,int(1/eps)): #从分为2段区间开始
        n = 2**i #表示分段区间数
        h = (b-a)/n #分段区间间隔
        for t2 in range(0,n):
            T[i] += h*(f(a+t2*h)+f(a+(t2+1)*h))/2 #分段梯形求积
        if np.abs(T[i]-T[i-1]) < eps:
            return n, T[i]
        else:
            continue

def f(x):
    if x == 0:
        return 1
    else:
        return np.sin(x)/x

eps = 0.001
n, I = Trapezoidal_integral(f,0,1,eps)
print(n,I)