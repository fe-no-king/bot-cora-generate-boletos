from utils.file_load import load_dict_list
from utils.validations import validate_client, validate_cnpj, validate_value, validate_day_month, validate_frequency
from utils.generate_dates import generate_due_dates
from utils.message import welcome_ascii

print(welcome_ascii())

# Carrega a lista de dados
data_list = load_dict_list('list-data.xlsx')

# Solicita as datas de início e fim
data_start = input('Digite a data inicio m-Y: ')
data_end = input('Digite a data final m-Y: ')

# Verifica se há dados na lista
if len(data_list) > 0:
    for val in data_list:
        # Validações e obtenção dos dados
        cnpj = validate_cnpj(val.get('CNPJ'))
        client = validate_client(val.get('CLIENTE', 'SEM NOME'))
        value = validate_value(val.get('VALOR'))
        day_month = validate_day_month(val.get('DIA DO MÊS'))
        frequency = 3

        # Verifica se todos os dados necessários estão presentes
        if client and cnpj and value and day_month and frequency:
           
            due_dates = generate_due_dates(data_start, data_end, day_month, frequency)
            print("Datas de vencimento:", due_dates)