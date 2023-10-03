import random


class Player:
    def __init__(self):
# TODO: сделать определение человека проще. Возможно сначала просить ввести формат игры. С компьютером или с человеком.
        self.name = input('Введите имя игрока: ')
        self.type = input('Введите тип игрока (человек/компьютер): ')
        numbers = [i for i in range(1, 91)]
        self.card_list = random.sample(numbers, 15)

    def change_card(self):
        pass