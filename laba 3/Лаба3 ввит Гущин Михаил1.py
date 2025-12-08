def read_all(filee):
    """Читает и выводит весь файл сразу."""
    with open(filee, 'r') as file:
        print("=== Чтение всего файла ===")
        content = file.read()
        print(content)

def read_lines(fl):
    """Читает и выводит файл построчно с нумерацией."""
    with open(fl, 'r') as file:
        print("=== Построчное чтение ===")
        line_num = 1
        for line in file:
            print(f"{line_num}: {line}", end='')
            line_num += 1

# Выполнение задания 1

r = int(input("Режим чтения: (всего файла - 1; построчно - 2): "))
if r==1:
    read_all('example.txt')
elif r==2:
    read_lines('example.txt')
else:
    print('идите нафиг нет такого типа чтения')