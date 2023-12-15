# Day 3: Gear Ratios
import re
from collections import defaultdict


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


def generate_meta(raw_input_data: [str]):
    special_char_at_pos = dict()
    special_char_exists_dict = dict()
    part_numbers_meta = []

    part_number_pattern = r"\d+"
    special_character_pattern = r"[.]*([!-\/:-@[-`{-~])?[.]*"

    cols = len(raw_input_data[0])

    for row_idx, row_data in enumerate(raw_input_data):
        part_number_matches = re.finditer(pattern=part_number_pattern, string=row_data)
        for match in part_number_matches:
            meta = dict()
            meta["row"] = row_idx
            meta["span"] = match.span(0)
            meta["part_number"] = int(match.group(0))
            part_numbers_meta.append(meta)

        special_char_matches = re.finditer(
            pattern=special_character_pattern, string=row_data
        )
        for match in special_char_matches:
            special_char = match.group(1)
            if special_char:
                col, _ = match.span(1)
                row = row_idx
                idx = row * cols + col
                special_char_exists_dict[idx] = True
                special_char_at_pos[idx] = special_char

    return special_char_exists_dict, special_char_at_pos, part_numbers_meta


if __name__ == "__main__":
    input_data = read_input("./input.txt")
    special_char_exists_dict, special_char_at_pos, part_numbers_meta = generate_meta(
        input_data
    )
    star_char_adj_part_numbers = defaultdict(list)

    rows = len(input_data)
    cols = len(input_data[0])

    res = 0

    for part_number_meta in part_numbers_meta:
        row = part_number_meta["row"]
        col_start = part_number_meta["span"][0]
        col_end = part_number_meta["span"][1] - 1

        left_pos_idx = (row * cols) + col_start - 1 if col_start - 1 >= 0 else None
        right_pos_idx = (row * cols) + col_end + 1 if col_end + 1 <= cols - 1 else None

        top_pos_idexes = []
        bottom_pos_idexes = []

        # col_start - 1 and col_end + 1 + 1 to accomodate the diagnols
        for col in range(col_start - 1, col_end + 2):
            if col >= 0 and col <= cols - 1:
                # not the first row
                if row > 0:
                    top_pos_idx = (row - 1) * cols + col
                    top_pos_idexes.append(top_pos_idx)
                # not the last row
                if row < rows - 1:
                    bottom_pos_idx = (row + 1) * cols + col
                    bottom_pos_idexes.append(bottom_pos_idx)

        pos_indexes = []
        if left_pos_idx:
            pos_indexes.append(left_pos_idx)
        if right_pos_idx:
            pos_indexes.append(right_pos_idx)
        pos_indexes.extend(top_pos_idexes)
        pos_indexes.extend(bottom_pos_idexes)

        for pos_index in pos_indexes:
            if special_char_exists_dict.get(pos_index, False):
                if special_char_at_pos[pos_index] == "*":
                    star_char_adj_part_numbers[pos_index].append(
                        part_number_meta["part_number"]
                    )

    for possible_gear_pos in star_char_adj_part_numbers:
        adj_part_numbers = star_char_adj_part_numbers[possible_gear_pos]
        # len = 2, valid gear
        if len(adj_part_numbers) == 2:
            print(adj_part_numbers)
            gear_ratio = adj_part_numbers[0] * adj_part_numbers[1]
            res += gear_ratio

    print(f"Result is {res}")
