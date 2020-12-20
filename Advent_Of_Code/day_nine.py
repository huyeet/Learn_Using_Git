from pathlib import Path
import time
PATH = Path(__file__).parent / "day_nine_input.txt"


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_numbers = f.read().splitlines()
    return all_numbers


start_time = time.time()
received = receive_batch(PATH)
print(f"--- {time.time() - start_time} seconds ---")