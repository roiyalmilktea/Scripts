A, B, C = list(map(int, input().split()))
v = B//C

if A <= (v*C) <= B:
    print(v*C)
else:
    print("-1")
