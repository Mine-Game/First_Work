# # Отображение всех эллементов типов
# my_list = ["str", 123, 12.21, False, [1, 2], (3, 4), {5, 6}]
#
# for num, i in enumerate(my_list):
#     print(f"{num}) {type(i)}")

# # обмен значений соседних элементов списка приведённого через input
# l = int(input("Введите колличество элементов списка: "))
# k = 0
# addList = []
#
# while k != l:
#     k += 1
#     m = input(f"Введите {k} значение из списка: ")
#     addList.append(m)
#
# ne_list = addList
# j = 0
# for i in range(int(len(ne_list) / 2)):
#     ne_list[j], ne_list[j + 1] = ne_list[j + 1], ne_list[j]
#     j += 2
#
# print(ne_list)

# # Используем list для решения задачи: найти время года по месяцу
# Winter = [12, 1, 2]
# Spring = [3, 4, 5]
# Summer = [6, 7, 8]
# Autumn = [9, 10, 11]
#
# month = int(input("Введите номер месяца: "))
#
# if month in Winter:
#     print("Зима")
# elif month in Spring:
#     print("Весна")
# elif month in Summer:
#     print("Лето")
# elif month in Autumn:
#     print("Осень")

# # Используем dict
# month = int(input("Введите номер месяца: "))
# my_dict = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
#
# for el in my_dict:
#     if month in my_dict[el]:
#         print(f"Сейчас: {el} ")

# # Пользователь вводит слова разделенные пробелами, получает их в строчку, если длина слова более 10 букв,
# # видно только первые 10
# in_put_list = input('Введите слова разделенные пробелами: ')
#
# list_split = in_put_list.split()
# print(list_split)
# k = 0
# for i in list_split:
#     print(f"{k}) {i[0:10]}")
#     k += 1

# # Рейтинг План, Какждая новая цифра обязательно добавляется сзади такой же цифры.
# my_list = [7, 5, 3, 3, 2]
# while True:
#     new_number = int(input("Введите новый элемент рейтинга: "))
#     i = 0
#     for n in my_list:
#         if new_number <=n:
#             i +=1
#     my_list.insert(i,new_number)
#     print(my_list)

# Система учёта товара и аналитика
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжеия "Enter": ').upper() == 'Q':
        break
    num +=1
    for f in features.keys():
        pro = input(f'Введите значение свойства "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append((features[f]))
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)