"""
Yesの条件
・s<t であることと s<=x<t
・s>=t だが、s<=x　または　x<t
"""
s, t, x = list(map(int, input().split()))
if s < t:
    if s <= x < t:
        ans = 'Yes'
    else:
        ans = 'No'
if s >= t:  # s=23 t=0 x=23
    if x < t or s <= x:
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)
