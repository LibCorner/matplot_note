#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

#Simple plot: 画cos和sin
X=np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S=np.cos(X),np.sin(X)
#使用默认的设置plot
plt.plot(X,C)
plt.plot(X,S)
plt.show()

#举例说明默认设置: instantiating defaults

#创建一个size为8*6 inches, 80 dots per inch的figure
plt.figure(figsize=(8,6),dpi=80)

#在1*1的网格里创建一个新的subplot
plt.subplot(1,1,1)

#使用宽度为1的蓝色blue线画cosine
plt.plot(X,C,color="blue",linewidth=1.0,linestyle="-")
plt.plot(X,S,color="red",linewidth=2.0,linestyle="-")

#设置x的范围limits
plt.xlim(-4.0,4.0)

#设置x的刻度ticks
plt.xticks(np.linspace(-4,4,9,endpoint=True))

#设置y的范围limits
plt.ylim(-1.0,1.0)

#设置y的刻度ticks
plt.yticks(np.linspace(-1,1,5,endpoint=True))

#使用72 dots像素per inch 保存图像
#plt.savefig("exercice_2.png",dpi=72)

#显示
plt.show()