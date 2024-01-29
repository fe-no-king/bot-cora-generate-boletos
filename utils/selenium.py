from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def init_driver():

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "/home/programador/Documents/Projects/bot-cora/tmp",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get("https://app.cora.com.br/dashboard")
    time.sleep(10)
    return driver

def search_and_click(driver, search_text):

    search_contacts = driver.find_element(By.ID, 'searchContacts')
    search_contacts.send_keys(search_text)
    time.sleep(2)
    elementos_ul = driver.find_elements(By.CSS_SELECTOR, 'ul.list')

    if len(elementos_ul) > 1:
        first_li = elementos_ul[1].find_element(By.CSS_SELECTOR, 'li')
        first_li.click()
    
    time.sleep(2)


def click_element(driver, path):
    
    button = driver.find_element(By.XPATH, path)
    button.click()
    time.sleep(2)

def set_bankslip_amount(driver, amount):

    amount_field = driver.find_element(By.ID, 'emissionAmount')
    amount_field.clear()
    amount_field.send_keys(amount)

    js_script = f"document.getElementById('emissionAmount').value = '{amount}';"
    driver.execute_script(js_script)

    time.sleep(2)

def set_select_due_date(driver, date):

    click_element(driver, '/html/body/div[1]/div/main/div/div/div[2]/div/div[1]/div/div/div/input')

    js_script = """

    function converteData(date) {
        const meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ];

        const partes = date.split("/");
        const mes = partes[1];
        const ano = partes[2];

        const nomeMes = meses[parseInt(mes) - 1];

        return nomeMes+" "+ano;
    }

    function next_verify_date(count, date_text, date) {
    
        count++;

        let current_text = document.getElementsByClassName('react-datepicker__current-month')[0].textContent;

        if(current_text == undefined || count == 20){
            return 0;
        }

        if(current_text == date_text){

            let day = date.split("/")[0];
            document.getElementsByClassName("react-datepicker__day--0"+day)[0].click();
            return 0;
        }
        
        document.getElementsByClassName('react-datepicker__navigation--next')[0].click();

        setTimeout(() => {
            next_verify_date(count, date_text, date);
        }, 500);
    }

    next_verify_date(0, converteData('"""+date+"""'), '"""+date+"""');

    """
    
    driver.execute_script(js_script)
    time.sleep(6)