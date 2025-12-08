import my_module

try:        
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    s = my_module.sumnum(a,b)
    print(s)
except ValueError:
    print("Ошибка: введены некорректные данные. Пожалуйста, введите числа.")