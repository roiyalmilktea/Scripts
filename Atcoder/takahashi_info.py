# 初期配列をつくる
a = []
cnt = 0
for i in range(0, 3):
    # 作業用配列をつくった
    row = list(map(int, input().split()))
    # aにrowの要素を追加する
    a.append(row)

for j in range(0, 2):
    x = a[0][j] - a[0][j+1]
    y = a[1][j] - a[1][j+1]
    z = a[2][j] - a[2][j+1]

    if x == y == z:
        cnt += 1

for j in range(0, 2):
    x = a[j][0] - a[j+1][0]
    y = a[j][1] - a[j+1][1]
    z = a[j][2] - a[j+1][2]

    if x == y == z:
        cnt += 1

if cnt == 4:
    print("Yes")
else:
    print("No")


#----------------------------------------------------------#
a = []
cnt = 0

for i in range(0, 3):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(0, 2):
    x = a[0][i] - a[0][i+1]
    y = a[1][i] - a[1][i+1]
    z = a[2][i] - a[2][i+1]

    if x == y == z:
        cnt += 1

for i in range(0, 2):
    x = a[i][0] - a[i+1][0]
    y = a[i][1] - a[i+1][1]
    z = a[i][2] - a[i+1][2]

    if x == y == z:
        cnt += 1

if cnt == 4:
    print("Yes")
else:
    print("No")
