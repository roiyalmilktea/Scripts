N = int(input())
cnt = 0
pt, px, py = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x-px)+abs(y-py) <= t-pt and t % 2 == (x+y) % 2:
        cnt += 1
    pt, px, py = t, x, y
print("Yes" if cnt == N else "No")
