#import math
#num = int(input('Введите целое число: ' ))
#r = math.sqrt(num)
#print(r)


import math
import datetime

#4.1
def sqrt(num):
    return math.sqrt(num)
num = float(input('Введите число для вычисления квадратного корня: '))
r = sqrt(num)
print("Квадратный корень: ", r)


#4.2
tm = datetime.datetime.now()
print('Текущее время и дата: ', tm)