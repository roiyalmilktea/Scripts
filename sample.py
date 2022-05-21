import re

n = int(input())

if n % 3 == 0:
    ans = 'true'
else:
    ans = 'false'
l = [int(n) for n in list(str(n))]

if 3 in l:
    ans = 'true'
else:
    ans = 'false'


print(ans)
