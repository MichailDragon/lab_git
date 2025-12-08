def read_all(filee):
    try:
        with open(filee, 'r') as file:
            print("=== Чтение всего файла ===")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filee}' не найден.")

def read_lines(fl):
    try:
        with open(fl, 'r') as file:
            print("=== Построчное чтение ===")
            line_num = 1
            for line in file:
                print(f"{line_num}: {line}", end='')
                line_num += 1
    except FileNotFoundError:
        print(f"Ошибка: файл '{fl}' не найден.")

r = int(input("Режим чтения: (всего файла - 1; построчно - 2): "))
if r==1:
    read_all('example.txt')
elif r==2:
    read_lines('example.txt')
else:
    print('идите нафиг нет такого типа чтения')















#def read_all(filee):
    #"""Читает и выводит весь файл сразу."""
    #try:
        #with open(filee, 'r') as file:
            #print("=== Чтение всего файла ===")
            #print(file.read())
    #except FileNotFoundError:
        #print(f"Ошибка: файл '{filee}' не найден.")


#def read_lines(filee):
    #"""Читает и выводит файл построчно с нумерацией."""
    #try:
        #with open(filee, 'r') as file:
            #print("=== Построчное чтение ===")
            #line_num = 1
            #for line in file:
                #print(f"{line_num}: {line.rstrip()}")
                #line_num += 1
    #except FileNotFoundError:
        #print(f"Ошибка: файл '{filee}' не найден.")


## Выполнение задания 1
#read_all('example.txt')

#read_lines('example.txt')