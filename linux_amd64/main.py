from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint
from time import sleep


def main():
    urls = [
        'http://47.56.193.8/f/33248059-507113316-bca3d5',
        'http://47.56.193.8/f/33248059-507113317-d44329',
        'http://47.56.193.8/f/33248059-507113315-da9588',
        'http://47.56.193.8/f/33248059-507113314-a1c90e',
        'http://47.56.193.8/f/33248059-507113313-de9247',
        'http://47.56.193.8/f/33248059-507113312-d1e285',
        'http://47.56.193.8/f/33248059-507113311-71fa8e',
        'http://47.56.193.8/f/33248059-507113310-1967f3',
        'http://47.56.193.8/f/33248059-507113309-c2cbc8'
    ]
    br.get(urls[randint(0, len(urls) - 1)])
    try:
        WebDriverWait(br, 20, 0.2).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="passcode"]')),message=""
        )
        br.find_element_by_xpath('//*[@id="passcode"]').send_keys('8542')
        br.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div/div/div/div[2]/div[2]/button').click()
    except NoSuchElementException:
        pass
    WebDriverWait(br, 20, 0.2).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button'))
    )
    br.find_element_by_xpath('//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button').click()
    sleep(5)
    br.quit()
    return()


if __name__ == '__main__':
    br = Chrome()
    main()
    exit(0)
