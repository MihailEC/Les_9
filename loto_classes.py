import random


class Player:
    def __init__(self, number_player, type_player, name_player):
        # входные данные: номер игрока, тип игрока(ч/к), имя игрока
        self.type = type_player # присвоение типа игрока
        self.name = name_player # присвоение имени
        self.number_player = number_player # присвоение номера игрока
        numbers = [i for i in range(1, 91)] # задание списка отбора для карточки игрока
        self.card_list = random.sample(numbers, 15) # отбор для карточки
        self.card_list.sort()
        

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

    def check_number_in_card(self, number):
        if number in self.card_list:
            return True
        else:
            return False
   
    def check_type(self):
        if self.type == 'ч':
            return True
        else:
            return False

    def check_win(self, win_list):
        if win_list == self.card_list:
            return True
        else:
            return False