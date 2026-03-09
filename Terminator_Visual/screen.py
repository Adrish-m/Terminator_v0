from time import sleep
from . import colordraw as cd
from .ui import *
#import g_vars
from .. import g_vars

print("\x1b[?25l" , end='')
tile = "."
buffer = ''

def init(w,h,t=tile,delay=0.1):
          g_vars.width = w
          g_vars.height = h
          g_vars.tile = t
          g_vars.world=[[[g_vars.tile,0] for y_loop in range(g_vars.width)] for x_loop in range(g_vars.height)]
          g_vars.delay = delay

def empty_fn():
          pass
def return_fn(x):
        return x

def display(main = empty_fn,update = empty_fn):
          global buffer
          try:
                    main()
                
                    while True:
                              update()
                              buffer+=g_vars.head+'\n'
                              for i in g_vars.world:
                                        for j in i:
                                                #print(i)
                                                #print(j[0])
                                                #dig = int(j[1])
                                                #print(buffer)
                                                buffer += cd.rnb(j[0],j[1])
                                                #buffer += j[1]
                                        buffer += '\n'
                              buffer+=g_vars.tail+'\n'
                              print(buffer, flush = True)
                              sleep(g_vars.delay)
                              buffer = ''
                              print('\x1b[1J\x1b[H',end='')
                              g_vars.frame += 1
          finally:
                    print("\x1b[?25h" , end='')
                    
# def label(text,x,y,color=0):
#         global world
#         a = 0
#         # def col():
#         #         pass
#         # if color != "":
#         #         exec(f"col = cd.{color}")
#         for i in text:
#                 world[y][x+a] = [i,color]
#                 a+=1