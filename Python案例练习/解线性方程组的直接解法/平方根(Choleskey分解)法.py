import numpy as np
def Choleskey(A,b):
    n = len(b)
    for i in range(n): # 取A的下三角形部分
        A[0:i,i] = 0
    L = np.zeros([n,n])

    # 求L
    L[0,0] = np.sqrt(A[0,0]) # 处理第一列
    L[1,0] = A[1,0]/L[0,0]
    L[2,0] = A[2,0]/L[0,0]
    for r in range(1,n): # 处理余下的列
        L[r,r] = np.sqrt(A[r,r]-np.dot(L[r,:r],L[r,:r].T)) # 处理主对角线上的元素
        for j in range(r+1,n):
            L[j,r] = (A[j,r] - np.dot(L[j,:r],L[r,:r].T))/L[r,r]

    # 求Ly = b
    y = np.zeros([n, 1])
    y[0, 0] = b[0, 0]/L[0,0]
    for i in range(1, n):
        y[i, 0] = (b[i, 0] - np.dot(L[i, :i], y[:i, 0]))/L[i, i]

    # 求(L^T)x = y
    L_T = L.T
    x = np.zeros([n, 1])
    x[n - 1] = y[n - 1] / L_T[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        x[k, 0] = (y[k, 0] - np.dot(L_T[k, k + 1:], x[k + 1:, 0])) / L_T[k, k]
    print(x)

A = np.array([[4,-1,1],[-1,17/4,11/4],[1,11/4,7/2]])
b = np.array([[0],[1],[0]])
Choleskey(A,b)