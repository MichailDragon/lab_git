from moduleee import numbers, strings

try:
    a = float(input('Введите число: '))
    b = float(input('Введите число: '))
    print("Сумма чисел:", numbers.sumnum(a, b))
    print("Произведение чисел:", numbers.umnnum(a, b))
except ValueError:
    print("Ошибка: введены некорректные данные.")
    

text = input("Введите текст: ")
print("перевернутый текст: ", strings.revese_string(text))
print("количество символов в тексте: ", strings.count(text))