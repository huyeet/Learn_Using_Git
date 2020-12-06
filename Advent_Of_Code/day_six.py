from pathlib import Path
PATH = Path(__file__).parent / "day_six_input.txt"
# def gonna look into other people's solutions after I'm done with this.
# Use a set is alright, but I want to look at solutions that do not use that.


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_questions = f.read().splitlines()
    return all_questions


def count_yes(answered: list):
    num_questions = 0
    set_answered = set()
    for i in range(len(answered)):
        line = answered[i]
        if line.strip() != "":
            print(sorted(line))
            for x in list(line):
                set_answered.add(x)
        if line.strip() == "" or i == len(answered) - 1:
            num_questions += len(set_answered)
            set_answered.clear()
    return num_questions


questions = receive_batch(PATH)
print(count_yes(questions))
