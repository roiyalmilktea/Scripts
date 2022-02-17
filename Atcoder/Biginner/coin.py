N = int(input())  # total
A = int(input())  # 1enn


m = N % 500
if m <= A:
    print("Yes")
else:
    print("No")
