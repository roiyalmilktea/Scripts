n, a, b = list(map(int, input().split()))
cnt = 0
d = []

for i in range(n):
    # 1以上n以下の整数を文字列に変換
    s = str(i+1)
    # 1文字ずつ数値化し配列にする
    array = list(map(int, s))

    # list内の総和
    cnt = sum(array)
    # 各桁の総和がa以上b以下の時dに追加

    if cnt >= a and cnt <= b:
        d.append(i+1)

print(sum(d))
