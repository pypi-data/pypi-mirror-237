import argparse
from src.char_count_vp.char_counter import count_unique_chars


def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Count unique characters in a string or a file."
    )
    parser.add_argument("--string", type=str, help="Input string")
    parser.add_argument("--file", type=str, help="Input path file")

    args = parser.parse_args()
    # Updating --file parametr prioritization
    if not args.string and not args.file:
        parser.error("Please provide either --string or --file")
    elif args.file:
        args.string = None

    return args


if __name__ == "__main__":
    args = parse_args()
    unique_chars = count_unique_chars(args.string, args.file)
    print(f"Unique chars count: {unique_chars}")
