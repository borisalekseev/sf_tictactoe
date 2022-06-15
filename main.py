import re
import random

x_mark, o_mark = re.compile(r'[xхXХ]'), re.compile(r'[oOоО0]')
empty_field, zero_field, cross_field = '•', 'O', 'X'
play_field = list()
win_combos = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
              [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]


def start():
    global play_field
    play_field = [[empty_field for i in range(3)] for j in range(3)]

    while True:
        choose_side = input('Введи Х или О: ')
        if re.fullmatch(x_mark, choose_side):
            print('Ты играешь за крестики!')
            return 'X'
        elif re.fullmatch(o_mark, choose_side):
            print('Ты играешь за нолики!')
            return 'O'
        else:
            print('Ты ввёл недопустимый символ!')


def display():
    global play_field
    output, count = '', 0
    for line in play_field:
        output += ('|'.join(line) + '\n')
        count += 1
    print(output)


def player_turn(side):
    coords = (int(input('Введи координату по горизонтали: ')),
              int(input('Введи координату по вертикали: ')))
    while True:
        try:
            if play_field[coords[0] - 1][coords[1] - 1] == empty_field:
                play_field[coords[0] - 1][coords[1] - 1] = side
                return True
            print('\nЗдесь рисовать нельзя!\n')
        except IndexError:
            print('\nУкажи координаты от 1 до 3 по каждой оси!\n')


def computer_turn(comp_side):
    while True:
        coords = random.randint(0, 2), random.randint(0, 2)
        if play_field[coords[0]][coords[1]] == empty_field:
            play_field[coords[0]][coords[1]] = comp_side
            return True


def check():
    global play_field
    for combo in win_combos:
        if play_field[combo[0][0]][combo[0][1]] \
                == play_field[combo[1][0]][combo[1][1]] \
                == play_field[combo[2][0]][combo[2][1]] != empty_field:
            return True
    return False


def main():
    print('Привет!\nДобро пожаловать в крестики-нолики!'
          '\nЧтобы выбрать сторону нажми Х или О\nЧтобы сходить введи координаты\n',
          '(от 1 до 3 по горизонтали и по вертикали)')
    while True:
        side = start()
        count = random.randint(0, 1)
        if side == 'X':
            comp_side = 'O'
        else:
            comp_side = 'X'
        while not check():
            if count % 2:
                player_turn(side)
                display()
                if check():
                    print('\nПоздравляем! Вы выиграли!\n')
                    break
                count += 1
            else:
                computer_turn(comp_side)
                display()
                if check():
                    print('\nВы проиграли(((\n')
                    break
                count += 1
        again = input('Хотите сыграть ещё раз? (Да/Нет)\n\n')
        if re.fullmatch(r'да', again, re.IGNORECASE):
            continue
        print('Спасибо за игру!)')
        break


if __name__ == '__main__':
    main()
