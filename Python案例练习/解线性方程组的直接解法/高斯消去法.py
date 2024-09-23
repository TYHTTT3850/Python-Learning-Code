import numpy as np
# 高斯消元法
def gauss1(A,b):
    n = len(b)
    for i in range(n): #消元
        for j in range(i+1,n):
            m = A[j,i]/A[i,i]
            A[j] = A[j] - m*A[i]
            b[j] = b[j] - m*b[i]
    print(A)
    print(b)
    if A[n - 1,n - 1] == 0: #求解
        print("无解")
    else:
        x[n - 1] = b[n - 1] / A[n - 1,n - 1]
        for k in range(n - 2, -1, -1):
            s = A[k,k + 1:] @ x[k + 1:]
            x[k] = (b[k] - s) / A[k,k]
    print(x)
A = np.array([[1,0,0],[2,2,2],[4,4,5]],dtype=np.float64)
b = np.array([[2],[5],[9]],dtype=np.float64)
x = np.zeros((len(b),1),dtype=np.float64)
gauss1(A,b)
