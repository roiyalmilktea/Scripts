import math

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]


def dist(s, t):
    return math.sqrt((t[0] - s[0]) ** 2 + (t[1] - s[1]) ** 2)


ans = 0
for i in range(N):
    for j in range(i, N):
        ans = max(ans, dist(P[i], P[j]))
print(ans)
