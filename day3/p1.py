import re

def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def solution(data):
    summ = 0
    for i in data:
        ls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",i)
        for a,b in ls:
            summ += int(a)*int(b)
    return summ


def main():
    data = load_data("./day3/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()