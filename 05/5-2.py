# def show_game_board():
#     for i in range(3):
#         for j in range(3):
#             print(game[i][j],end = " ")
#         print()

# game = [["-","-","-"],
#         ["-","-","-"],
#         ["-","-","-"]]


# for i in range(3):
#     for j in range(3):
#         print(game[i][j], end = "  ")
#     print()

# satr = int(input("shomare sath: "))
# sotun = int(input("shomare sotun: "))
# game[satr][sotun] = "X"

# for i in range(3):
#     for j in range(3):
#         print(game[i][j], end = "  ")
#     print()

# satr = int(input("shomare sath: "))
# sotun = int(input("shomare sotun: "))
# game[satr][sotun] = "O"

# for i in range(3):
#     for j in range(3):
#         print(game[i][j], end = "  ")
#     print()


#2
def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end = "  ")
        print()

game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

show_game_board()

while True:
    print("player1")
    while True:
        satr = int(input("shomare sath: "))
        sotun = int(input("shomare sotun: "))
        if  0<= satr <= 2 and 0<= sotun <= 2:
            if game[satr][sotun]=="-":
                game[satr][sotun] = "X"
                break
            else:  
                print("khooneh khali")
        else:
            print("try again")
    show_game_board()


    print("player2")
    while True:
        satr = int(input("shomare sath: "))
        sotun = int(input("shomare sotun: "))
        if  0<= satr <= 2 and 0<= sotun <= 2:
            if game[satr][sotun]=="-":
                game[satr][sotun] = "O"
                break
            else:  
                print("khooneh khali")
        else:
            print("try again")

    show_game_board()
    def etmam_bazi():
        if game[0][0]==game[1][1]==game[2][2] == "X":
            print("player1 bord")
    etmam_bazi()
    
