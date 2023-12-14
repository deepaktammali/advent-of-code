# Day 2: Cube Conundrum
import re

red_cubes_in_bag = 12
green_cubes_in_bag = 13
blue_cubes_in_bag = 14


def read_input(path: str):
    input_data = []
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")
    return input_data


if __name__ == "__main__":
    input_games = read_input("./input.txt")
    res = 0

    for input_game in input_games:
        # This will split Game 1 and 16 red, 10 green; 12 red, 6 blue;
        part0, part1 = input_game.split(":")
        game_id = part0.split(" ")[1]
        picks = part1.split(";")

        are_valid_picks = True
        for pick in picks:
            red_cubes_match = re.search(r"(\d{1,})\s+red", pick)
            green_cubes_match = re.search(r"(\d{1,})\s+green", pick)
            blue_cubes_match = re.search(r"(\d{1,})\s+blue", pick)

            if red_cubes_match:
                red_cubes_count = int(red_cubes_match.group(1))
                if red_cubes_count > red_cubes_in_bag:
                    are_valid_picks = False
                    break

            if green_cubes_match:
                green_cubes_count = int(green_cubes_match.group(1))
                if green_cubes_count > green_cubes_in_bag:
                    are_valid_picks = False
                    break

            if blue_cubes_match:
                blue_cubes_count = int(blue_cubes_match.group(1))
                if blue_cubes_count > blue_cubes_in_bag:
                    are_valid_picks = False
                    break

        if are_valid_picks:
            res += int(game_id)

    print(f"Result is {res}")
