#!/bin/sh
# 基本情報技術者試験過去問

from operator import imod
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.fe-siken.com/fekakomon.php"


def login():
    driver.get(url)


if __name__ == '__main__':
    login()
