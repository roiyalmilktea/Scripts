S = list(input())
T = list(input())
ans = "No"

if S == T:
    ans = "Yes"
for i in range(len(S)-1):  # 入れ替え比較をするから長さより-1まで繰り返す
    S[i], S[i+1] = S[i+1], S[i]  # 位置を入れ替える
    if S == T:
        ans = "Yes"
    S[i], S[i+1] = S[i+1], S[i]  # 違っていたから位置を戻した


print(ans)
