import re

def load_data(path):
    with open(path, "r") as file:
        lines = file.read()
    return lines


def solution(data):
    summ = 0
    iss = data.split("do()")
    isss = [j.split("don't()")[0] for j in iss]
    for k in isss:
        ls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",k)
        for a,b in ls:
            summ += int(a)*int(b)
    return summ


def main():
    data = load_data("./day3/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()




# import re

# with open('./day3/input.txt') as file:
#     text = file.read()

# lines_to_parse = []

# to_check = text.split("do()")
# for item in to_check:
#     lines_to_parse.append(item.split("don't()")[0])


# total = 0
# for line in lines_to_parse:
#     matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
#     for match in matches:
#         left, right = match.split(",")
#         left = int(left.split("(")[1])
#         right = int(right.split(")")[0])
#         total += left * right

# print(total)