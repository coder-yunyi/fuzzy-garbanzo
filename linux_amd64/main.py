from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from random import randint
from time import sleep


def main():
    urls = [
        'https://down.fruitpan.com/fs/0c7o6dce5reaef342154fsgdfh3/',
        'https://down.fruitpan.com/fs/8cbo0d1ebr2aaf942154fsgdfh9/',
        'https://down.fruitpan.com/fs/ccodaeraaf42b154cfsgcdfhabb/',
        'https://down.fruitpan.com/fs/ecod7era8f42f1544fsg7dfh8bb/'
    ]
    br.get(urls[randint(0, 3)])
    br.implicitly_wait(30)    
    br.find_element_by_xpath(
        '//*[@id="speed-type-1"]/div/div[1]/button'
    ).click()
    sleep(35)
    br.find_element_by_xpath(
        '//*[@id="downbtn"]'
    ).click()
    sleep(8)
    return()


if __name__ == '__main__':
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    br = Chrome(chrome_options=options)
    main()
