#2
import math
def moadele2():
    print("aX^2+bX+c=0")
    a= int (input("a= "))
    b= int (input("b= "))
    c= int (input("c= "))
    d=((b**2)-(4*a*c))
    if d<0:
        print("there is no answer")
    if d==0:
        print((-b)/(2*a))
    if d>0:
        x1= (-b-math.sqrt(d))/(2*a)
        x2= (-b+math.sqrt(d))/(2*a)
        print(x1,x2)
moadele2()
