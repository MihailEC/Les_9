import random

from loto_classes import Player

player_one = Player()
card_p_one = player_one.card_list
player_two = Player()
card_p_two = player_two.card_list

dice_list = [i for i in range(1, 91)]

win_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

while card_p_one != win_list or card_p_two != win_list:
    # TODO: 1. сделать сортировку по возрастанию для каждой строки чисел в карточке
    # TODO: 2. сделать функции вывода карточек в классе или отдельно
    choice_dice = random.choice(dice_list)
    print(f'Новый бочонок: {choice_dice} (осталось: {len(dice_list) - 1})')
    dice_list.remove(choice_dice)
    print(f'------Карточка {player_one.name}------')
    print(card_p_one[0:4])
    print(card_p_one[5:9])
    print(card_p_one[10:15])
    print('---------------------------------------')

    print(f'------Карточка {player_two.name}------')
    print(card_p_two[0:4])
    print(card_p_two[5:9])
    print(card_p_two[10:15])
    print('---------------------------------------')
    action = input('Зачеркнуть цифру?(y/n): ')
# TODO: добавить метод изменения карточки в классе
    if player_one.type == 'человек' and action == 'y':
        if choice_dice in card_p_one:
            for j in range(len(card_p_one)):
                if card_p_one[j] == choice_dice:
                    card_p_one[j] = '-'
        else:
            print(f'Числа в карточке нет! Игрок {player_one.name} проиграл!')
            break
    elif player_two.type == 'человек' and action == 'y':
        if choice_dice in card_p_two:
            for j in range(len(card_p_two)):
                if card_p_two[j] == choice_dice:
                    card_p_two[j] = '-'
        else:
            print(f'Числа в карточке нет! Игрок {player_two.name} проиграл!')
            break
    elif player_one.type == 'компьютер':
        for j in range(len(card_p_one)):
            if card_p_one[j] == choice_dice:
                card_p_one[j] = '-'
    elif player_two.type == 'компьютер':
        for j in range(len(card_p_two)):
            if card_p_two[j] == choice_dice:
                card_p_two[j] = '-'
    else:
        print('Тип игрока не определен!')
        break
# TODO: сделать подсчет количества очков и вывод победителя