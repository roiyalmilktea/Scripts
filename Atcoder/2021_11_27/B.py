a, b = map(int, input().split())  # a=229 b=390
while a > 0 and b > 0:
    if (a % 10)+(b % 10) >= 10:
        print("Hard")
        exit()
    a //= 10
    b //= 10
print("Easy")

# a=123 len(a)=3
# b=123 len(b)=3
