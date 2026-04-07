P = int(input())
D = int(input())
B = int(input())

total = P*1 + D*2 + B*3

if total >= 150:
    print("B")
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")
