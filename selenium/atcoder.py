# githubにあげる時はパスワードを消すこと！
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://atcoder.jp/login")
# 入力枠のユーザ名のところをさがす
e1 = driver.find_element_by_name('username')
# 入力枠のパスワードのところをさがす
e2 = driver.find_element_by_name('password')
# ユーザ名を入力する
e1.send_keys('loyal')
# パスワードを入力する
e2.send_keys('algreversing6')  # 公開するときは絶対消すこと
e1.submit()
e2.submit()
