from pathlib import Path
PATH = Path(__file__).parent / "day_six_input.txt"
# def gonna look into other people's solutions after I'm done with this.
# Using a set is alright, but I want to look at solutions that do not use that.
# Wow the code is atrocious. Why do I even think of using recursion?


def receive_batch(file_path: Path):
    with file_path.open() as f:
        all_questions = f.read().splitlines()
    return all_questions


def count_yes_shared(answered: list):
    num_questions = 0
    main_list = []
    for i in range(len(answered)):
        line = answered[i]
        if line.strip() != "":
            main_list.append(list(line))
        if line.strip() == "" or i == len(answered) - 1:
            if len(main_list) == 1:
                num_questions += len(main_list[0])
            else:
                for letter in main_list[0]:
                    result = intersect_pancake(letter, main_list[1], index=1, main_list=main_list)
                    if result == 1:
                        num_questions += 1
            main_list.clear()
    return num_questions


def intersect_pancake(letter: str, list_answers: list, index: int, main_list: list):
    if letter in list_answers:
        if index < len(main_list) - 1:
            return intersect_pancake(letter, main_list[index + 1], index + 1, main_list)
        elif index == len(main_list) - 1:
            return 1
    elif letter not in list_answers:
        return


questions = receive_batch(PATH)
print(count_yes_shared(questions))
