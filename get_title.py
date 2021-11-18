from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://uta.pw/sakusibbs/post.php?mml_id=35"
driver.get(url)

link = driver.find_element_by_link_text('名作アーカイブ')

link.click()

time.sleep(30)
driver.close()

