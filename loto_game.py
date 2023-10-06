import loto_classes

dice_list = [i for i in range(1, 91)]

win_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

try:
    count_players = int(input('Введите количество игроков: '))
except ValueError:
    print('Введите число! Выходим.')
    exit()

players_list = []
try:
    for i in range(1, count_players + 1):
        type_player = input(f'Игрок {count_players} человек или компьютер (ч/к): ')
        type_player = type_player[:1]
        type_player = type_player.lower()
        players_list.append(loto_classes.Player(i, type_player))
except ValueError:
    print('Неверно введен тип игрока! Выходим')
    exit()

# выполняем
for i in range(1, 91):
    loto_classes.circle_of_players(dice_list, players_list, count_players)
    for j in range(0, count_players):
        if players_list[j].card_list == win_list:
            print(f'Победил игрок {players_list[j].name}. Количество очков: {players_list[j].score}')
            exit()
