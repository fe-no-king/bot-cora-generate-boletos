import pandas
import re

def validate_client(client):
    return str(client) if pandas.notna(client) else None

def validate_cnpj(cnpj):

    cleaned_cnpj = re.sub(r'\D', '', str(cnpj))
    if pandas.notna(cleaned_cnpj) and cleaned_cnpj.isdigit():
        return int(cleaned_cnpj)
    
    print(f'CNPJ inválido: {cnpj}')
    return None

def validate_value(value):
    try:
        return float(value)
    except ValueError:
        print(f'Valor invalido: {value}')
        return None

def validate_day_month(day_month):
    if pandas.notna(day_month) and 1 <= day_month <= 31:
        return int(day_month)

    print(f'Dia do mês invalido deve estar no intervalo entre 01 e 30: {value}')
    return None

def validate_frequency(frequency):
    allowed_frequencies = {1, 2, 3, 4, 6}
    if pandas.notna(frequency) and frequency in allowed_frequencies:
        return int(frequency)
    
    print(f'Frequência invalida {frequency}, deve ser 1, 2, 3, 4, 6')
    return None

def convert_dot_to_comma(number):
    formatted_number = "{:.2f}".format(float(number))
    return formatted_number.replace('.', ',')