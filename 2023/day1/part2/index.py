# Day 2: Trebuchet?!
import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

num_word_to_int_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


if __name__ == "__main__":
    input_data = read_input("./input.txt")

    pattern = r"^[a-zA-Z]*(?P<first_num>\d)[a-zA-Z\d]*?(?P<last_num>\d)?[a-zA-Z]*$"
    first_num_pattern = (
        rf'[a-zA-Z]*?(?P<first_num>(?:{"|".join(digits)}|\d))[a-zA-Z\d]*'
    )
    last_num_pattern = rf'(?:[a-zA-Z\d]|{"|".join(digits)})*(?P<last_num>(?:{"|".join(digits)}|\d))[a-zA-Z]*'

    res = 0
    for test_str in input_data:
        first_num_match = re.search(pattern=first_num_pattern, string=test_str)
        last_num_match = re.search(pattern=last_num_pattern, string=test_str)

        if first_num_match:
            first_num_str = first_num_match.group("first_num")
            first_num = num_word_to_int_dict[first_num_str]
            second_num_str = last_num_match.group("last_num")
            second_num = (
                num_word_to_int_dict[second_num_str]
                if second_num_str is not None
                else first_num
            )

            num = int(f"{first_num}{second_num}")
            res += num

    print(f"Result is {res}")
