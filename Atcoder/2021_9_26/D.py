N = int(input())
A = list(map(int, input().split()))

mod = 998244353

ans = [0]*10
ans[A[0]] = 1

for i in range(1, N):
    nxt = [0]*10
    for j in range(10):
        nxt[(j+A[i]) % 10] += ans[j] % mod
        nxt[(j*A[i]) % 10] += ans[j] % mod
    ans = nxt

for i in range(10):
    print(ans[i] % mod)
