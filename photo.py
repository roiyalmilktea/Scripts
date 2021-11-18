from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://uta.pw/sakusibbs/post.php?mml_id=35'
driver.get(url)
# class属性がposttitleの要素を取得
e = driver.find_element_by_class_name('posttitle')
# テキストを表示
print(e.text)

driver.close()
