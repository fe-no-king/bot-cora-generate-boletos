from datetime import datetime, timedelta

def adjust_day_month(year, month, day):
    """Ajusta o dia do vencimento para o último dia do mês, se necessário."""
    last_day_of_month = (datetime(year, month % 12 + 1, 1) - timedelta(days=1)).day
    return min(day, last_day_of_month)

def add_months(dt, months):
    """Adiciona um número específico de meses a uma data."""
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    day = min(dt.day, (datetime(year, month % 12 + 1, 1) - timedelta(days=1)).day)
    return datetime(year, month, day)

def generate_due_dates(data_start, data_end, day_month, frequency):
    """Gera uma lista de datas de vencimento com base nos parâmetros fornecidos."""
    due_dates = []

    start_date = datetime.strptime(data_start, '%m-%Y').replace(day=1)
    end_date = datetime.strptime(data_end, '%m-%Y').replace(day=1)

    current_date = start_date
    while current_date <= end_date:
        # Ajusta o dia do vencimento
        day_to_use = adjust_day_month(current_date.year, current_date.month, day_month)
        due_date = current_date.replace(day=day_to_use)

        # Verifica se a data de vencimento está dentro do intervalo
        if due_date <= end_date:
            due_dates.append(due_date.strftime('%d-%m-%Y'))

        # Incrementa a data de acordo com a frequência
        current_date = add_months(current_date, frequency)

    return due_dates