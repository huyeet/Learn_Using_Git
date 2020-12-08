import regex
import sys
file_path = "day_five_input.txt"

sys.setrecursionlimit(10**6)


def receive_batch():
    with open(file_path) as f:
        all_seats = f.read().splitlines()
    return all_seats


def process_seats(seats: list):
    seats_id = []
    for seat in seats:
        info = regex.match(r"(\w{7})(\w{3})", seat)
        row = find_rowcol_seats(info.group(1), 127)
        col = find_rowcol_seats(info.group(2), 7)
        seat_id = row * 8 + col
        seats_id.append(seat_id)
    return seats_id


def find_rowcol_seats(row_or_col: str, max_row_col: int):
    row_col_min = 0
    row_col_max = max_row_col
    lower_half = ["F", "L"]
    upper_half = ["B", "R"]
    for i in row_or_col:
        if i in lower_half:
            row_col_max = (row_col_max + row_col_min) // 2
        elif i in upper_half:
            row_col_min = (row_col_max + row_col_min) // 2 + 1
    return row_col_min


def quick_sort(seats_ID: list):
    # Second reimplementation of quicksort. Has to look up past implementation tho.
    if len(seats_ID) <= 1:
        return seats_ID
    pivot = seats_ID[len(seats_ID) // 2]
    left = [seat for seat in seats_ID if seat < pivot]
    middle = [seat for seat in seats_ID if seat == pivot]
    right = [seat for seat in seats_ID if seat > pivot]
    return quick_sort(left) + middle + quick_sort(right)


seats = receive_batch()
wow = process_seats(seats)
sorted_id = set(quick_sort(wow))

# Slightly more improved ver using set
all = set(range(min(sorted_id), max(sorted_id)+1))
only = all - sorted_id

# Set is fooking awesome!
print(only)

# My solution
# for i in range(len(sorted_id) - 1):
    # if sorted_id[i+1] - sorted_id[i] > 1:
        # print(f"({sorted_id[i+1]} + {sorted_id[i]}) / 2 = {(sorted_id[i+1] + sorted_id[i]) / 2}")
        # break

