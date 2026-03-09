import colordraw as cd
from time import sleep
t=0.02
lst= ['\\','/']
i = 0
k=0
while True:
          for m in range(0,i):
                    print(" ",end='')
          for j in range(0,i if i< 7 else 7):    
                    print(cd.rnb(lst[(j+k)%2],j%7), end='')
                    sleep(t)
          print("=O", end='')
          print("\r" , end='')          
          i += 1
          k = i%2

          
