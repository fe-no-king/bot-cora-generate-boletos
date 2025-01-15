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
    # Localiza o campo de pesquisa e insere o texto
    search_contacts = driver.find_element(By.ID, 'searchContacts')
    search_contacts.send_keys(search_text)
    time.sleep(2)  # Aguarda para garantir que os resultados carreguem

    try:
        # Localiza o elemento pelo XPath fornecido
        element_to_click = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/ul/div/li')
        element_to_click.click()  # Realiza o clique no elemento
        time.sleep(2)  # Aguarda após o clique, se necessário
    except Exception as e:
        print(f"Erro ao localizar ou clicar no elemento: {e}")

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
        // Realiza o clique no elemento identificado pelo XPath
        function clickElementByXPath(xpath) {
            const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (element) {
                element.click();
                console.log(`Clique realizado no elemento com XPath: ${xpath}`);
            } else {
                console.error(`Elemento com XPath ${xpath} não encontrado.`);
            }
        }

        clickElementByXPath('/html/body/div[1]/div/main/div/div/div[2]/div/div[1]/div/div/div/input');
    """
    
    driver.execute_script(js_script)
    time.sleep(0.5)

    js_script = """
        // Função para converter a data em texto formatado (ex: "fevereiro 2025")
        function converteData(date) {
            const meses = [
                "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
            ];

            const partes = date.split("/");
            const mes = partes[1];
            const ano = partes[2];

            const nomeMes = meses[parseInt(mes) - 1];

            return nomeMes + " " + ano;
        }

        // Função para verificar a data e selecionar o dia
        function next_verify_date(count, date_text, date) {
            count++;

            let current_text = document.getElementsByClassName('react-datepicker__current-month')[0].textContent;
            current_text = current_text.toLowerCase();

            // Se a data atual não for encontrada ou número de tentativas excedido, para a execução
            if (current_text === undefined || count === 20) {
                return 0;
            }

            // Se o mês/ano da data corresponder ao desejado, seleciona o dia
            if (current_text === date_text) {
                let day = date.split("/")[0];
                document.getElementsByClassName("react-datepicker__day--0" + day)[0].click();
                return 0;
            }

            // Clica no botão para avançar para o próximo mês
            document.getElementsByClassName('react-datepicker__navigation--next')[0].click();

            // Reexecuta a função após um pequeno atraso
            setTimeout(() => {
                next_verify_date(count, date_text, date);
            }, 500);
        }

        next_verify_date(0, converteData('"""+date+"""'), '"""+date+"""');
    """

    driver.execute_script(js_script)
    time.sleep(6)