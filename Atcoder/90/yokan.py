L, N = map(int, input().split())

K = int(input())

A = [0]+list(map(int, input().split()))+[l]


def check(n):
    st = 0
    cnt = 0
    for i in A:
        if i-st >= n:
            st = i
            cnt += 1
    return cnt >= K+1


left = 0
right = L

while left-right >= 1:
    mid = (right+left)//2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
