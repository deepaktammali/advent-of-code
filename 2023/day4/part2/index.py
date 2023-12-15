# Day 4: Scratchcards
import re
from collections import defaultdict


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


if __name__ == "__main__":
    input_data = read_input("./input.txt")

    res = 0

    scratch_cards_meta = dict()
    max_card_number = -1
    scratch_cards_count = defaultdict(int)
    total_cards = len(input_data)

    for scratch_card in input_data:
        scratch_card_meta = {}

        card_title_str, number_lists = scratch_card.split(":")

        card_number_match = re.search(pattern="\d+", string=card_title_str)
        card_number = int(card_number_match.group(0))
        scratch_cards_count[card_number] = 1
        max_card_number = max(max_card_number, card_number)

        winning_numbers_str, numbers_we_have_str = number_lists.split("|")
        winning_numbers_str = winning_numbers_str.strip()
        numbers_we_have_str = numbers_we_have_str.strip()

        winning_numbers_set = set(re.findall(pattern="\d+", string=winning_numbers_str))
        numbers_we_have = re.findall(pattern="\d+", string=numbers_we_have_str)

        matching_numbers = 0
        for num in numbers_we_have:
            if num in winning_numbers_set:
                matching_numbers += 1

        scratch_card_meta["matching_numbers"] = matching_numbers
        scratch_cards_meta[card_number] = scratch_card_meta

    for curr_card_number in range(1, max_card_number + 1):
        meta = scratch_cards_meta[curr_card_number]
        matching_numbers = meta["matching_numbers"]
        if matching_numbers > 0:
            for i in range(1, matching_numbers + 1):
                # add count of next cards as we get their copies
                scratch_cards_count[curr_card_number + i] += scratch_cards_count[
                    curr_card_number
                ]
                total_cards += scratch_cards_count[curr_card_number]

    print(f"The result is {total_cards}")
