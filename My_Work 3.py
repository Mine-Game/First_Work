################################################################################################
# # Функция деления, обработана ошибка деления на 0 и ошибочный ввод
# def del_func(one, two):
#     try:
#         one = int(one)
#         two = int(two)
#         Division = one / two
#         return print(Division)
#     except ZeroDivisionError:
#         print("Ошибка, на ноль делить нельзя.")
#     except ValueError:
#         print("Вы ввели ошибочное значение, введите число.")
#
#
# del_func((input("Введите числитель для деления: ")), (input("Введите знаменатель для деления: ")))
################################################################################################
# # функцию, принимающую несколько параметров, описывающих данные пользователя,
# # вывод одной строкой
# def return_f(**kwargs):
#     print(kwargs)
#
# name_s = input("Введите имя: ")
# phone_s = input("Введите номер телефона: ")
# adres_s = input("Введите адрес: ")
# email_s = input("Введите email: ")
# return_f(name=name_s, phone=phone_s, adres=adres_s, email=email_s)
################################################################################################
# Получаем 3 числа от пользователя, выводим 2 максимальных числа
# def my_func(First, Second, Third):
#     my_list = [First, Second, Third]
#     try:
#         my_list.remove(min(my_list))
#         return sum(my_list)
#     except TypeError:
#         return "Enter only a numbers"
#
# 
# print(my_func(2, 11, -30))
################################################################################################
# # Умножение числа в степень
# # Cложная реализация без оператора **, предусматривающая использование цикла.
# def steppe(x, y):
#     i = 1
#     s = i * -1
#     sr = x
#     if y < 0:
#         while s != y:
#             sr = sr * x
#             i += 1
#             s -= 1
#         sr = 1 / sr
#     elif y > 0:
#         while i != y:
#             sr = sr * x
#             i += 1
#             s -= 1
#     return sr
#
# num_st = float(input("Введите число: "))
# steppe_n = int(input("Введите степень: "))
#
# print(steppe(num_st, steppe_n))
################################################################################################
# # Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# # При нажатии Enter должна выводиться сумма чисел
# # Обработаны ошибки и поломки программы, создан выход через 'q'
# new_number_int = []
# t = False
#
# while t != True:
#     numbers_all = input("Введите числа разделенные пробелом: ")
#     numbers_all = numbers_all.split()
#
#     for i in numbers_all:
#         if i == "q":
#             t = True
#             break
#         elif i == "Q":
#             t = True
#             break
#         try:
#             i = int(i)
#             new_number_int.append(i)
#         except ValueError:
#             print("Для выхода введите 'q' ")
#
#     new_number_2 = sum(new_number_int)
#     print(new_number_2)
################################################################################################
# При вводе слов в любом регистре, через пробел, система выдаёт слова, только в английском регистре,
# делает первую букву заглавной.
# "nice авп ъghj jапро hjjпаро вапрghgh cool" из этого выражения выводится только Nice и Coll
# rus_lower = set('abcdefghijklmnopqrstuvwxyz')
# rus_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# symbols = set('!?:;"., ').union("123456789")
#
#
# def title_f(text):
#     text_filter_list = []
#     for i in text:
#         if set(i).difference(set.union(rus_lower, symbols, rus_upper)):
#             continue
#         else: text_filter_list.append(i)
#     return text_filter_list
#
#
# text = input("Введите слова с маленькой буквы: ")
# text = text.title()
# text = text.split()
# text = title_f(text)
# print(text)
