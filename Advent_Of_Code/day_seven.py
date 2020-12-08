import regex
import time
from pathlib import Path
PATH = Path(__file__).parent / "day_seven_input.txt"
# Try not to use regex this time... Use line.split for dis.
# Also, definitely look up other people's solutions once you've done with this.
# yeah, MAKE SURE THAT YOU READ OTHER PEOPLE'S SOLUTIONS


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_rules = f.read().splitlines()
    return all_rules


def create_bags_dict(all_rules: list):
    bags_par_child = {}
    child_list = []
    par_color = ""
    bags_count = 0
    for rule in all_rules:
        rule = rule.split()
        for word_index in range(len(rule) - 1):
            if regex.match(r"bag.*", rule[word_index + 1]):
                color = f"{rule[word_index - 1]} {rule[word_index]}"
                bags_count += 1
                if bags_count == 1:
                    # Initialize dict keys
                    par_color = color
                    bags_par_child[color] = bags_par_child.get(color, 0)
                else:
                    child_list.append(color)
        bags_par_child[par_color] = child_list
        child_list = []
        bags_count = 0
    return bags_par_child


def num_contain_shiny_gold(bags_dict: dict):
    shiny = 0
    color_parents_to_ignore = []
    for key, value in bags_dict.items():
        if "shiny gold" in value:
            shiny += 1
            color_parents_to_ignore.append(key)
    for color in color_parents_to_ignore:
        del bags_dict[color]
    # Real iteration, blyat
    while len(color_parents_to_ignore) != 0:
        layer_color_shiny = set()
        # Some results repeat itself...
        for key, value in bags_dict.items():
            if key not in color_parents_to_ignore:
                for child_color in color_parents_to_ignore:
                    if child_color in value:
                        shiny += 1
                        layer_color_shiny.add(key)
                        break
        for color in layer_color_shiny:
            del bags_dict[color]
        color_parents_to_ignore = layer_color_shiny
    return shiny


start_time = time.time()
rules = receive_batch(PATH)
bags_bags = create_bags_dict(rules)
print(num_contain_shiny_gold(bags_bags))
print(f"--- {time.time() - start_time} seconds ---")
