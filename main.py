import os
from random import randint
from time import sleep


def new_row(size: int, position: int) -> str:
    """
    :param size: How long the string will be.
    :param position: The location of the snowflake.
    :return: A string that has a snowflake at the given position.
    """

    # First, we create the template string.
    # In Python, we can use this special syntax to repeat the " " character for x amount of times.
    # x being the `size` variable.
    template = " " * size

    # TODO: Explain Python index syntax
    # https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
    template = template[:position] + "*" + template[position + 1:]

    return template


# Because we generate a row, we need to know where the position of the snowflake is.
# This is why we return both the string and position of the snowflake. Example code:
#
#   row_str, position = generate_new_row(10)
#
#   row_data = generate_new_row(10)
#   row_data[0] # the string
#   row_data[1] # the position (integer)
#
def generate_new_row(size: int) -> (str, int):
    """
    Generates a string with a snowflake in a random position.
    :param size: How long the string will be.
    :return: A tuple, first element is the string with the snowflake inside.
    The second element is the position of the snowflake.
    """

    # Now, we generate a random value from 0 to `size` and we use this position to modify the specific character
    # within the template string.
    position = randint(0, size - 1)
    # We remove 1 from the size because we will be using this position to index the string, and we must account for
    # zero-based indexing.

    # Zero-based indexing is the idea that counting starts at 0, so, for a given list, the first element will be
    # addressed as list[0], for the second element, list[1]; for the nth position of the list, list[n - 1].
    # Read why we chose this convention: https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html

    return new_row(size, position), position


if __name__ == '__main__':

    # TODO: Implement screen refresh mechanic with a finite state machine, account for FPS + screen size.
    # Do this AFTER we implement the basic snow program.
    snowflake_queue: list[int] = []

    columns = 20
    lines = 50

    while True:  # Program loop on each frame

        # 1. If the queue has reached its full length
        #   a. remove the last row
        #   b. and push everything down by 1.
        # 2. Generate a new row and append that to the queue.
        # 3. Draw each line from the snowflake queue.

        # Hint: Google is your friend, do research as needed!


        # Post-draw operations, these come after drawing the screen
        sleep(0.2)  # Frame limiter
        os.system('clear')  # Clear terminal screen
