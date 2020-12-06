import math
# I have to learn how to intersect two lists

test_set_1 = {"a", "b", "c", "d"}
test_set_2 = {"m", "a", "d", "f"}

test_list_1 = ["a", "b", "c", "d"]
test_list_2 = ["m", "a", "d", "f"]
test_list_3 = ["c", "d", "a", "f"]
test_list_4 = ["a", "z", "x", "y"]
print(test_set_2 - test_set_1)
print(sorted(test_set_2))

print(test_list_1)


def intersect_two(list_one: list, list_two: list, list_three: list):
    for i in list_one:
        if i in list_two:
            if i in list_three:
                print(i)


def intersect_variable(lists_o_answers: list):
    i = 0
    while i < len(lists_o_answers):
        return "bruh"


def intersect_blyat(letter: str, list_answers: list, index: int, main_list: list):
    if len(main_list) > 1:
        if letter in list_answers:
            if index < len(main_list) - 1:
                return intersect_blyat(letter, main_list[index + 1], index + 1, main_list)
            elif index == len(main_list) - 1:
                return 1
        elif letter not in list_answers:
            return
    elif len(main_list) == 1:
        return len(list_answers)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit(
        "intersect_two(['a', 'b', 'c', 'd'],['m', 'a', 'd', 'f'], ['c', 'd', 'a', 'f'])",
        setup="from __main__ import intersect_two", number=1
                       ))

another = [test_list_1]
main_blin = [test_list_1, test_list_2, test_list_3, test_list_4]
for i in test_list_1:
    boom = intersect_blyat(letter=i, list_answers=another[0], index=0, main_list=another)
    print(boom)