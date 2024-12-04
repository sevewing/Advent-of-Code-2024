def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return [list(line.strip()) for line in lines]


def solution(data):
    times = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            if data[i][j] == "A":
                s1 = ''.join([data[i+n][j+n] for n in range(-1,2)])
                s2 = ''.join([data[i+n][j-n] for n in range(-1,2)])
                a = ["MAS","SAM","MAS","SAM"]
                b = ["SAM","MAS","MAS","SAM"]
                if (s1,s2) in zip(a,b):
                    times += 1
    return times


def main():
    data = load_data("./day4/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()
