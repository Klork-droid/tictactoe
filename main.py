import pickle
import argparse
import random


class Game:
    counter = 0
    place = [[0], [0]]
    row = 0
    column = 0
    error = False
    continue_game = True

    class InputChar:
        PLAYER = 'X'
        COMPUTER = 'O'


def calc_xy(value):
    """Возвращает позицию введенного элемента в массиве"""
    y_num = int((value - 1) / Game.column)
    x_num = int((value - 1) % Game.column)
    return y_num, x_num


def save(data):
    """Сохранение ключевых данных"""
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)


def load():
    """Загрузка ключевых данных"""
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
    return data


def create_key_data(check_load):
    """Создание нового массива или загрузка массива из файла сохранения"""
    if check_load == 'true':
        data = load()
        Game.place = data.get('place')
        Game.counter = data.get('counter')
        Game.row = data.get('row')
        Game.column = data.get('column')

    elif args.n.isdigit() and args.k.isdigit():
        Game.row = int(args.n)
        Game.column = int(args.k)
        Game.place = [[0] * Game.column for _ in range(Game.row)]
        for i in range(Game.row):
            for j in range(Game.column):
                Game.place[i][j] = 1 + Game.column * i + j
        Game.counter = 0

    else:
        print('Аргументы n и k должны принимать числа')
        Game.error = True


def draw_place():
    """Отрисовка массива в консоле"""
    s = '---' * (len(str(Game.row * Game.column)) * Game.column)
    print(s)
    for elem in Game.place:
        for e in elem:
            print('|', ' ' * (len(str(Game.row * Game.column)) - len(str(e))), e, end=' ')
        print('|')
        print(s)


def read_input_from_player(player_symbol):
    """Считывание и проверка на заполненность указанного места в массиве"""
    max_value = Game.column * Game.row
    while True:
        value = input(f'Куда поставить: {player_symbol}?\n')
        if not value == 'save':
            if value.isdigit() and 1 <= int(value) <= max_value:
                value = int(value)
                y_num, x_num = calc_xy(value)
                if str(Game.place[y_num][x_num]) in Game.InputChar:
                    print('Клетка уже занята')
                    continue
                Game.place[y_num][x_num] = player_symbol
            else:
                print(f'Введите число от 1 до', max_value)
                continue
        return value


def auto_create_input_from_player(player_symbol):
    """Автоматическое создание указанного места и его проверка на заполненность"""
    while True:
        value = random.randint(1, Game.row * Game.column)
        y_num, x_num = calc_xy(value)
        if str(Game.place[y_num][x_num]) in Game.InputChar:
            continue
        Game.place[y_num][x_num] = player_symbol
        return value


def calculate_points(y_num, x_num, y_step, x_step, min_value, max_value):
    """
    Нахождение количества X или O в одну сторону при 0 и в обратную при 1
    Формулами заменил повторяющийся код отличающийся только одним знаком
    y = y_num + num * y_step
    x = x_num + num * x_step
    y = y_num - num * y_step
    x = x_num - num * x_step
    """
    symbol_in_place = Game.place[y_num][x_num]
    symbol_in_place_count = 0
    for num in range(min_value, max_value):
        y = y_num + num * y_step - 2 * num * y_step * min_value
        x = x_num + num * x_step - 2 * num * x_step * min_value
        if y < Game.row and x < Game.column and Game.place[y][x] == symbol_in_place:
            symbol_in_place_count += 1
    return symbol_in_place_count


def calculate_points_in_one_line(y_num, x_num, y_step, x_step):
    """"Нахождение количества X или O в одной линии"""
    symbol_in_place_count = 0
    max_value = min(Game.row, Game.column)
    symbol_in_place_count += calculate_points(y_num, x_num, y_step, x_step, 0, max_value)
    symbol_in_place_count += calculate_points(y_num, x_num, y_step, x_step, 1, max_value)
    return symbol_in_place_count


def calculate_points_in_all_line(value):
    """
    Поиск максимального количесва X или O во всех линиях.
    Вывод победителя
    """
    y_num, x_num = calc_xy(value)
    val_counts = [calculate_points_in_one_line(y_num, x_num, 0, 1),
                  calculate_points_in_one_line(y_num, x_num, 1, 1),
                  calculate_points_in_one_line(y_num, x_num, 1, 0),
                  calculate_points_in_one_line(y_num, x_num, -1, 1)]
    val_count = max(val_counts)
    if val_count >= min(Game.row, Game.column):
        print(f'Winner', Game.place[y_num][x_num])
        return False
    return True


def main():
    """
    Проверка не закончилась ли уже игра.
    Компановка ключевых значений в словарь для возможности соханению.
    Проверка очередности хода.
    Проверка на победу одного из игроков.
    """
    while Game.continue_game:
        draw_place()
        data = {
            'place': Game.place,
            'counter': Game.counter,
            'row': Game.row,
            'column': Game.column,
        }
        if Game.counter % 2 == 0:
            value = read_input_from_player(Game.InputChar.PLAYER)
            if value == 'save':
                save(data)
                Game.continue_game = False
                continue
        else:
            value = auto_create_input_from_player(Game.InputChar.COMPUTER)
        if Game.counter >= min(Game.row, Game.column) * 2 - 2:
            draw_place()
            Game.continue_game = calculate_points_in_all_line(value)
        Game.counter += 1


"""Парсер аргументов из консоли"""
parser = argparse.ArgumentParser(description='Game tic tac toe')
parser.add_argument('-n', action='store', dest='n', help='Row value')
parser.add_argument('-k', action='store', dest='k', help='Column value')
parser.add_argument('-l', action='store', dest='l', help='Load save (true/false)')
args = parser.parse_args()

create_key_data(args.l)  # Заполнение ключевых данных класса
if not Game.error:
    main()
