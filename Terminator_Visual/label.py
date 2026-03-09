from . import colordraw as cd
world = []
def init(ls):
        global world
        world = ls

def label(text,x,y,color=0):
        global world
        a = 0
        # def col():
        #         pass
        # if color != "":
        #         exec(f"col = cd.{color}")
        for i in text:
                world[y][x+a] = [i,color]
                a+=1