def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def solution(data):
    data2d = [d.split() for d in data]
    l1 = [int(d[0]) for d in data2d]
    l2 = [int(d[1]) for d in data2d]
    sumsum = 0
    for i in l1:
        ps = [j for j, x in enumerate(l2) if x == i]
        sumsum += i * len(ps)

    return sumsum
        

def main():
    data = load_data("./day1/input.txt")
    result = solution(data)
    print(result)

if __name__ == '__main__':
    main()