from selenium import webdriver
import os
import time

login_url = 'http://uta.pw/sakusibbs/users.php?action=login'
user_id, password = ('JS-TESTER', 'ipCU12ySxI')
# 保存先フォルダ
save_dir = os.path.dirname(os.path.abspath(__file__))
save_file = save_dir+'/list.csv'
# Chromeのオプションで保存フォルダを指定
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': save_file})

# メイン処理


def login_download():
    driver = webdriver.Chrome(options=options)
    try_login(driver)
    link_click(driver, 'mypage')
    for i in range(30):
        if os.path.exists(save_file):
            break
        time.sleep(1)


def try_login(driver):
    driver = driver.get(login_url)
    usr = driver.find_element_by_name('username_mmlbbs6')
    usr.send_keys(user_id)
    pwd = driver.find_element_by_name('password_mmlbbs6')
    pwd.send_keys(password)
    pwd.submit()


def link_click(driver, label):
    a = driver.find_element_by_partial_link_text(label)
    a.click()


if __name__ == '__main__':
    login_download()
