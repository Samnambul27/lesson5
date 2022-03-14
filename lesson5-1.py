print('Введите данные для записи в файл \n Для окончания ввода введите пустую строку')
with open('task_1.txt', 'w', encoding='utf-8') as my_fail:
    while(line := input()) != '':
        my_fail.write(f'{line}\n')