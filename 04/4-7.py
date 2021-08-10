#7
def kmm(a,b):
    if a > b:
        c = a
        a = b
        b = c
    while b!= 0:
        o = a % b
        a = b
        b = o
    r = a
    return r
while True:
    x = int(input())
    y = int(input())
    p = int((x*y)/kmm(x,y))
    print("kmm : ", p)
