# #запуск скрипта с параметрами, для получения ЗП по формуле (выработка в часах * ставку в час) + премия
# #Запуск через консоль Пусть> python My_Work_4.py (Часы) (Ставка) (Премия)
# #Исправленна ошибка ValueError, для букв.
# from sys import argv
#
#
# def zp(hours, wage, prize):
#     salary = (hours * wage) + prize
#     return print(salary)
#
#
#try:
#    name, hours, wage, prize = argv
#    try:
#        hours = float(hours)
#        wage = float(wage)
#        prize = float(prize)
#        zp(hours, wage, prize)
#    except ValueError:
#        print("Ошибка! Нужно вводить только цифры")
#except ValueError:
#    print("Укажите значения: количество отработанных часов, заработная плата в часах, премия")
##################################################################################################################
# Представлен список чисел(Генератором). Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# import random
# LastNum = 1000
# numbers = [(random.randint(1, 50)) for i in range(10)]
# nextlist_2 = [numbers[num] for num in range(1, len(numbers)) if numbers[num] > numbers[num - 1]]
#
# print(numbers)
# print(nextlist_2)
################################################################################################################
# # Найти числа от 20 до 240, кратные 21 или 20
# print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])
#
################################################################################################################
# # Представлен список чисел. Определить элементы списка, не имеющие повторений.
# import random
# numbers = [(random.randint(-10, 10)) for _ in range(20)]
# print(f"Все числа: {numbers}")
# uniq_list = [el for el in numbers if numbers.count(el) == 1]
# print(f"В строке не повторяются: {uniq_list}")
################################################################################################################
# from functools import reduce
#
# def my_list(el_1, el_2):
#     return el_1 * el_2
#
# uniq_list = [el for el in range (100, 1001, 2)]
# print(f"Четные числа от 100 до 1000:\n{uniq_list}\n<Произведение всех чисел:\n{reduce(my_list, uniq_list)}")
################################################################################################################
# # итератор, генерирующий целые числа, начиная с указанного
# from  itertools import count
# print('Программа генерирует целые числа, начиная с угазанного, для старта необходимо ввести число. '
#       'для выхода из программы - q')
# for i in count(int(input('Введите стартовое число: '))):
#     print(i, end='')
#     quit = input()
#     if quit == 'q':
#         break
################################################################################################################
# # итератор, повторяющий элементы некоторого списка, определенного заранее.
# from  itertools import cycle
# u_list = input('Введите числа, разделяя пробелом: Введите "q" для выхода').split()
# cycler = cycle(u_list)
# quite = None
# while quite != 'q':
#     print(next(cycler), end='')
#     quite = input().lower()
################################################################################################################
# # Реализовать генератор с помощью функции с ключевым словом yield. Найти факториал,
# # постоянно выводить 2!=2, 3!=6 и т.д.
# def fact_gen(number):
#     f_num = 1
#     if number == 0:
#         yield f'{number}! = 1'
#     for i in range(1, number + 1):
#         f_num *= i
#         yield f'{i}!={f_num}'
#
#
# for el in fact_gen(int(input('Factorial number: '))):
#     print(el)
