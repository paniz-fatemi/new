#3
# x = input("enter x: " )
# y = input("enter y: " )
# try:
#     x = int(x)
#     y = int(y)
#     for i in range(1, x + 1):
#         print(i, end=' ')
#     print()
#     for i in range( 1, x + 1):
#         print( i * y, end = ' ' )
#     print()
# except ValueError as err:
#     print(err)




x,y = eval(input("enter X,Y: "))
for i in range(1,x+1):
    for j in range(1,y+1):
        print(format(i*j,'3d'),end='')
    print()
    
    
#:(((
