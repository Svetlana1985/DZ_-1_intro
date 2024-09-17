# #1
# num_1 = int(input('Введите любое число: '))
# num_2 = int(input('Введите любое число: '))
# num_3 = int(input('Введите любое число: '))
# summa = num_1 + num_2 + num_3
# prod = num_1 * num_2 * num_3
# print(f'Сумма чисел: {summa}')
# print(f'Произведение чисел: {prod}')
import math
import random

# #2
# num_1 = int(input('Введите сумму з/п: '))
# num_2 = int(input('Введите сумму выплат по кредиту за месяц: '))
# num_3 = int(input('Введите сумму задолженности за коммунальные услуги: '))
# result = num_1 - num_2 - num_3
# print(f'Сумма, оставшаяся после выплат: {result}')

# #3
# num_1 = int(input('Введите длину диагонали ромба "A": '))
# num_2 = int(input('Введите длину диагонали ромба "B": '))
# if num_1 <= 0 or num_2 <= 0:
#     print('Диагональ не может иметь отрицательное значение или равна "0"')
# else:
#     print(f'Площадь ромба: {(num_1 * num_2) / 2}')

#4
import random

num_x = random.randint(0,1000)
sum_num = 0
print(f'Рандомное число: {num_x}')
for i in str(num_x):
    sum_num += int(i)
print(f'Сумма цифр рандомного числа: {sum_num}')
if num_x % 2 == 0 and sum_num % 3 ==0:
    print(f'Число делится на 6: {num_x}')
else:
    print(f'Число не делится на 6: {num_x}')



