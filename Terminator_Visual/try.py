from . import screen
from . import colordraw as cd
#import label
#label.init(screen.world)
screen.init(16,10,cd.v("."))
#screen.world[1][1][0] = "*"
#screen.world[1][1] = str(screen.height)
a = 0
#screen.label("hi",4,4,3)
def update():
          global a
          #screen.world[a%screen.height][1][0] = cd.rnb(chr(65+(a%26)),a%7)
          #print("hi",flush=True)
          a+=1
          #screen.label("hello",4,5,3)
          #screen.blink("m","n",2,2,frame,3)
          #screen.blink("f","g",4,4,frame,4)
          #screen.blink("/","\\",4,4,3,1)
          screen.anim(["/",'-','\\'],3,4,0,[2,3,4])
          screen.anim(["4","5"],3,4,0,[2,6])
          #screen.label(str(screen.frame),3,4)
          #screen.box(0,0,8,8,3)
          screen.box(1,1,9,9,2)
          screen.label(str(screen.g_vars.frame),5,6,4)
          screen.g_vars.tail = 'Hello'
          if a>10:
                  screen.g_vars.head = str(a)
screen.display(update = update)
