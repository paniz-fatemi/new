#4
import math
b = []
a = int(input("teedad danesh juyan ra vared konid :"))
for i in range(a):
    b.append(float(input()))
print (b)
print(max(b))
print(min(b))

average = sum(b)
print("average :" ,average/a)
