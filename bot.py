from selenium import webdriver
import time

URL_LOG = "https://lms.kgeu.ru/login/index.php"
URL_MAIN = "https://lms.kgeu.ru/course/view.php?id=588&section=3"
DATA = {
    "fmannanov01@gmail.com": "p57aw63Hy0",
    "lol-lol12@inbox.ru": "P67NZ43pL0",
    "danis2405@icloud.com": "M65Ft70za3",
    "sadwoxy@mail.ru": "t53JF70LK4"
}
def main(login, password):
    driver = webdriver.Chrome()
    driver.get(URL_LOG)
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(login)
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element_by_id("loginbtn").click()
    driver.get(URL_MAIN)
    driver.close()
    driver.quit()
    

if __name__ == '__main__':
    while True:
        for login, password in DATA.items():
            main(login, password)
            print(f'Произошёл вход с аккаунта {login}')
        time.sleep(172800)