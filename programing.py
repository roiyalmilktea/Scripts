from selenium import webdriver

driver = webdriver.Chrome()

paiza = 'https://paiza.jp/challenges/'

atcoder = 'https://atcoder.jp/'


def login():
    driver.get(paiza)


if __name__ == '__main__':
    login()
