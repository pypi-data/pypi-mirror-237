# Character Counter

This Python application allows you to count the number of unique characters in a provided string or a text file.

## Usage

### Running the Application

Navigate to the `src` directory and run the `command_line.py` script with the desired options:

```python -m command_line.py --string "your_string_here"```

or

```python -m command_line.py --file /path/to/your/text_file.txt```

## Function Details

### count_unique_chars(string=None, file_path=None)

Count the number of unique characters in the input string.

#### Parameters:

- `string` (str): The string in which to count unique characters.
- `file_path` (str): The path to the input text file.

#### Returns:

- `int`: The count of unique characters in the input string.

#### Raises:

- `TypeError`: If the input is not a string.

## Author

Volodymyr Perehuda 