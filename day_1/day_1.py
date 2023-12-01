
# Take input and get 2 digit numbers and get sum

path = r'/home/ant/AoC_2023/day_1/data.txt'


def take_sum(file) -> int:
    sum = 0
    n1 = None
    n2 = None

    for line in file:
        n1 = None
        n2 = None

        for ch in line:
            if ch.isdigit():

                if n1 is None:  # only changes when its None
                    n1 = int(ch)

                n2 = int(ch)  # Always changes so it takes the last digit

        print(n1, n2, sum)
        sum += int(str(n1) + str(n2))

    return sum


with open(path, "r", encoding="utf-8") as file:
    total = take_sum(file)

print(total)
