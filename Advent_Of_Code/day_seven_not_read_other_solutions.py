import regex
import time
from pathlib import Path
PATH = Path(__file__).parent / "day_seven_input.txt"
# Try not to use regex this time... Use line.split for dis.
# Also, definitely look up other people's solutions once you've done with this.
# yeah, MAKE SURE THAT YOU READ OTHER PEOPLE'S SOLUTIONS
# I need to learn how to make a weighted graph.
# Second half failed. I need to practice recursion as well as learn how to create and traverse through
# a weighted graph... 


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_rules = f.read().splitlines()
    return all_rules


def create_bags_dict(all_rules: list):
    bags_par_child = {}
    child_list = []
    color_with_numbers = []
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
                    if rule[word_index - 2].isnumeric():
                        number = int(rule[word_index - 2])
                    else:
                        number = rule[word_index - 2]
                    color_with_numbers.append(number)
                    child_list.append(color)
        bags_par_child[par_color] = [child_list, color_with_numbers]
        child_list = []
        color_with_numbers = []
        bags_count = 0
    return bags_par_child


def num_contain_shiny_gold(bags_dict: dict):
    shiny = 0
    color_parents_to_ignore = []
    for key, value in bags_dict.items():
        if "shiny gold" in value[0]:
            shiny += 1
            color_parents_to_ignore.append(key)
    for color in color_parents_to_ignore:
        del bags_dict[color]
    # Real iteration, blyat
    while len(color_parents_to_ignore) != 0:
        layer_color_shiny = set()
        for key, value in bags_dict.items():
            if key not in color_parents_to_ignore:
                for child_color in color_parents_to_ignore:
                    if child_color in value[0]:
                        shiny += 1
                        layer_color_shiny.add(key)
                        break
        for color in layer_color_shiny:
            del bags_dict[color]
        color_parents_to_ignore = layer_color_shiny
    return shiny


def shiny_total(all_bags: dict, color_name: str):
    total_bags_inside = 0
    bag_contain = all_bags.get(color_name, "nope")
    path = f"{color_name}"
    for i in range(len(bag_contain[0])):
        value = bag_contain[1][i]
        child_color = bag_contain[0][i]
        count = traverse_through_colors(color_value=value, main_bags=all_bags, color_name=child_color,
                                       path=path)
        path = f"{color_name}"
    return total_bags_inside


def traverse_through_colors(color_value, main_bags: dict, color_name: str, path: str):
    if type(color_value) != int:
        print(path)
        return path
    elif type(color_value) == int:
        bags_inside = main_bags.get(color_name, "nope")
        color_children = bags_inside[0]
        value_list = bags_inside[1]
        path += f" > {color_value} {color_name}"
        for i in range(len(color_children)):
            traverse_through_colors(value_list[i], main_bags, color_children[i], path)


# Below are another solutions. Make sure you understand it.
def count_inner_bags(bags_rules: dict):
    # Solutions from other people... I'm dumb.
    # They make it so elegant.
    def wat(current_bag):
        return sum(int(count) + int(count) * wat(bag) for count, bag in bags_rules[current_bag])
    return wat("shiny gold")


def read_input(filename: Path):
    with filename.open() as file:
        bag_rules = {}
        for line in file:
            outer_bag, inner_bags = line.split(" bags contain")
            bag_rules[outer_bag] = regex.findall(r'([0-9]+) ([a-z ]+) bag[s]?', inner_bags.strip())
    return bag_rules


start_time = time.time()
rules = receive_batch(PATH)
bags_bags = create_bags_dict(rules)
print(num_contain_shiny_gold(bags_bags))
print(shiny_total(all_bags=bags_bags, color_name="shiny gold"))
wat = read_input(PATH)
print(count_inner_bags(wat))
print(f"--- {time.time() - start_time} seconds ---")
