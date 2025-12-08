#1.1
def greet(name):
    return ('Здравствуйте,', name)
name1 = str(input('Введите ваше имя: '))
print(greet(name1)) 

#1.2
def square(number):
    return number**2
num = float(input('Введите число для возведения в квадрат: '))
print('Квадрат чила:', square(num))

#1.3
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
x = float(input('Введете x: '))
y = float(input('Введите y: '))
print('Большее число:', max_of_two(x, y))

#2
def describe_person(namee, age=30):
    return ('Имя человека:', namee, ', Возраст:', age)
name2 = str(input('Введите имя: '))
age = input('Введите возраст (или оставьте пустым для заполнения автоматически): ')
if age == '':
    print (describe_person(name2)) 
else:
    print(describe_person(name2, int(age))) 

#3
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

n = int(input("Введите целое число для проверки на простоту: "))
if is_prime(n):
    print(f"Число {n} — простое.")
else:
    print(f"Число {n} — не является простым.")
