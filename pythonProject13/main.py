print("Игра крестики-нолики")
pl_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plaing_size = 3

def playing_field():
    print("_" * 7 * plaing_size)
    for i in range(plaing_size):
        print((" " * 6 + "|") * 3)
        print("   ", pl_field[i * 3], "|", "  ", pl_field[1 + i * 3], "|", "  ", pl_field[2 +i * 3],"|")
        print(("_" * 6 + "|") * 3)
def step_player(index, char):
    if (index > 9 or index< 1 or pl_field[index - 1] in ("X","0")):
        return False
    pl_field[index - 1] = char
    return True
    pass
def chek_win():
    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
        (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )
    for i in win_combination:
        if (pl_field[i[0]] == pl_field[i[1]] and pl_field[i[1]] == pl_field[i[2]]):
            win = pl_field[i[0]]
    return win
def game():
    current_player = "X"
    step = 1
    while(step < 10) and (chek_win() == False):
        index = int(input("Ходит игрок" + current_player + "Для выхода из игры введите 0. Для хода в игре введие номер поля:"))
        if(index == "0"):
            break
        if (step_player(index, current_player)):
            print("Ход сделан. Теперь ходит следующий игрок")
            if(current_player == "X"):
                current_player = "0"
            else:
                current_player = "X"
            playing_field()
            step += 1
        else:
            print("Такой ход сделать нельзя. Введите номер поля заново")

        char = pl_field[index - 1]

    if step == 10:
        print("Игра окончена. Ничья.")
    else:
        print("Игра окончена, выиграл " + chek_win())
game()
