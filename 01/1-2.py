#ماشین حساب
import math
op = input()
if op =="sqrt" or op =="sin":
    a = float(input())
else:
    a = float(input())
    b = float(input())

if op =="-":
    r = a - b
elif op == "+":
    r = a + b
elif op == "*":
    r = a * b
elif op =="/":
    if b == 0:
        r = "no no no no"
    else:
        r = a/b
elif op == "^":
    r = a**b
elif op == "log":
    r = math.math.log(a)
elif op =="sqrt":
    r = math.math.sqrt(a)
elif op == "sin":
    r = math.sin(a)

print(r)