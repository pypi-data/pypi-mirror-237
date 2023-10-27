import pytest
from src.char_count_vp.char_counter import count_unique_chars
from unittest.mock import patch, mock_open
import subprocess


# Testing typical cases
def test_count_unique_chars():
    cases = ["abbbccdf", "abcabcabc", "aabbcc", "abcdefg"]
    results = [3, 0, 0, 7]  # Correct results of count_unique_chars
    for case, result in zip(cases, results):
        actual_result = count_unique_chars(case)
        assert (
            actual_result == result
        ), f"Test failed: Need {actual_result}, got {result}"


atypical_cases = (
    (123, "<class> 'int'"),
    (None, "class <'NoneType'>"),
    (False, "class <'bool'>"),
)


# Testing atypical cases
@pytest.mark.parametrize("arg", atypical_cases)
def test_input_type(arg):
    with pytest.raises(TypeError) as exc_info:
        count_unique_chars(arg=None)
        assert str(exc_info.value) == f"Input must be string, not {type(arg)}'"


# Testing work of cache
def test_count_unique_chars_cache():
    # Clear the cache at the beginning of the test
    count_unique_chars.cache_clear()

    # Before first call, checking if cache is clear
    assert (0, 0, 128, 0) == count_unique_chars.cache_info(), "Cache not clear"

    test_cases = ("abc", "abc", "cba")
    cache_cases = [(0, 1, 128, 1), (1, 1, 128, 1), (1, 2, 128, 2)]

    for cache_case, test_case in zip(cache_cases, test_cases):
        count_unique_chars(test_case)
        cache_data = count_unique_chars.cache_info()
        cache_error = f"Cache info {cache_data} does not match {cache_case}"
        assert cache_case == cache_data, cache_error


# Cache reset
def setup_function(function):
    count_unique_chars.cache_clear()


# Testing CLI
def test_parse_args(capfd):
    # Define the command-line arguments
    args_list = [
        ["python3", "../command_line.py", "--string", "d"],
        ["python3", "../command_line.py", "--file", "../src/char_count_vp/x.txt"],
        [
            "python3",
            "../command_line.py",
            "--string",
            "ab",
            "--file",
            "../src/char_count_vp/x.txt",
        ],
        [
            "python3",
            "../command_line.py",
            "--file",
            "../src/char_count_vp/x.txt",
            "--string",
            "ab",
        ],
    ]

    for args in args_list:
        # Execute the command-line arguments
        subprocess.run(args)
        out, err = capfd.readouterr()
        if "--string" in args and "--file" in args:
            # Both --string and --file provided, prioritize --file
            with open(args[args.index("--file") + 1], "r") as file:
                data = file.read().replace("\n", "")
            output = f"Unique chars count: {count_unique_chars(data)}"
        elif "--string" in args:
            output = f"Unique chars count: {count_unique_chars(args[args.index('--string') + 1])}"
        elif "--file" in args:
            with open(args[args.index("--file") + 1], "r") as file:
                data = file.read().replace("\n", "")
            output = f"Unique chars count: {count_unique_chars(data)}"
            assert output == out.strip()


# Mock-file test
@patch("builtins.open", new_callable=mock_open, read_data="abcd.")
def test_mock_file_count(mock_file, file_path="dummy.txt"):
    with open(file_path, "r") as file:
        content = file.read()
        count_unique_chars(content)


if __name__ == "__main__":
    test_count_unique_chars()
    test_input_type(arg=None)
    test_parse_args
    test_mock_file_count
    pytest.main(["-v"])  # Run pytest with verbose output
