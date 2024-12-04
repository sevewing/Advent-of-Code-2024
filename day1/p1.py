def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def sort_list(l):
    l_r = [l.pop(l.index(min(l))) for _ in range(len(l))]
    return l_r

def solution(data):
    data2d = [d.split() for d in data]
    l1 = [int(d[0]) for d in data2d]
    l2 = [int(d[1]) for d in data2d]
    l1 = sort_list(l1)
    l2 = sort_list(l2)
    dis = [abs(x-y) for x,y in zip(l1, l2)]
    return sum(dis)
        

def main():
    data = load_data("./day1/input.txt")
    result = solution(data)
    print(result)

if __name__ == '__main__':
    main()