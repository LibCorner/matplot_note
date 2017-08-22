#coding:utf-8
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib import transforms

#文本
plt.text(x=0.5,y=0.5,s="matplotlib",ha='center',va='center',fontsize=16)

#带文本框的box的文本
'''
#使用bbox.bbox参数，使用设置`Rectange`对象的属性
'''
bbox_props=dict(boxstyle='square,pad=0.3',facecolor='red',ec='b',lw=0)
t=plt.text(0,0,"Direction",ha='center',va='center',rotation=0,size=15,bbox=bbox_props)
plt.show()

##################多个文本####################################
fig,ax=plt.subplots()
sent="hello i am a computer"

length=len(sent)
sent=sent.split()
score=[0.1,0.2,0.6,0.4,0.7]

ax.set_xticks(np.arange(0,length,1))
x=2
y=0.1
for w,s in zip(sent,score):
    bbox_props=dict(boxstyle='square,pad=0.3',facecolor=cm.Reds(s)[:3],ec='b',lw=0)
    t=ax.text(x,y,w,ha='center',va='center',rotation=0,size=15,bbox=bbox_props)
    x0,y0,width,height=t.get_clip_box().bounds
    x+=3
    print(x)
    
fig.show()


#####################每个单词使用不同的背景色#######################
plt.figure()
t = plt.gca().transData
fig = plt.gcf()
sent="hello it am a. at the end of the day of the"

length=len(sent)
sent=sent.split()
score=[0.1,0.2,0.6,0.4,0.7,0.5,0.8,0.3,0.4]

x=0
y=0.1
for w,s in zip(sent,score):
    bbox_props=dict(boxstyle='square,pad=0.3',facecolor=cm.Reds(s/2)[:3],ec='b',lw=0)
    text=plt.text(x,y," "+w+" ",ha='left',va='center',rotation=0,size=15,bbox=bbox_props,transform=t)
    text.draw(fig.canvas.get_renderer())
    ex = text.get_window_extent()
    t = transforms.offset_copy(text._transform,x=0.1+ex.width, units='dots')
#t = plt.gca().transData
#fig = plt.gcf()
fig.show()