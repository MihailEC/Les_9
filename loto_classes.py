import random


class Player:
    def __init__(self, count_players):
        type_player = input(f'Игрок {count_players} человек или компьютер (ч/к): ')
        type_player = type_player[:1]
        type_player = type_player.lower()
        self.type = type_player
        if self.type == 'ч':
            name = input(f'Введите имя игрока {count_players}: ')
            self.name = name
        elif self.type == 'к':
            self.name = f'Компьютер {count_players}'
        else:
            raise ValueError
        numbers = [i for i in range(1, 91)]
        self.card_list = random.sample(numbers, 15)
        self.card_list.sort()
        self.score = 0

    def change_card(self, choice_dice):
        for j in range(0, 15):
            if self.card_list[j] == choice_dice:
                self.card_list[j] = '-'

    def card_print(self):
        card_list_1 = self.card_list[:5]
        card_list_2 = self.card_list[5:10]
        card_list_3 = self.card_list[10:15]
        card_list_1 = map(str, card_list_1)
        card_list_2 = map(str, card_list_2)
        card_list_3 = map(str, card_list_3)
        print(f'------Карточка {self.name}------')
        print(' '.join(card_list_1))
        print(' '.join(card_list_2))
        print(' '.join(card_list_3))
        print('---------------------------------------')


def circle_of_players(dice_list, players_list, count_players):
    """
    Функция для игры в лото. Проход одного круга по игрокам.
    :param dice_list: Список цифр в мешке.
    :param players_list: Список игроков.
    :param count_players: Количество игроков
    :return:
    """
    choice_dice = random.choice(dice_list)
    print(f'Новый бочонок: {choice_dice} (осталось: {len(dice_list) - 1})')
    dice_list.remove(choice_dice)
    for i in range(0, count_players):
        # Цикл вывода карточек
        for j in range(0, count_players):
            players_list[j].card_print()
        print(f'Ход игрока {players_list[i].name}.')

        if players_list[i].type == 'ч':
            action = input('Зачеркнуть цифру?(y/n): ')
            action = action[:1]
            action = action.lower()
            if choice_dice in players_list[i].card_list and action == 'y':
                players_list[i].change_card(choice_dice)
                players_list[i].score += 1
            elif choice_dice in players_list[i].card_list and action == 'n':
                print(f'Число в карточке есть! Игрок {players_list[i].name} проиграл!')
                exit()
            elif choice_dice not in players_list[i].card_list and action == 'n':
                continue
            elif choice_dice not in players_list[i].card_list and action == 'y':
                print(f'Число в карточке нет! Игрок {players_list[i].name} проиграл!')
                exit()
            else:
                print('Неверно введено действие!')
                exit()
        elif players_list[i].type == 'к':
            players_list[i].change_card(choice_dice)
            players_list[i].score += 1
