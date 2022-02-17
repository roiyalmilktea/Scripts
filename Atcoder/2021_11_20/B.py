# B.py
n, x = map(int, input().split())
# 4,2
a = [0] + list(map(int, input().split()))
# [0,3,1,1,4]
b = [0] * (n + 1)
while not b[x]:  # b[x]になるまで繰り返し
    b[x] = 1
    x = a[x]
print(b.count(1))
