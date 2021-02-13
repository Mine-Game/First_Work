from datetime import timedelta

# Введите время в сек. получите в формате День, Часы:Минуты:Секунды.
second = int(input("Введите вермя в секундах: "))

Time = "{}".format(str(timedelta(seconds=second)))
print(Time)

# Введите любое число N получите "n+nn+nnn=(Ответ)"
n = int(input("Введите число N: "))
n2 = f"{n}" + f"{n}"
n3 = f"{n}" + f"{n}" + f"{n}"
n2 = (int(n2))
n3 = (int(n3))
print(f"{n}+{n}{n}+{n}{n}{n}={n + n2 + n3}")


# Подсчёт максильного числа
Numbers = input("Введите целое число: ")
i = len(Numbers)
Number = int(Numbers)
i2 = 0
maxNum = 0
while Number != 0:
    lastNumb = Number % 10
    Number = Number // 10
    if lastNumb > maxNum:
        maxNum = lastNumb
    elif lastNumb < maxNum:
        continue
print(maxNum)


# Расчёт прибыли, рентабельности, прибыли в расчёте на одного сотрудника компании

Revenue = int(input("Введите значение выручки вашей компании: "))
Costs = int(input("Введите значение издержек вашей компании: "))

if Revenue > Costs:
    print(f"Прибыль равна: {Revenue - Costs}")
    Profitability = Revenue/Costs
    print(f"Рентабельность компании: {Profitability:.2}")
    employees = int(input("Введите Количество сотрудников: "))
    RevenueOneEmployees = (Revenue - Costs)/employees
    print(f"Прибыль в расчёте на одного сотрудника компании: {RevenueOneEmployees}")
elif Costs > Revenue:
    print(f"Убыток равен: {Costs - Revenue}")

# Через сколько дней я смогу бегать нужное количество км.
Distance = int(input("Укажите колличество киллометров на первый день: "))
DistanceLast = int(input("Укажите КМ в конце, сколько хотите бегать: "))
Procente = int(input("Введите процент: "))
Procente = Procente/100


i = 0
while True:
    i += 1
    if Distance >= DistanceLast:
        print(f"Ответ: На {i-1} день, спортсмен достиг результата - не менее {DistanceLast}КМ в день.")
        break
    else:
        Distance = (Distance * Procente)+Distance
        print(f"День {i}: {Distance:.3}")
        continue
