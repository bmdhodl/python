symbols = [' ' for _ in range(9)]
moves = 1
grid_x = ""
grid_y = ""


def main():
    start()
    while True:
        turn()
        winner()
        if moves > 10:
            print('Draw')
            break


# X always goes first
def turn():
    global symbols
    global moves

    if moves % 2 != 0:
        x_move()
    else:
        o_move()
    moves += 1


def winner():
    if any(substring == 'XXX' for substring in [symbols[::4], symbols[1::3], symbols[2::3], symbols[0:3], symbols[3:6],
                                                symbols[6:9], symbols[2:7:2]]):
        print('X wins')
        exit()
    elif any(substring == 'OOO' for substring in
             [symbols[::4], symbols[1::3], symbols[2::3], symbols[0:3], symbols[3:6], symbols[6:9], symbols[2:7:2]]):
        print('O wins')
        exit()
    elif moves == 10:
        print('Draw')
        exit()


def start():
    # you need result because those Winner scenarios are not meant to be on repeat
    print(f"""
---------
| {symbols[0]} {symbols[1]} {symbols[2]} |
| {symbols[3]} {symbols[4]} {symbols[5]} |
| {symbols[6]} {symbols[7]} {symbols[8]} |
---------
    """)


def grid():
    counter = 0  # initialize counter variable
    position = (grid_x - 1) * 3 + grid_y
    row = (position - 1) // 3 + 1
    col = (position - 1) % 3 + 1

    print("---------")
    for row in range(3):
        row_str = "| "
        for col in range(3):
            row_str += symbols[counter] + " "
            counter += 1
        row_str += "|"
        print(row_str)
    print("---------")


def x_move():
    global symbols
    global grid_x
    global grid_y

    while True:
        user_move = input()
        grid_x, grid_y = user_move.split()
        grid_x = int(grid_x)
        grid_y = int(grid_y)

        if 0 < grid_x < 4 and 0 < grid_y < 4:
            position = (grid_x - 1) * 3 + grid_y - 1
            if symbols[position] == ' ':
                symbols_list = list(symbols)
                symbols_list[position] = 'X'
                symbols = ''.join(symbols_list)
                grid()
                break  # exit the while loop since the move is valid
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")


def o_move():
    global symbols
    global grid_x
    global grid_y

    while True:
        user_move = input()
        grid_x, grid_y = user_move.split()
        grid_x = int(grid_x)
        grid_y = int(grid_y)

        if 0 < grid_x < 4 and 0 < grid_y < 4:
            position = (grid_x - 1) * 3 + grid_y - 1
            if symbols[position] == ' ':
                symbols_list = list(symbols)
                symbols_list[position] = 'O'
                symbols = ''.join(symbols_list)
                grid()
                break  # exit the while loop since the move is valid
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")


# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

main()
