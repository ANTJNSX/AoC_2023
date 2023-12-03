import os
import re

path = os.getcwd() + r'/day_1/data.txt'


# START PART 1
def part_1(file) -> int:
    sum = 0
    n1 = None
    n2 = None

    # loop over the line and grab the first and last digit
    for line in file:
        n1 = None
        n2 = None

        for ch in line:
            if ch.isdigit():  # number check

                if n1 is None:  # only changes when its None
                    n1 = int(ch)

                n2 = int(ch)  # Always changes so it takes the last digit

        # print(n1, n2, str(n1)+str(n2), sum)
        sum += int(str(n1) + str(n2))  # add the final integer

    return sum


# Running part 1 results
with open(path, "r", encoding="utf-8") as file:  # open data file
    total = part_1(file)

print("Results of part 1:", total)


# START PART 2
# Solution makes sense and returns correct additions for each line,
# very unsure why it is not working...
regx = r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"


def find_num(nm):
    match nm:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"

        case _:  # default case
            return str(nm)


def part_2(file):
    sum = 0
    number_words = []

    for line in file:
        number_words = re.findall(regx, line)

        n1 = find_num(number_words[0])
        n2 = find_num(number_words[-1])

        sum += int(n1 + n2)

        # print(n1, n2, n1+n2, sum)
        # print(number_words, sum, '\n')

    return sum


# Running part 2 results
with open(path, "r", encoding="utf-8") as file:  # open data file
    total = part_2(file)

print("Results of part 2:", total)
