s=40
import math
for i in range(1,int(math.sqrt(s)+1)):
               if s%i==0:
                 print(i)
for j in range(i,0,-1):
    if s%j==0:
       print(s//j)
