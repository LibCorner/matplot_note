#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

#1D plotting
x=np.linspace(0,3,20)
y=np.linspace(0,9,20)
plt.plot(x,y) #line plot
plt.show()
plt.plot(x,y,'o') # dot plot
plt.show()

#2D arrays：二维数组
image=np.random.rand(30,30)
plt.imshow(image,cmap=plt.cm.hot)
plt.colorbar()
plt.show()