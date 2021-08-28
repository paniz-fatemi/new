#4
import random
counter_bazikon = 0
counter_ma = 0

while True :
    items = ["sang","kaqaz","qeichi"]
    computer_choice = random.choice(items)

    print("0 : sang")
    print("1 : kaqaz")
    print("2 : qeichi")
    user_choice_i = int(input())
    user_choice = items[user_choice_i]

    if computer_choice == "sang" and user_choice == "qeichi" or computer_choice == "qeichi" and user_choice == "kaqaz" or computer_choice == "kaqaz" and user_choice == "sang" :
        print("shoma bakhti!!!!!")
        counter_ma += 1
    elif computer_choice == "sang" and user_choice == "kaqaz" or computer_choice == "kaqaz" and user_choice == "qeichi" or computer_choice == "qeichi" and user_choice == "sang":
        print("shoma bordi!!!!!")
        counter_bazikon += 1
    else :
        print("mosavi shod")

    print("computer choice was :" , computer_choice)
    print("Do you want to play again?  yes :1  and  no :2")
    u = int(input())
    if u == 2 :
        print("emtiaz bazikon: ",counter_bazikon,"   ","emtiaz computer: ",counter_ma)
        if counter_ma > counter_bazikon:
            print("computer barande nahaii")
        elif counter_bazikon > counter_ma:
            print("shoma barande nahaii")
        else:
            print("mosavi shodid")
        break