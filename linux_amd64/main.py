from selenium.webdriver import PhantomJS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint
from time import sleep


def in_url(device: any, url: str):
    if url in device.current_url():
        return True
    else:
        return False


def main():
    urls = [
        'https://down.fruitpan.com/fs/0c7o6dce5reaef342154fsgdfh3/',
        'https://down.fruitpan.com/fs/8cbo0d1ebr2aaf942154fsgdfh9/',
        'https://down.fruitpan.com/fs/ccodaeraaf42b154cfsgcdfhabb/',
        'https://down.fruitpan.com/fs/ecod7era8f42f1544fsg7dfh8bb/'
    ]
    br.get(urls[randint(0, 3)])
    br.implicitly_wait(40)
    br.find_element_by_xpath(
        '/html/body/div[7]/div[2]/div[1]/div[1]/div[2]/div/div[1]/button'
    ).click()
    sleep(30)
    WebDriverWait(br, 20, 0.2).until(in_url(br, 'https://down.fruitpan.com/file/'))
    sleep(2)
    br.find_element_by_xpath(
        '/html/body/div[7]/div[2]/div[1]/div[2]/div[1]/button[1]'
    ).click()
    sleep(5)
    return()


if __name__ == '__main__':
    br = PhantomJS()
    main()
