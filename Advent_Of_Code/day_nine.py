from pathlib import Path
import time
import regex
PATH = Path(__file__).parent / "day_nine_input.txt"
accumulator = 0


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_instructions_console = f.read().splitlines()
    return all_instructions_console


start_time = time.time()
received = receive_batch(PATH)
print(f"--- {time.time() - start_time} seconds ---")