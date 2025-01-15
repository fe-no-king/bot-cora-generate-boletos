from utils.file_load import load_dict_list
from utils.validations import validate_client, validate_cnpj, validate_value, validate_day_month, validate_frequency, convert_dot_to_comma
from utils.generate_dates import generate_due_dates

from utils.selenium import init_driver, search_and_click, click_element, set_bankslip_amount, set_select_due_date
from utils.folder import create, move_files

from utils.message import welcome_ascii

import time

print(welcome_ascii())

# Carrega a lista de dados
data_list = load_dict_list('list-data.xlsx')

default_data_start = "02-2025"
default_data_end = "03-2025"

# Solicita as datas de início e fim
data_start = input(f'Digite a data inicio m-Y [{default_data_start}]: ') or default_data_start
data_end = input(f'Digite a data final m-Y [{default_data_end}]: ') or default_data_end

driver = init_driver()

# Verifica se há dados na lista
if len(data_list) > 0:
    for val in data_list:

        # Validações e obtenção dos dados
        cnpj = validate_cnpj(val.get('CNPJ'))
        client = validate_client(val.get('CLIENTE', 'SEM NOME'))
        value = validate_value(val.get('VALOR'))
        day_month = validate_day_month(val.get('DIA DO MÊS'))
        frequency = validate_frequency(val.get('FREQUÊNCIA'))

        value = convert_dot_to_comma(value)

        # Verifica se todos os dados necessários estão presentes
        if client and cnpj and value and day_month and frequency:
           
            due_dates = generate_due_dates(data_start, data_end, day_month, frequency)

            if(len(due_dates) > 0):

                for date in due_dates:

                    driver.get("https://app.cora.com.br/dashboard")
                    time.sleep(2)

                    path = f'clients/{cnpj}'

                    click_element(driver, '/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/button')
                    click_element(driver, '/html/body/div[1]/div/main/div/ul/div[2]')

                    click_element(driver, '/html/body/div[1]/div/main/div/div/div')
                    click_element(driver, '/html/body/div[1]/div/main/footer/div/button[2]')

                    search_and_click(driver, cnpj)

                    create(path)

                    # set valor
                    set_bankslip_amount(driver, value)

                    # set date
                    set_select_due_date(driver, date)

                    time.sleep(2)

                    click_element(driver, '/html/body/div[1]/div/main/footer/div/button[2]')

                    time.sleep(2)

                    click_element(driver, '/html/body/div[1]/div/main/footer/div/button[2]')

                    click_element(driver, '/html/body/div[1]/div/main/div[1]/div/div[5]/button')

                    move_files('tmp', path)     

