#مثلث
x = int(input())
y = int(input())
z = int(input())


if z < x + y and x < z + y and y < z + x :
    print ("its ok")

else :
    print ("not ok")