#coding:utf-8
import matplotlib.pyplot as plt
from matplotlib import transforms

def rainbow_text(x,y,ls,lc,**kw):
    """
    Take a list of strings ``ls`` and colors ``lc`` and place them next to each
    other, with text ls[i] being shown in color lc[i].

    This example shows how to do both vertical and horizontal text, and will
    pass all keyword arguments to plt.text, so you can set the font size,
    family, etc.
    """
    t = plt.gca().transData
    fig = plt.gcf()

    #### note: this line moved down ....### 
    #plt.show()                           #
    #######################################
    #horizontal version
    for s,c in zip(ls,lc):
        text = plt.text(x,y," "+s+" ",color=c, transform=t,fontsize=15,bbox=bb **kw)
        text.draw(fig.canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, x=ex.width, units='dots')

    #vertical version
    for s,c in zip(ls,lc):
        text = plt.text(x,y," "+s+" ",color=c, transform=t,
                rotation=90,va='bottom',ha='center',**kw)
        text.draw(fig.canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, y=ex.height, units='dots')

    t = plt.gca().transData
    fig = plt.gcf()
    plt.show() ############### when this is here, you can see that 
               ############### all unicorns poo rainbows ;-)


plt.figure()
rainbow_text(0.0,0.0,"all unicorns poop rainbows ! ! !".split(), 
        ['red', 'orange', 'brown', 'green', 'blue', 'purple', 'black'],
        size=30)

