import loto_classes, random

win_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

dice_list = [i for i in range(1, 91)] # задание мешка с бочонками

try:
    count_players = int(input('Введите количество игроков: '))
except ValueError:
    print('Введите число! Выходим.')
    exit()

players_list = []
try:
    # цикл задания имени и типа игроков
    for i in range(1, count_players + 1):
        type_player = input(f'Игрок {i} человек или компьютер (ч/к): ')
        type_player = type_player[:1].lower()
        if type_player == 'ч':
            name = input(f'Введите имя игрока {i}: ')
        elif type_player == 'к':
            name = f'Компьютер {i}'
        else:
            raise TypeError('Неправильный тип игрока.')
        players_list.append(loto_classes.Player(i, type_player, name)) # добавление игроков в список
except TypeError:
    print('Неверно введен тип игрока! Выходим')
    exit()

# код игры
while dice_list != []:
    # выбор бочонка из списка dice_list
    choice_dice = random.choice(dice_list)
    print(f'Новый бочонок: {choice_dice} (осталось: {len(dice_list) - 1})')
    dice_list.remove(choice_dice)

    for i in range(0, count_players): # Цикл игры
        players_list[i].card_print() # Вывод карточки игрока
        print(f'{str(players_list[i])} ходит')
        if players_list[i].check_type(): # проверка типа игрока (ч/к)
            action = input('Зачеркнуть цифру?(y/n): ') # предложение сделать ход если человек
            action = action[:1].lower()
            if players_list[i].check_number_in_card(choice_dice): # проверка наличия числа на бочонке в карточке игрока 
                if action == 'y': # проверка введенного действия
                    players_list[i].change_card(choice_dice) # изменение карточки игрока
                else:
                    print(f'Число в карточке есть! Игрок {str(players_list[i])} проиграл! Игра закончена.') # проигрыш игрока если он неверно выбрал
                    exit()
            else:
                if action == 'y': # проверка введенного действия
                    print(f'Числа в карточке нет! Игрок {str(players_list[i])} проиграл! Игра закончена.') # проигрыш игрока если он неверно выбрал
                    exit()
                else:
                    continue # действие введено верно и игра продолжается
        else: # действия если тип игрока компьютер
            if players_list[i].check_number_in_card(choice_dice): # проверка наличия числа на бочонке в карточке игрока
                players_list[i].change_card(choice_dice) # изменение карточки игрока при наличии числа в карточке
            else:
                continue # игра продолжается так как числа в карточке нет
# Проверка на условие выйгрыша   
    for j in range(0, count_players):
        if players_list[j] == win_list:
            print(f'Победил {str(players_list[i])}! Игра закончена.')
            exit()
