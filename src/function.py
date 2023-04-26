import json
from datetime import datetime

"Переводим json-файл в список"
def execute(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    execute = []
    for i in data:
            execute.append(i)
    return execute


"Создаем список выполненных операций (EXECUTED)"
def filter_by_state(lst):
    new_lst = []
    for item in lst:
        if 'state' in item and item['state'] == 'EXECUTED':
            new_lst.append(item)
    return new_lst


"Сортируем список по дате, в порядке убывания"
def sort_by_date(lst):
    return sorted(lst, key=lambda x: x['date'], reverse=True)


"Создаем список из пяти самых свежих операций"
def print_first_five_operations(lst):
    first_five_operations = lst[:5]
    return  first_five_operations


"Получаем первую операцию и все что с ней связано"
def get_first_id_info(lst):
    first_operation = lst[0]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info


"Получаем вторую операцию и все что с ней связано"
def get_second_id_info(lst):
    first_operation = lst[1]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info


"Получаем третью операцию и все что с ней связано"
def get_third_id_info(lst):
    first_operation = lst[2]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info


"Получаем четвертую операцию и все что с ней связано"
def get_fourth_id_info(lst):
    first_operation = lst[3]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info


"Получаем пятую операцию и все что с ней связано"
def get_five_id_info(lst):
    first_operation = lst[4]
    first_id = first_operation['id']
    first_id_info = []
    for operation in lst:
        if operation['id'] == first_id:
            first_id_info.append(operation)
    return first_id_info


"Получаем описание типа перевода"
def get_description(data):
    return data[0]['description']


"Получаем дату операции"
def get_date(data):
    date = data[0]['date']
    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_obj.strftime('%d.%m.%Y')


"Получаем счет, куда переводим деньги"
def get_to(accounts):
    for account in accounts:
        to = account['to']
    last_four = to[-4:]
    formatted = f"Счет **{last_four}"
    return formatted

"Получаем количество денег участвующих в операции"
def get_amount_from_list(transactions):
    amounts = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError('Input parameter must be a list of dictionaries')
        if 'operationAmount' in transaction and isinstance(transaction['operationAmount'], dict) and 'amount' in transaction['operationAmount']:
            amounts.append(float(transaction['operationAmount']['amount']))
        for i in amounts:
            return i

"Получаем информацию откуда переводили деньги"
def gettofromlist(transactions):
    tolist = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError('Input parameter must be a list of dictionaries')
        if 'from' in transaction:
            tolist.append(transaction['from'])
    result = ''
    for i in tolist:
        words = i.split()
        for word in words:
            if any(char.isdigit() for char in word) and len(word)>=16 and len(word)<=19:
                result += word[:4] + ' ' + word[4:6] + '**' + ' ' + '****' + ' ' + word[-4:] + ' '
            elif word.isalpha() or word.isspace():
                result += word + ' '
    return result.strip()
