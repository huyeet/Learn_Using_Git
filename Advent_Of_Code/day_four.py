import regex

file_path = "day_four_input.txt"


def receive_batch():
    with open(file_path) as f:
        all_passports = f.read().splitlines()
    return all_passports


def process_passports(all_passports: list):
    num_valid = 0
    passport = ""
    for i in range(len(all_passports)):
        line_passport = all_passports[i].lower()
        if line_passport != "":
            passport += f" {line_passport}"
        elif line_passport == "":
            num_fields_passport = check_validity(passport)
            if num_fields_passport == 7:
                num_valid += 1
            passport = ""
    return num_valid


def check_validity(line: str):
    num_valid_fields = 0
    BIRTH_YEAR = r"byr:(\d+)"
    ISSUE_YEAR = r"iyr:(\d+)"
    EXPIR_YEAR = r"eyr:(\d+)"
    HEIGHT = r"hgt:(\d+)(\w+)"
    HAIR_C = r"hcl:#[0-9a-f]{6}"
    EYES_C = r"ecl:(\w+)"
    valid_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = r"pid:[0-9]{9}"
    if check := regex.search(BIRTH_YEAR, line):
        year = check.group(1)
        if 1920 <= int(year) <= 2002:
            num_valid_fields += 1
    if check := regex.search(ISSUE_YEAR, line):
        year = check.group(1)
        if 2010 <= int(year) <= 2020:
            num_valid_fields += 1
    if check := regex.search(EXPIR_YEAR, line):
        year = check.group(1)
        if 2020 <= int(year) <= 2030:
            num_valid_fields += 1
    if check := regex.search(HEIGHT, line):
        value = int(check.group(1))
        if check.group(2) == "cm":
            if 150 <= value <= 193:
                num_valid_fields += 1
        elif check.group(2) == "in":
            if 59 <= value <= 76:
                num_valid_fields += 1
    if regex.search(HAIR_C, line):
        num_valid_fields += 1
    if match := regex.search(EYES_C, line):
        if match.group(1) in valid_eye_color:
            num_valid_fields += 1
    if regex.search(pid, line):
        num_valid_fields += 1
    return num_valid_fields


passports = receive_batch()
print(process_passports(passports))
