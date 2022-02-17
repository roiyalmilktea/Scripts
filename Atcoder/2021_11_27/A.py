
s = input()
t = input()

if s[0] == '.' and t[1] == '.':
    print('No')
elif s[1] == '.' and t[0] == '.':
    print('No')
else:
    print('Yes')
