import re
import random

def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def check(line, rule):
    pn = line.pop(0)
    if len(line) == 0:
        return True
    try:
        for v in rule[pn]:
            if v == line[0]:
                return check(line, rule)
    except:
        pass
    return False

    
def get_issue(line, rule):
    ls = len(line)
    for i in range(ls):
        for j in range(i+1, ls):
            if line[j] in list(rule.keys()) and line[i] in rule[line[j]]:
                return [i, j]
    return
   

def solution(data):
    rule = {}
    mids = []
    
    for i in data:
        if i == "":
            continue
        try:
            k,v = i.split("|")
            if rule.get(k) == None:
                rule.update({k:{v}})
            else:
               rule.get(k).add(v)
        except:
            line = i.split(",")
            ck = check(line.copy(), rule)
            if ck:
                continue
            while not ck:
                p1, p2 = get_issue(line, rule)
                line[p1], line[p2] = line[p2], line[p1]
                ck = check(line.copy(), rule)
            mids.append(int(line[int(len(line)/2)]))
    
    return sum(mids)


def main():
    data = load_data("./day5/input.txt")
    result = solution(data)
    print(result)


if __name__ == '__main__':
    main()
