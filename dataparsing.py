from datetime import date
from data import add_expenses, last_data, delete_specific_data, specific_data_id


def specific_insert(text:str):
    a = list(text.split('..'))  
    if a[-1] == '':
        a[-1] = 0
    try:
        for i in range(len(a)):
            a[i] = a[i].strip()
    except:
        pass
    a[4] = int(a[4])
    a[5] = int(a[5])
    add_expenses(a)




def parsing(text: str):
    d = date.today()
    a = list(text.split(".."))
    a.insert(0, str(d))
    if a[-1] == '':
        a[-1] = 0

    try:
        for i in range(len(a)):
            a[i] = a[i].strip()
    except:
        pass
    a[4] = int(a[4])
    a[5] = int(a[5])
    add_expenses(a)




def parser(text:str):
    text2 = text.split('..')
    if len(text2) == 1:
        text3 = text.split()
        a = specific_data_id(text3[1])
        delete_specific_data(text3[1])
        return f'Удалил: \n{a}'
    elif len(text2) == 5:
        parsing(text)
        data_to_print = last_data()
        return f'Добавил: \n{data_to_print}'
    elif len(text2) == 6:
        specific_insert(text)
        data_to_print = last_data()
        return f'Добавил: \n{data_to_print}'


# print(parser('01.01.2021.. Единицы.. Гурам.. .. 200..'))
# parser('Удали 28')