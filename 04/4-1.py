#1
n = int(input())
for i in range(n):
    if i // 2 == i / 2:
        print('*',end='')
    if i // 2 != i/ 2:
        print('#',end='')


n = int(input())
m = int(input())
def shatranji():
    for i in range(n,m):
        if i // 2 == i / 2:
            print('*',end='')
        if i // 2 != i/ 2:
            print('#',end='')

shatranji()

    