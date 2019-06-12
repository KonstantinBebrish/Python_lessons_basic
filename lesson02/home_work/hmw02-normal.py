import math

list = [2, -5, 8, 9, -25, 25, 4]
ResList = []

for num in list:
    
    if num < 0:
        print(f"It's impossible to get a square root from {num}")
    elif (math.sqrt(num) - int(math.sqrt(num))) != 0:
        print(f"The number {num} has no whole square root")
    else:
        ResList.append(int(math.sqrt(num)))
        print(f"The number {num} is added to the list!!")

print(f"The final list looks like that: \n{ResList}")


# Задача 2: Дана дата в формате дд.мм.гггг, например 02.11.2013.
# Вывести дату в текстовом формате например второе ноября 2013 года.

Days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцатьпервое',
    '22': 'двадцатьвторое',
    '23': 'двадцатьтретье',
    '24': 'двадцатьчетвертое',
    '25': 'двадцатьпятое',
    '26': 'двадцатьшестое',
    '27': 'двадцатьседьмое',
    '28': 'двадцатьвосьмое',
    '29': 'двадцатьдевятое',
    '30': 'тридцатое',
    '31': 'тридцатьпервое'
    }
Months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
    }

StrDate = "03.09.2017"

ResDate = ""

print(f"DD = {StrDate[0:2]}")
print(f"MM = {StrDate[3:5]}")
print(f"YYYY = {StrDate[6:10]}")

DD = StrDate[0:2]
MM = StrDate[3:5]
YYYY = StrDate[6:10]

for Day, StrDay in Days.items():
    if Day == DD:
        ResDate += StrDay 
        print(f"Bingo! {ResDate}")

ResDate += " "

for Month, StrMonth in Months.items():
    if Month == MM:
        ResDate += StrMonth
        print(f"Bingo! {ResDate}")

ResDate = "Я календарь переверну и снова " + ResDate + " " + YYYY + " " + "года"

print(f"String representation of the date looks like: \n{ResDate}")


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


import random

n = int(input("Введите количество чисел в списке: "))

List = [random.randint(-100,100) for i in range(n)]

print(List)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить
# lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# B

Lst = [1, 2, 4, 5, 6, 2, 5, 2]


UniqueLst = []

print("\n" * 30)

for num in Lst:
    Approved = 0
    for i in range(0, len(Lst)):
        if Lst[i] == num:
            Approved += 1

    if Approved == 1:
        UniqueLst.append(num)
        print(f"The element {num} is added to the Unique List")
    else:
        print(f"The element {num} is NOT added to the Unique List!")
        

print(f"The final Unique List looks like that:\n{UniqueLst}")
        

# A

Lst = [1, 2, 4, 5, 6, 2, 5, 2]


NewLst = []

print("\n" * 30)

NewLst = set(Lst)
    
print(f"The final New List looks like that:\n{NewLst}")
