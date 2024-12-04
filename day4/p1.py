def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]


def solution(data):
    times = 0

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1)
    ]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                for dr, dc in directions:
                    try:
                        s = ''.join(data[i + n * dr][j + n * dc] for n in range(4)
                                    if ((i + n * dr) >= 0 and (j + n * dc) >= 0))
                        if s == "XMAS":
                            times += 1
                    except IndexError:
                        continue

    return times


def main():
    data = load_data("./day4/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()
