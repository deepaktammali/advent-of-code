# day 21 : Step Counter
from collections import defaultdict


def read_input(file_name):
    input_data = []
    with open(file_name, "r", encoding="utf-8") as f:
        file_data = f.read()
        input_data = file_data.split("\n")

    return input_data


# g -> garden, r -> rock and u -> unknown
def get_metadata(input_data):
    rows = len(input_data)
    cols = len(input_data[0])

    map = [["u" for _ in range(cols)] for _ in range(rows)]
    start_pos = []

    for r, row in enumerate(input_data):
        for c, item in enumerate(row):
            map[r][c] = "g" if item == "." or item == "S" else "r"
            if item == "S":
                start_pos = [r, c]

    return map, start_pos, rows, cols


n_pos_diff = [[-1, 0], [1, 0], [0, 1], [0, -1]]

if __name__ == "__main__":
    possible_steps = 64
    input_data = read_input("./input.txt")
    garden_map, start_pos, rows, cols = get_metadata(input_data)

    steps_taken = 0
    curr_positions = [start_pos]

    while steps_taken < possible_steps:
        visited = defaultdict(bool)
        new_curr_positions = []

        for pos in curr_positions:
            r, c = pos
            for pos_diff in n_pos_diff:
                r_diff, c_diff = pos_diff
                n_r = (r_diff + r) % rows
                n_c = (c_diff + c) % cols
                n_pos = [n_r, n_c]

                index_pos = n_r * cols + n_c
                is_already_visited = visited[index_pos]

                # explore only if the neighbor is a garden
                if garden_map[n_pos[0]][n_pos[1]] == "g" and not is_already_visited:
                    visited[index_pos] = True
                    new_curr_positions.append(n_pos)

        curr_positions = new_curr_positions

        steps_taken += 1

    print(f"Result is {len(curr_positions)}")
