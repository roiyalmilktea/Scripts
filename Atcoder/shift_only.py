n = int(input())
a = list(map(int, input().split()))
cnt = 0
while all(i % 2 == 0 for i in a):  # a=8 12 40としてaが全て偶数である限り繰り返される
    a = [i/2 for i in a]# aの配列を全て2で割る。
    cnt += 1 
print(cnt)
