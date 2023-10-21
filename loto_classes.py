import random


class Player:
    def __init__(self, number_player, type_player, name_player):
        """
        присвоение типа, имени, номера игрока и его карточки
        :param number_player: номер игрока
        :param type_player: тип игрока (ч/к)
        :param name_player: имя игрока
        """
        # входные данные: номер игрока, тип игрока(ч/к), имя игрока
        self.type = type_player # присвоение типа игрока
        self.name = name_player # присвоение имени
        self.number_player = number_player # присвоение номера игрока
        numbers = [i for i in range(1, 91)] # задание списка отбора для карточки игрока
        self.card_list = random.sample(numbers, 15) # отбор для карточки
        self.card_list.sort()

    def __str__(self):
        """
        При приведении объекта к строке выводится "Игрок (номер игрока): (имя игрока)"
        :return: "Игрок (номер игрока): (имя игрока)"
        """
        if self.type == 'ч':
            return f'Игрок {self.number_player}: {self.name}'
        else:
            return f'Компьютер {self.number_player}'

    def __eq__(self, other):
        """
        сравнение карточки игрока с другим объектом (например списком для выйгрыша)
        :param other: список или карточка другого игрока
        :return: True - если равны, False - если не равны
        """
        return self.card_list == other
        

    def change_card(self, choice_dice):
        """
        изменение карточки игрока
        :param choice_dice: выбранное значение для удаления из карточки
        :return: изменяет список карточки игрока
        """
        for j in range(0, 15):
            if self.card_list[j] == choice_dice:
                self.card_list[j] = '-'

    
    def card_print(self):
        """
        Вывод карточки игрока в консоль
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

    def check_number_in_card(self, number):
        """
        проверка наличия номера в карточке
        :param number: номер для сравнения
        :return: True - если номер есть в карточке, False - если нет номера в карточке
        """
        if number in self.card_list:
            return True
        else:
            return False
   
    def check_type(self):
        """
        проверка типа игрока (ч/к)
        :return: True - если человек(ч), False - если компьютер(к)
        """
        if self.type == 'ч':
            return True
        else:
            return False

    # def check_win(self, win_list):
    #     """
    #     сравнение каточки игрока с другим списком
    #     :param win_list: список
    #     :return: True - если карточка и список равны, False - если не равны
    #     """
    #     if win_list == self.card_list:
    #         return True
    #     else:
    #         return False