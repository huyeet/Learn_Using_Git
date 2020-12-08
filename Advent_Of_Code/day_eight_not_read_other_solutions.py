# You will have to look into other people's solutions after you've done with this.
# Try to not spend too much time on this as you have a test tomorrow.
from pathlib import Path
import time
import regex
PATH = Path(__file__).parent / "day_eight_input.txt"
accumulator = 0


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_instructions_console = f.read().splitlines()
    return all_instructions_console


def total_before_inf(accumulator: int, instructions: list):
    PATTERN = r"(acc|jmp|nop) ([+-]\d*)"
    flag_list = [0 for i in range(len(instructions))]
    index = 0
    instructions_index = []
    # Original break condition: flag_list[index] != 2
    while flag_list[index] != 2 and index < len(instructions):
        instruction_match = regex.match(PATTERN, instructions[index])
        type = instruction_match.group(1)
        value = int(instruction_match.group(2))
        if type == "acc":
            accumulator += value
            index += 1
        elif type == "nop":
            index += 1
            instructions_index.append(index)
        elif type == "jmp":
            index += value
            instructions_index.append(index)
        flag_list[index] += 1
    return instructions_index


def change_command(instructions_index: list, all_instructions: list):
    # Brute force try to turn every single jump or noc, if repeat, break.
    # If not, then break once the index reaches the length of the instructions.
    accumulator = 0
    index = 0
    flag_list = [0 for i in range(len(all_instructions))]
    PATTERN = r"(acc|jmp|nop) ([+-]\d*)"

    # Brute force incoming...
    for instruction in instructions_index:
        while index < len(all_instructions):
            instruction_match = regex.match(PATTERN, all_instructions[index])
            type = instruction_match.group(1)
            value = int(instruction_match.group(2))
            if type == "acc":
                accumulator += value
                index += 1
            elif type == "nop":
                if all_instructions[index] == all_instructions[instruction]:
                    print(f"{instruction}: {all_instructions[index]}")
                    index += value
                else:
                    index += 1
            elif type == "jmp":
                if all_instructions[index] != all_instructions[instruction]:
                    index += value
                else:
                    print(f"{instruction}: {all_instructions[index]}")
                    index += 1
            if index < len(all_instructions):
                flag_list[index] += 1
                if flag_list[index] == 2:
                    break
            else:
                break
        if index == len(all_instructions):
            break
        else:
            accumulator = 0
            index = 0
            flag_list = [0 for i in range(len(all_instructions))]
    return accumulator


start_time = time.time()
all_instructions = receive_batch(PATH)
boom = total_before_inf(accumulator, all_instructions)
change_one_command = change_command(instructions_index=boom, all_instructions=all_instructions)
print(change_one_command)
print(f"--- {time.time() - start_time} seconds ---")

