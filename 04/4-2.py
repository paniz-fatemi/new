#2
def fucktoreal(nom):
    num=1
    t = 0
    for i in range(nom):
        num = num * (i+1)
        if num == nom:
            print("yes")
            t=1
            break
    if t==0:
        print("no")
nom=int(input())
fucktoreal(nom)
