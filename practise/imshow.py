#coding:utf-8
import numpy as np
aimport matplotlib.pyplot as plt

fig,ax=plt.subplots()
min_val,max_val,diff=0.,10.,1.

N_points=int((max_val-min_val)//diff)
data=np.random.rand(N_points,N_points)
ax.imshow(data, interpolation='none')

#text 文本的位置
ind_array=np.arange(min_val,max_val,diff)
x,y=np.meshgrid(ind_array,ind_array)

for xv,yv in zip(x.flatten(),y.flatten()):
    c='x' if (xv+yv)%2 else '0'
    ax.text(xv,yv,c,va='center',ha='center')
    
#设置tick marks
ax.set_xticks(np.arange(min_val-diff/2,max_val-diff/2))
ax.set_xticklabels([])
ax.set_xlim(min_val-diff/2,max_val-diff/2)
ax.grid()
plt.show()

s="hello"
plt.imshow(np.ones([1,5]),shape=[1,2])
plt.text(0,0,s,va='center',ha='center')

cmaps=['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','Dark2', 'Set1', 'Set2', 'Set3']
nrows=len(cmaps)
gradient=np.linspace(0,1,256)
gradient=np.vstack((gradient,gradient))

fig,axes=plt.subplots(nrows=nrows)
fig.subplots_adjust(top=0.95,bottom=0.01,left=0.2,right=0.99)
axes[0].set_title("colormaps",fontsize=14)

for ax,name in zip(axes,cmaps):
    ax.imshow(gradient,aspect='auto',cmap=plt.get_cmap(name))
    pos=list(ax.get_position().bounds)
    x=pos[0]-0.01
    y=pos[1]+pos[3]/2
    fig.text(x,y,name,va='center',ha='right',fontsize=10)
    
for ax in axes:
    ax.set_axis_off()
