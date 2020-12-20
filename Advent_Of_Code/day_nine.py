from pathlib import Path
import time
PATH = Path(__file__).parent / "day_nine_input.txt"
# Apparently this uses a Knapsack algorithm. I have no idea what it means...
# First try done using BRUTE FORCE!


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_numbers = f.read().splitlines()
        all_numbers = list(map(int, all_numbers))
    return all_numbers


def wrong_number(nums: list):
    index = 0
    # Okay, sort this shit out...
    for i in range(25, len(nums)):
        preamble = sorted(nums[index:i])
        target = nums[i]
        preamble = shorten_list(preamble, target)
        result = find_da_number(preamble, target)
        if result == f"{target} IS INVALID!":
            return target, nums[:i]
        index += 1


def shorten_list(preamble: list, target: int):
    # Find the positions. I can use binary for this...
    for i in range(len(preamble)):
        if preamble[i] > target:
            return preamble[:i]
    return preamble


def find_da_number(preamble: list, target: list):
    # This is such a dumb solution...
    # At least I manage to do it
    index = len(preamble) - 1
    while index > 0:
        for i in range(index):
            if preamble[i] + preamble[index] == target:
                return f"{target} IS VALID!"
        index -= 1
    return f"{target} IS INVALID!"


def contiguous_set(preamble: list, target: int):
    # Let's brute force this.
    for i in range(len(preamble)):
        index = i + 1
        while index < len(preamble):
            test_list = preamble[i:index]
            total = sum(test_list)
            if total == target:
                satisfied_list = test_list
                return satisfied_list
            elif total > target:
                break
            elif total < target:
                index += 1


start_time = time.time()
received = receive_batch(PATH)
#print(received)
false_number = wrong_number(received)
print(false_number[0])

part_2_list = contiguous_set(false_number[1], false_number[0])
part_2_list = sorted(part_2_list)
print(part_2_list[0] + part_2_list[-1])
print(f"--- {time.time() - start_time} seconds ---")