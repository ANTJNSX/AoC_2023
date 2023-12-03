import os


def part_1(file):  # extract the data into a dict
    for line in file:
        pass

    return 0


splitters = [":", ","]
limit = {"red": 12, "green": 13, "blue": 14}
path = os.getcwd() + r"/day_2/data.txt"

with open(path, "r", encoding="utf-8") as file:
    part_1(file)
