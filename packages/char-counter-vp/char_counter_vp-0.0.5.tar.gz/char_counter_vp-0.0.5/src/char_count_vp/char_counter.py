from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=128)
def count_unique_chars(string=None, file_path=None):
    """
    Count the number of unique characters in the input string.

    Parameters:
        string (str): The string in which to count unique characters.
        file_path (str): The path to the input text file.

    Returns:
        int: The count of unique characters in the input string.

    Raises:
        TypeError: If the input is not a string.
    """
    if string is not None:
        counter = Counter(string)
        # Calculate the number of characters occurring only once
        count = sum(map(lambda x: x == 1, counter.values()))
        return count
    elif file_path:
        with open(file_path, "r") as file:
            content = file.read()
        return count_unique_chars(content)
    else:
        raise TypeError(f"String or a file path needed, not '{type(string)}'")
