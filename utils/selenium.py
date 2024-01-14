from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def init_driver():
    driver = webdriver.Firefox()
    driver.get("https://app.cora.com.br/emitir-cobranca/modelo-de-boleto/contatos")
    time.sleep(15)
    return driver

def load_data(file_path):
    return pd.read_excel(file_path).head()

def search_and_click(driver, search_text):
    search_contacts = driver.find_element(By.ID, 'searchContacts')
    search_contacts.send_keys(search_text)
    time.sleep(5)
    elementos_li = driver.find_elements(By.CSS_SELECTOR, 'ul.list > li')
    if len(elementos_li) > 2:
        elementos_li[1].click()
    return len(elementos_li)