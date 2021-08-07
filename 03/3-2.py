#2
import random
n = int(input())
a = []
while len(a)< n:
    x = random.randint(0,99999)
    if x not in a:
        a.append(x)
print(a)
