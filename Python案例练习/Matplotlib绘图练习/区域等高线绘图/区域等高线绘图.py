import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

data = pd.read_excel("区域高程数据.xlsx",header=None)
fig = plt.figure()
axe = fig.add_subplot(111)

z = np.array(data.head(874),dtype=int)/1000
m,n = z.shape
x = 50*np.arange(0,n)/1000
y = 50*np.arange(0,m)/1000
x,y = np.meshgrid(x,y)
contour = axe.contour(x,y,z)
axe.clabel(contour,colors='black',fontsize=8)
axe.set_xlabel('$x$/KM')
axe.set_ylabel('$y$/KM',rotation=0)
axe.set_title('Contour Line of This Area(Unit of Measurement is KM)')
fig.tight_layout()
plt.show()