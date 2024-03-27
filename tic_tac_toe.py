def check_winner():
    if list_[0][0] == "X" and list_[0][1] == "X" and list_[0][2] == "X":
        return "X"
    if list_[1][0] == "X" and list_[1][1] == "X" and list_[1][2] == "X":
        return "X"
    if list_[2][0] == "X" and list_[2][1] == "X" and list_[2][2] == "X":
        return "X"
    if list_[0][0] == "X" and list_[1][0] == "X" and list_[2][0] == "X":
        return "X"
    if list_[0][1] == "X" and list_[1][1] == "X" and list_[2][1] == "X":
        return "X"
    if list_[0][2] == "X" and list_[1][2] == "X" and list_[2][2] == "X":
        return "X"
    if list_[0][0] == "X" and list_[1][1] == "X" and list_[2][2] == "X":
        return "X"
    if list_[0][2] == "X" and list_[1][1] == "X" and list_[2][0] == "X":
        return "X"
    if list_[0][0] == "0" and list_[0][1] == "0" and list_[0][2] == "0":
        return "0"
    if list_[1][0] == "0" and list_[1][1] == "0" and list_[1][2] == "0":
        return "0"
    if list_[2][0] == "0" and list_[2][1] == "0" and list_[2][2] == "0":
        return "0"
    if list_[0][0] == "0" and list_[1][0] == "0" and list_[2][0] == "0":
        return "0"
    if list_[0][1] == "0" and list_[1][1] == "0" and list_[2][1] == "0":
        return "0"
    if list_[0][2] == "0" and list_[1][2] == "0" and list_[2][2] == "0":
        return "0"
    if list_[0][0] == "0" and list_[1][1] == "0" and list_[2][2] == "0":
        return "0"
    if list_[0][2] == "0" and list_[1][1] == "0" and list_[2][0] == "0":
        return "0"
    return "*"


def tic_tac():
    for i in list_:
        print(*i)
    print()


list_ = [['*', '*', '*'], [], []]
list_[1].extend('*' * 3), list_[2].extend('*' * 3)
print("Добро пожаловать в крестики-нолики! \n""-----------------------------------")
tic_tac()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ход ноликов")
    else:
        turn_char = "X"
        print("Ход крестиков")
    x = int(input("Введите номер строки ")) - 1
    y = int(input("Введите номер столбца ")) - 1
    if list_[x][y] == "*":
        list_[x][y] = turn_char
    else:
        print("Ячейка уже занята. Переход хода")
        tic_tac()
        continue

    tic_tac()
    if check_winner() == "X":
        print("Победа крестиков")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
