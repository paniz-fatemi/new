#6
import math
r = []
counter = 0
a , b , c = 0 , 1 , None
j = int(input())
for i in range (j):
   c = a + b 
   r.append(c)
   a = b
   b = c
   counter += 1
r.insert(0,1)

print (r)