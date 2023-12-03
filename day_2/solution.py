import os


def part_1(file):
    for line in file:
        line = str(line)
        line = line.replace("Game ", "")

        res = line.split(":")  # result with game number in the beginning

        print(res)

    return 0


limit = {"red": 12, "green": 13, "blue": 14}
path = os.getcwd() + r"/day_2/data.txt"

with open(path, "r", encoding="utf-8") as file:
    part_1(file)
