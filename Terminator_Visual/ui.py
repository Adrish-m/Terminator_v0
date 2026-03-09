#import g_vars
from .. import g_vars
def label(text,x:int,y:int,color=0):
        a = 0
        # def col():
        #         pass
        # if color != "":
        #         exec(f"col = cd.{color}")
        for i in text:
                g_vars.world[y][x+a] = [i,color]
                a+=1
def box(x1,y1,x2,y2,color=0):
        # top = "┌" + "─" * inner_width + "┐"
        # bottom = "└" + "─" * inner_width + "┘"

        #corners
        g_vars.world[y1][x1]=["┌",color]
        g_vars.world[y2][x2]=["┘",color]        
        g_vars.world[y1][x2]=["┐",color]
        g_vars.world[y2][x1]=["└",color]

        #sides
        for i in range(x1+1,x2):
                g_vars.world[y1][i]=["─",color]
                g_vars.world[y2][i]=["─",color]
        for i in range(y1+1,y2):
                g_vars.world[i][x1]=["│",color]
                g_vars.world[i][x2]=["│",color]

def blink(text1,text2,x:int,y:int,color1=0,color2=0,interval=3):
        #bg = world[y][x]
        if g_vars.frame%interval != 0:
                label(text1,x,y,color1)
        else:
                label(text2,x,y,color2)

def anim(chars:list,x:int,y:int,color=0,colorlist=[]):
                ielem = g_vars.frame%len(chars)
                label(str(len(chars)),4,5)
                if colorlist == []:
                        label(chars[ielem],x,y,color)
                else:
                        label(chars[ielem],x,y,colorlist[ielem%len(colorlist)])

def tail(text:list):
        return text