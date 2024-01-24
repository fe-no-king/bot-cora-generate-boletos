from utils.selenium import init_driver, search_and_click, click_element, set_bankslip_amount, set_select_due_date
from utils.folder import create, move_files
import time

driver = init_driver()
path = 'clients/11293137000106'

click_element(driver, '/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div[2]/button')
click_element(driver, '/html/body/div[1]/div/main/div/ul/div[2]/div')

click_element(driver, '/html/body/div[1]/div/main/div/div/div')
click_element(driver, '/html/body/div[1]/div/main/div/div[2]/div[8]/button[1]')

search_and_click(driver, '11293137000106')

create(path)

# set valor
set_bankslip_amount(driver, "210,00")

# set date
set_select_due_date(driver, '10/02/2024')

click_element(driver, '/html/body/div[1]/div/main/div/div/div[9]/button[1]')
click_element(driver, '/html/body/div[1]/div/main/footer/div/button[2]')
click_element(driver, '/html/body/div[1]/div/main/div[1]/div/div[5]/button')

move_files('tmp', path)