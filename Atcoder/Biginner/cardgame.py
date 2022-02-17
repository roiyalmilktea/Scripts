import math

n = int(input())
# カードの数字の配列をつくる
cards = list(map(int, input().split()))
# AとBに配列をつくる
A = []
B = []
# テキトーに並べていた数字を順にする
cards.sort()
# 逆にする
cards.reverse()

for i in range(n):
    if i % 2 == 0:
        A.append(cards[i])
    else:
        B.append(cards[i])
print(int(math.fabs(sum(A)-sum(B))))
