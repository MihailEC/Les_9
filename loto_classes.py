import random


class Player:
    def __init__(self, number_player, type_player):
        """
        Присвоение типа игроку, имени, создание карточки игрока
        :param number_player: номер игрока
        :param type_player: тип игрока
        """
        # type_player = input(f'Игрок {count_players} человек или компьютер (ч/к): ')
        # type_player = type_player[:1]
        # type_player = type_player.lower()
        self.type = type_player
        if self.type == 'ч':
            name = input(f'Введите имя игрока {number_player}: ')
            self.name = name
        elif self.type == 'к':
            self.name = f'Компьютер {number_player}'
        else:
            raise ValueError
        numbers = [i for i in range(1, 91)]
        self.card_list = random.sample(numbers, 15)
        self.card_list.sort()
        self.score = 0

    def change_card(self, choice_dice):
        """
        метод изменения карточки игрока
        :param choice_dice: выбранный бочонок
        :return:
        """
        for j in range(0, 15):
            if self.card_list[j] == choice_dice:
                self.card_list[j] = '-'

    def card_print(self):
        """
        Метод вывода карточки игрока
        :return:
        """
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
    choice_dice = random.choice(dice_list) # вытаскиваем случайный бочонок
    print(f'Новый бочонок: {choice_dice} (осталось: {len(dice_list) - 1})')
    dice_list.remove(choice_dice) # удаляем выбранный бочонок
    for i in range(0, count_players): # Цикл хода
        for j in range(0, count_players): # Цикл вывода карточек
            players_list[j].card_print()
        print(f'Ход игрока {players_list[i].name}.')
        if players_list[i].type == 'ч': # условие если игрок человек
            action = input('Зачеркнуть цифру?(д/н): ')
            if choice_dice in players_list[i].card_list and action[:1].lower() == 'д': # сравнение выбранного бочонка с карточкой игрока и выбранного дествия
                players_list[i].change_card(choice_dice) # изменяем карточку игрока
                players_list[i].score += 1 # подсчет очков
            elif choice_dice in players_list[i].card_list and action[:1].lower() == 'н': # сравнение выбранного бочонка с карточкой игрока и выбранного дествия
                print(f'Число в карточке есть! Игрок {players_list[i].name} проиграл!')
                exit()
            elif choice_dice not in players_list[i].card_list and action[:1].lower() == 'н': # сравнение выбранного бочонка с карточкой игрока и выбранного дествия
                continue
            elif choice_dice not in players_list[i].card_list and action[:1].lower() == 'д': # сравнение выбранного бочонка с карточкой игрока и выбранного дествия
                print(f'Числа в карточке нет! Игрок {players_list[i].name} проиграл!')
                exit()
            else:
                print('Неверно введено действие!')
                exit()
        elif players_list[i].type == 'к': # действия когда игрок компьютер
            players_list[i].change_card(choice_dice) # изменяем карточку игрока
            players_list[i].score += 1
