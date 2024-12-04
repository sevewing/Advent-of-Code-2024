def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    data2d = []
    for i in range(len(lines)):
        ls = list(lines[i])
        els = []
        for j in range(len(ls)):
            if ls[j] != "\n":
                els.append(ls[j])
        data2d.append(els)
    return data2d


def solution(data):
    times = 0
    test = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                try:
                    s = ''.join(data[i][j:j+4])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join(data[i][j-3:j+1])
                    if s == "SAMX":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i+n][j] for n in range(4)])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i-n][j] for n in range(4) if i-n>=0])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i-n][j-n] for n in range(4) if (i-n>=0 and j-n>=0)])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i-n][j+n] for n in range(4) if i-n>=0])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i+n][j+n] for n in range(4)])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
                try:
                    s = ''.join([data[i+n][j-n] for n in range(4) if j-n>=0])
                    if s == "XMAS":
                        times += 1
                except:
                    pass
            if times > test:
                print(i,j, times-test)
                test = times
    return times


def main():
    data = load_data("./day4/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()
