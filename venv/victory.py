print('Я хочу сыграть с тобой в одну игру...')
print('В ВИКТОРИНУ!!!')

again = 'Да'

while again == 'Да':

    count_true = 0;
    count_false = 0;
    percent_true = 0
    percent_false = 0

    # Илон Маск - 1971
    year = input('Год рождения Илона Маска? ')
    if (year == '1971'):
        print('Вы ответили верно!')
        count_true += 1
    else:
        print('Ответ неправильный')
        count_false += 1

    # Альберт Эйнштейн - 1879
    year = input('Год рождения Альберта Эйнштейна? ')
    if (year == '1879'):
        print('Вы ответили верно!')
        count_true += 1
    else:
        print('Ответ неправильный')
        count_false += 1

    # Чарльз Дарвин - 1809
    year = input('Год рождения Чарльза Дарвина? ')
    if (year == '1809'):
        print('Вы ответили верно!')
        count_true += 1
    else:
        print('Ответ неправильный')
        count_false += 1

    # Владимир Челомей - 1914
    year = input('Год рождения Владимира Челомея? ')
    if (year == '1914'):
        print('Вы ответили верно!')
        count_true += 1
    else:
        print('Ответ неправильный')
        count_false += 1

    # Архимед - 287
    year = input('Год рождения Архимеда (до нашей эры)? ')
    if (year == '287'):
        print('Вы ответили верно!')
        count_true += 1
    else:
        print('Ответ неправильный')
        count_false += 1

    percent_true = count_true * 100 / 5
    percent_false = count_false * 100 / 5

    if (percent_true == 100):
        print('Ты ответил правильно на все вопросы! Поздравляю!')
    elif (percent_false == 100):
        print('Ничего ты не знаешь, Джон Сноу! Иди читай википедию!')
    else:
        print('Правильные ответы: ', str(percent_true), ';', 'Неправильные ответы', str(percent_false))

    again = input('Хочешь ли попробовать заново? ')

print('Игра закончена!')
