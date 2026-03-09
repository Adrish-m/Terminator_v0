#Colour Draw
def v(x):
          return "\033[35m"+x+"\033[39m"
def i(x):
          return "\033[36m"+x+"\033[39m"
def b(x):
          return "\033[34m"+x+"\033[39m"
def g(x):
          return "\033[32m"+x+"\033[39m"
def y(x):
          return "\033[33m"+x+"\033[39m"
def o(x):
          return "\033[91m"+x+"\033[39m"
def r(x):
          return "\033[31m"+x+"\033[39m"
def reg(x):
        return "\033[39m"+x
def reset():
          print("\033[0m", end='')
def n(x , n):
          return "\033["+str(n)+"m"+x+"\033[39m"

def rnb(x , n):
          dictr = [reg, v , i ,b ,g ,y, o ,r]
          return dictr[n](x)
          
          
