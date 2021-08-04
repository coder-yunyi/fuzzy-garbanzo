from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def main(username: str, passwd: str, container: str):
    br = webdriver.Chrome()
    br.get("https://accounts.goorm.io/login?return_url=aHR0cHM6Ly9pZGUuZ29vcm0uaW8vbXkvZGFzaGJvYXJk&keep_login=true")
    WebDriverWait(br, 30, 0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/div[4]/button'))
    )
    br.find_element_by_xpath('//*[@id="emailInput"]').send_keys(username)
    br.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(passwd)
    br.find_element_by_xpath('//*[@id="app"]/section/div[4]/button').click()
    sleep(10)
    br.get(container)


if __name__ == '__main__':
    print("!!!本脚本不支持第三方账号登录goorm!!!")
    main(input("请输入您的goorm用户名:"), input("请输入您的goorm密码:"), input("输入容器url:"))
    print("keepalive流程正在进行...")
    print("开启keepalive后会长期占用50-100MB内存，请不要kill keepalive脚本")
