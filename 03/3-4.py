#4
n = int(input())
for i in range(n):
    if i // 2 == i / 2:
        print('*',end='')
    if i // 2 != i/ 2:
        print('#',end='')