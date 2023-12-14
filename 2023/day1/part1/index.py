# Day 1: Trebuchet?!
import re


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


if __name__ == "__main__":
    input_data = read_input("./input.txt")

    pattern = r"^[a-zA-Z]*(?P<first_num>\d)[a-zA-Z\d]*?(?P<last_num>\d)?[a-zA-Z]*$"

    res = 0
    for test in input_data:
        match = re.search(pattern=pattern, string=test)

        if match:
            first_num = match.group("first_num")
            second_num = match.group("last_num")
            second_num = second_num if second_num else first_num

            num = int(f"{first_num}{second_num}")
            res += num

    print(f"Result is {res}")
