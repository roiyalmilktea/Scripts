s = input().replace('eraser', '').replace(
    'erase', '').replace('dreamer', '').replace('dream', '')

if s == '':
    print("YES")
else:
    print("NO")

# replace関数で指定のワードを全て空白にした。そして、空白にされた（一致した）場合""YES"そうでなければ"NO"
