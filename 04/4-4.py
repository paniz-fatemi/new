#4
sefr = 0
b = 1
def shomaresh(teedad):
    a = sefr
    c = 0
    for i in range(len(teedad)):
        if(teedad[i]==" "):
            a = sefr
        elif a == sefr:
            a = b
            c += 1
    return c
teedad = input()
print("teedad kalamat: " + str(shomaresh(teedad)))