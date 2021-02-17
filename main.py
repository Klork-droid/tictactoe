import pickle
import argparse
import random


def calc_xy(value):
    """Возвращает позицию введенного элемента в массиве"""
    y_num = int((value - 1) / column)
    x_num = int((value - 1) % column)
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


def create_mass(check_load):
    """Создание нового массива или загрузка массива из файла сохранения"""
    if check_load == 'true':
        data = load()
        place = data.get('place')
        counter = data.get('counter')
        row = data.get('row')
        column = data.get('column')

    else:
        row = int(args.n)
        column = int(args.k)
        place = [[0] * column for i in range(row)]
        for i in range(row):
            for j in range(column):
                place[i][j] = 1 + column * i + j
        counter = 0
    return counter, place, row, column


def draw_place():
    """Отрисовка массива в консоле"""
    s = '---' * (len(str(row * column)) * column)
    print(s)
    for elem in place:
        for e in elem:
            print('|', ' ' * (len(str(row * column)) - len(str(e))), e, end=' ')
        print('|')
        print(s)


def take_input(player_symbol):
    """Считывание и проверка на заполненность указанного места в массиве"""
    while True:
        value = input(f'Куда поставить: {player_symbol}?\n')
        if not value == 'save':
            value = int(value)
            y_num, x_num = calc_xy(value)
            if str(place[y_num][x_num]) in 'XO':
                print('Клетка уже занята')
                continue
            place[y_num][x_num] = player_symbol
        return value


def auto_input(player_symbol):
    """Автоматическое создание указанного места и его проверка на заполненность"""
    while True:
        value = random.randint(1, row * column)
        y_num, x_num = calc_xy(value)
        if str(place[y_num][x_num]) in 'XO':
            continue
        place[y_num][x_num] = player_symbol
        return value


def calc_line(y_num, x_num, y_step, x_step):
    """"Нахождение количества X или O в одной линии"""
    val = place[y_num][x_num]
    val_count = 0
    for num in range(min(row, column)):
        y = y_num + num * y_step
        x = x_num + num * x_step
        if y < row and x < column and place[y][x] == val:
            val_count += 1
        else:
            break
    for num in range(1, min(row, column)):
        y = y_num - num * y_step
        x = x_num - num * x_step
        if y < row and x < column and place[y][x] == val:
            val_count += 1
        else:
            break
    return val_count


def calc_result(value):
    """
    Поиск максимального количесва X или O во всех линиях.
    Вывод победителя
    """
    y_num, x_num = calc_xy(value)
    val_counts = [calc_line(y_num, x_num, 0, 1),
                  calc_line(y_num, x_num, 1, 1),
                  calc_line(y_num, x_num, 1, 0),
                  calc_line(y_num, x_num, -1, 1)]
    val_count = max(val_counts)
    if val_count >= min(row, column):
        if place[y_num][x_num] == 'X':
            print('Winner X')
        else:
            print('Winner O')
        return False
    return True


def main(counter, place):
    """
    Проверка не закончилась ли уже игра.
    Компановка ключевых значений в словарь для возможности соханению.
    Проверка очередности хода.
    Проверка на победу одного из игроков.
    """
    continue_game = True
    while continue_game:
        draw_place()
        data = {
            'place': place,
            'counter': counter,
            'row': row,
            'column': column,
        }
        if counter % 2 == 0:
            value = take_input('X')
            if value == 'save':
                save(data)
                continue_game = False
                continue
        else:
            value = auto_input('O')
        if counter >= min(row, column) * 2 - 2:
            draw_place()
            continue_game = calc_result(value)
        counter += 1


"""Парсер аргументов из консоли"""
parser = argparse.ArgumentParser(description='Game tic tac toe')
parser.add_argument('-n', action='store', dest='n', help='Row value')
parser.add_argument('-k', action='store', dest='k', help='Column value')
parser.add_argument('-l', action='store', dest='l', help='Load save (true/false)')
args = parser.parse_args()

"""Глобальные переменные"""
check_load = args.l
counter, place, row, column = create_mass(check_load)
main(counter, place)
