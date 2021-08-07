from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def main(username: str, passwd: str):
    print(u"keepalive流程正在进行...")
    print(u"开启keepalive后会长期占用50-100MB内存，请不要kill keepalive脚本")
    br = webdriver.PhantomJS()
    br.get(
        "https://accounts.goorm.io/login?return_url=aHR0cHM6Ly9pZGUuZ29vcm0uaW8vbXkvZGFzaGJvYXJk&keep_login=true"
    )
    WebDriverWait(br, 30, 0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/div[4]/button'))
    )
    br.find_element_by_xpath('//*[@id="emailInput"]').send_keys(username)
    br.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(passwd)
    br.find_element_by_xpath('//*[@id="app"]/section/div[4]/button').click()
    sleep(10)
    br.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div[4]/div/div/div[1]/div[2]/a'
    ).click()
    sleep(3153600000)


if __name__ == '__main__':
    main(input(u"请输入您的goorm用户名:"), input(u"请输入您的goorm密码:"), input(u"输入容器url:"))

