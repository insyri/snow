import os
import sys
from time import sleep
from random import randint

from util import str_logic

if __name__ == '__main__':
    snowflake_data: list[(int, int)] = []

    columns = 20
    rows = 10

    # terminal size argument logic
    # python main.py x y
    if len(sys.argv) == 3:
        if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
            columns = int(sys.argv[1])
            rows = int(sys.argv[2])
        else:
            print("Values are not numeric, please input positive integers.")
            exit(1)
    elif len(sys.argv) == 2:
        print("You must use both input arguments if you choose to input dimensions.")
        exit(1)
    else:
        try:
            columns, rows = os.get_terminal_size()
        except OSError:
            pass

    SL = str_logic(columns)

    # sorts snowflake positions. len(index) = y; each row is a list of x values held at index[y].
    # (x, y) -> (index[y][n], y), where n >= 0 and represents an iteration of the snowflakes at that row.
    # len(index[y]) is the amount of snowflakes present at yth row.
    index: list[list[int]] = [[] for _ in range(rows)]
    # note: `[[]] * rows` does address copies, so doing `[id(n) for n in index]`, all values would return the same
    # address. so stupid.

    os.system('clear')
    while True:  # Program loop on each frame

        for _ in range(randint(0, int(columns / 4))):  # How many snowflakes should spawn
            snowflake_data.append((randint(0, columns - 1), rows - 1))  # Position of snowflakes

        # `j` tracks how many removes we've done, so when we add, we'll subtract `i` by `j` to make sure we don't skip
        # values. when we remove an element, the entire list shifts to the left by 1, so we have to back pedal by 1
        # when we move to the next one.
        rm_counter = 0
        for n in range(len(snowflake_data)):
            i = n - rm_counter

            snowflake = snowflake_data[i]
            y = snowflake[1]
            x = snowflake[0]

            if y < 0:
                del snowflake_data[i]
                rm_counter += 1
                continue

            index[y].append(x)
            snowflake_data[i] = (x, y - 1)

        for i in reversed(range(len(index) - 1)):
            if len(index[i]) == 0:
                print()
                continue

            print(SL.draw_line_multi(index[i]))

        # Post-draw operations, these come after drawing the screen

        index = [[] for _ in range(rows)]  # reset index for next frame
        sleep(0.2)  # Frame limiter
        os.system('clear')  # Clear terminal screen
