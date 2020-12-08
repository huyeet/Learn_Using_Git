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
    while flag_list[index] != 2:
        instruction_match = regex.match(PATTERN, instructions[index])
        type = instruction_match.group(1)
        value = int(instruction_match.group(2))
        if type == "acc":
            accumulator += value
            index += 1
        elif type == "nop":
            index += 1
        elif type == "jmp":
            index += value
        flag_list[index] += 1
        print(accumulator)
    return accumulator


start_time = time.time()
all_instructions = receive_batch(PATH)
boom = total_before_inf(accumulator, all_instructions)
print(boom)
print(f"--- {time.time() - start_time} seconds ---")

