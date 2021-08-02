#معدل
name = input("enter your name: ")
score1 = int(input("enter your score1: "))
score2 = int(input("enter your score2: "))
score3 = int(input("enter your score3: "))
average = (score1 + score2 + score3)/3
if average >= 17 :
    print("great")
if 17>average >= 12:
    print ("normal")
if average <12:
    print("fail")