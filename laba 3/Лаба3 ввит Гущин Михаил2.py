def write_new_file():
    text = input('Введите текст для записи в новый файл: ')
    with open('user_input.txt', 'w') as f:
        f.write(text)


def append_in_file():
    text = input('Введите текст для добавления в новый файл: ')
    with open('user_input.txt', 'a') as f:
        f.write('\n' + text)

wr = 0
wr = int(input("Режим записи: (создание нового файла - 1; добавление в файл - 2): "))
if wr==1:
    write_new_file()
elif wr==2:
    while wr==2:
        append_in_file()
        wr = int(input('продолжение записи - 2: '))
        if wr != 2:
            break
        
