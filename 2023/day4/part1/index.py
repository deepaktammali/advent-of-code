# Day 4: Scratchcards
import re


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


if __name__ == "__main__":
    input_data = read_input("./input.txt")

    res = 0

    for scratch_card in input_data:
        _, number_lists = scratch_card.split(":")

        winning_numbers_str, numbers_we_have_str = number_lists.split("|")
        winning_numbers_str = winning_numbers_str.strip()
        numbers_we_have_str = numbers_we_have_str.strip()

        winning_numbers_set = set(re.findall(pattern="\d+", string=winning_numbers_str))
        numbers_we_have = re.findall(pattern="\d+", string=numbers_we_have_str)

        card_points = 0
        for num in numbers_we_have:
            if num in winning_numbers_set:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points * 2

        res += card_points

    print(f"The result is {res}")
