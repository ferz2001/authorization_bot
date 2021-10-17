import os
import requests
import time
import ast
import logging

import telegram as tg
from selenium import webdriver
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


load_dotenv()

CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')
DATA = ast.literal_eval(os.getenv('DATA'))
URL_LOG = os.getenv('URL_LOG')
URL_MAIN = os.getenv('URL_MAIN')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s, %(name)s, %(levelname)s, %(message)s'
)
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
handler = RotatingFileHandler('mylog.log', maxBytes=50000000, backupCount=1)
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

bot = tg.Bot(token=BOT_TOKEN)
logger.debug('Bot is ready')

def send_message(message): 
    return bot.send_message(chat_id=CHAT_ID, text=message) 

def main(login, password):
    try:
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
    except Exception as e:
        send_message(f'Бот упал с ошибкой: {e}')
        logger.error(e, exc_info=True)
    

if __name__ == '__main__':
    while True:
        try:
            for login, password in DATA.items():
                main(login, password)
                send_message(f'Произошёл вход с аккаунта {login}')
            for i in range (1,144):
                requests.get('https://www.google.com/')
                time.sleep(20 * 60)
        except Exception as e:
            send_message(f'Бот упал с ошибкой: {e}')
            logger.error(e, exc_info=True)
            time.sleep(60)
