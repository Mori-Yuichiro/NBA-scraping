import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

args = sys.argv
print(args[1])
siteName = 'basketball-reference.com'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.{}/'.format(siteName))


def search(name):
    try:
        searchBox = driver.find_element(By.CLASS_NAME, 'ac-input')
        searchBox.send_keys(name)
        searchBox.submit()

        resultPlayerUrl = driver.find_element(By.CLASS_NAME, 'search-item-url')
        # print(type(resultPlayerUrl.text))
        driver.get('https://www.{}{}'.format(siteName, resultPlayerUrl.text))

        while True:
            key = input('「q」と入力しEnterを押すと終了')
            if key == 'q':
                print('ウィンドウを閉じます')
                break
        driver.quit()
    finally:
        print('終了')


if __name__ == '__main__':
    search(args[1])
