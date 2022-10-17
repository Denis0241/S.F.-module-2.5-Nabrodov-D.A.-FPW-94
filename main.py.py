def greet():
    print("--------------------")
    print("  Добро пожаловать  ")
    print("      в игру        ")
    print("  крестики-нолики   ")
    print("--------------------")
    print(" Формат ввода: x y  ")
    print(" x - номер строки   ")
    print(" y - номер столбца  ")


def show_field():
    print()
    print(" x/y| 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(map(str, row))} | "
        print(row_str)
        print("  --------------- ")
    print()


def users_input(f):
    global y, x
    while True:
        place = input("Введите координаты:").split()
        if len(place) != 2:
            print("Введите 2 координаты! ")
            continue

        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите числа!")
            continue

        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Вы вышли из диапазона!")
            continue
        if f[x][y] != " ":
            print("Клетка занята!")
            continue
        break
    return x, y


def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выйграл крестик!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выйграл нолик!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выйграл крестик!")
            return True
        elif symbols == ["0", "0", "0"]:
            print("Выйграл нолик!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        print("Выйграл крестик!")
        return True
    elif symbols == ["0", "0", "0"]:
        print("Выйграл нолик!")
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2 - i])
    if symbols == ["X", "X", "X"]:
        print("Выйграл крестик!")
        return True
    elif symbols == ["0", "0", "0"]:
        print("Выйграл нолик")
        return True

    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = users_input(field)

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        print("Игра окончена!")
        break

    if count == 9:
        print("Ничья!")
        break
