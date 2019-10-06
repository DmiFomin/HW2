while True:
    year = input('В каком году родился Пушкин А.С.? ')
    if (year == '1799'):
        print('Верно')
        while True:
            day = input('День рождения? ')
            if (day == '26'):
                print('Верно')
                break
            else:
                print('Неверный день')
        break
    else:
        print('Неверный год')

print('The End')