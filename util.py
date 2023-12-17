def insert_at_index(string: str, index: int, insert: str) -> str:
    if not (0 <= index < len(string) - 1):
        raise IndexError()

    # https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
    return string[:index] + insert + string[index + 1:]


class str_logic:
    def __init__(self, _columns: int):
        self.columns = _columns

    def draw_line(self, position: int) -> str:
        """
        :param position: The location of the snowflake.
        :return: A string that has a snowflake at the given position.
        """

        # First, we create the template string.
        # In Python, we can use this special syntax to repeat the " " character for x amount of times.
        # x being the `columns` variable.
        return insert_at_index(" " * self.columns, position, "*")

    def draw_line_multi(self, positions: list[int]) -> str:
        s = " " * self.columns
        for m in positions:
            s = insert_at_index(s, m, "*")
        return s
