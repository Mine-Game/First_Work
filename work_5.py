# # Создание файла в текстовом формате, запись в него построчно данных,которые вводит пользователь.
# # Об окончании ввода данных свидетельствует пустая строка.
# from itertools import count
# # out_f - создано для удобства, чтобы перезаписывать файл при старте :)
# out_f = open( "text_123.txt" , "w" )
# out_f.close()
# for i in count():
#     UserText = input("Введите текст, который нужно записать в фаил, нажмите 'Enter': ")
#     if UserText == '':
#         break
#     with open("text_123.txt", "a", encoding="utf-8") as wood:
#             wood.write(f"{UserText}\n")
##################################################################################################
# # подсчет количества строк и слов в каждой строке выбранного файла.
# strNum = 0
# with open('text_123.txt', 'r') as f:
#     for line in f:
#         strNum = strNum + 1
#         f = line.split()
#         s = len(f)
#         print(f"Колличество слов в строке {strNum}: {s}")
# with open('text_123.txt', 'r') as f:
#     LenText = len(f.headlines())
#     print(f"Количество строк файле: {LenText}")
###########################################
# # Из файла с фамилией и зп -
# # Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# # Выполнить подсчет средней величины дохода сотрудников.
# import re
# def search_number_string(string):
#     index_list = []
#     del index_list[:]
#     for i, x in enumerate(string):
#         if x.isdigit() == True:
#             index_list.append(i)
#     start = index_list[0]
#     end = index_list[-1] + 1
#     number = string[start:end]
#     return number
#
#
# familyAll = []
# SalaryAll = []
# AllSalary = 0
# with open('text_123.txt', 'r', encoding="utf-8") as wood:
#     listMemers = wood.readlines()
#     print(listMemers)
#     for i in listMemers:
#         Sallaary = search_number_string(i)
#         SalaryAll.append(Sallaary)
#         AllSalary = (float(AllSalary) + float(Sallaary))
#         family = re.sub(r'[^\w\s]+|[\d]+', r'', i).strip()
#         familyAll.append(family)
#
# print(f'Средняя зарплата сотрудников: {AllSalary/10}')
# print("Фамилии сотрудников с заработной платой менее 20000: ")
# n = 0
# for i in SalaryAll:
#     i = float(i)
#     n = n + 1
#     if i <= 20000:
#         print(familyAll[n])
#####################################################################################
# # Создать (не программно) текстовый файл со следующим содержимым:
# # One — 1
# # Two — 2
# # Three — 3
# # Four — 4
# # Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# # данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# # должен записываться в новый текстовый файл.
# rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
#
# with open("text_ru.txt", "w", encoding="utf-8") as new_file:
#     with open("text_r.txt", encoding="utf-8") as my_file:
#         new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])
######################################################################################
# # Создать (программно) текстовый файл, записать в него программно набор чисел,
# # разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# # ее на экран.
# from random import randint
#
# with open('text.txt', 'w', encoding='utf-8') as my_file:
#     my_list = [randint(1, 100) for _ in range(100)]
#     my_file.write(''.join(map(str, my_list)))
#
# print(f"Сумма элементов - {sum(my_list)}")
######################################################################################
# # Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# # предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# # количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# # Сформировать словарь, содержащий название предмета и общее количество занятий по
# # нему. Вывести словарь на экран.
# mydict = {}
# with open("text_6.txt", encoding="utf-8") as fobj:
#     for line in fobj:
#         name, stats = line.split(':')
#         name_sup = sum(map(int, "".join([i for i in stats if i == '' or '9' >=i >= '0']).split()))
#         mydict[name] = name_sup
#     print(f"{mydict}")
#####################################################################################################