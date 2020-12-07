from pathlib import Path
import time
PATH = Path(__file__).parent / "day_three_input.txt"


def receive_batch(file_path: Path):
    with file_path.open() as f:
        paths = f.read().splitlines()
    return paths


def load_into_go_down_hill(all_paths: list, x_shift: list, y_shift: list):
    multi_trees = 1
    for i in range(len(x_shift)):
        tree_count = go_down_hill(all_paths, x_shift[i], y_shift[i])
        multi_trees *= tree_count
        print(tree_count)
    return multi_trees


def go_down_hill(paths: list, x_shift: int, y_shift: int):
    tree_count = 0
    pos_x = 0
    pos_y = 0
    while pos_y < len(paths):
        path = list(paths[pos_y])
        if pos_x >= len(path):
            pos_x = pos_x - len(path)
        if path[pos_x] == "#":
            tree_count += 1
        pos_x += x_shift
        pos_y += y_shift
    return tree_count


start_time = time.time()
move_right = [1, 3, 5, 7, 1]
move_down = [1, 1, 1, 1, 2]
hills = receive_batch(PATH)
print(load_into_go_down_hill(hills, move_right, move_down))

print(f"--- {time.time() - start_time} seconds ---")
