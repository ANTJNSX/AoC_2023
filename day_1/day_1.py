import os

path = os.getcwd() + r'/day_1/data.txt'


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


with open(path, "r", encoding="utf-8") as file:  # open data file
    total = part_1(file)

print(total)


