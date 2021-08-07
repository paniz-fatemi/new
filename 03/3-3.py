#3
n = []
u = 0
while u != "no":
    n.append(int(input()))
    u = input("no?")
print(n)
if n == n.sort():
    print("morateb")
else:
    print("namoratab")