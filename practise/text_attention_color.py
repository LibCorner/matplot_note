#coding:utf-8
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import transforms
import matplotlib

matplotlib.use('qt4agg')  
#指定默认字体  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus'] = False  

def show_text_attention(text,weights,cmap=cm.Reds):
    '''文本中不同单词显示不同背景颜色
    '''
    plt.figure(figsize=(0.1,0.1))
    t=plt.gca().transData
    fig=plt.gcf()
    
    x=0
    y=0.5
    
    words=text.split()
    assert len(words)==len(weights)
    for w,s in zip(words,weights):
        #bbox文本框的属性
        bbox_props=dict(boxstyle="square,pad=0.3",facecolor=cmap(s)[:3],lw=0)
        text=plt.text(x,y," "+w+" ",va='center',ha='left',rotation=0,
                      size=15,bbox=bbox_props,transform=t)
        text.draw(fig.canvas.get_renderer()) #文字画到fig上
        ex=text.get_window_extent() 
        t=transforms.offset_copy(text._transform,x=ex.width,units='dots') #平移
    t=plt.gca().transData
    ax=plt.gca()
    ax.set_axis_off()
    fig=plt.gcf()
    fig.show()
    
if __name__=="__main__":
    sent="The computer is a very good and intersting thing i love it"

    score=[0.1,0.2,0.6,0.4,0.7,0.5,0.8,0.3,0.4,0.2,0.3,0.1]
    #红色
    show_text_attention(sent,score)
    #蓝色
    show_text_attention(sent,score,cm.Blues)
    #绿色
    show_text_attention(sent,score,cm.Greens)
    