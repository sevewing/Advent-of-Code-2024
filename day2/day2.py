import math


def Q1_is_report_safe(report):
    diff = [y-x for x, y in zip(report[:-1], report[1:])]
    is_increasing = all([d >= 1 and d <= 3 for d in diff])
    is_decreasing = all([d >= -3 and d <= -1 for d in diff])
    return is_increasing or is_decreasing


# dis = lambda x,y: x-y
def abs_c(x): return abs(x) > 0 and abs(x) < 4


def bad_point(diffs, diff_id):
    for i in range(len(diffs)):
        if abs(diffs[i]) > 3:
            return i
        if i+1 < len(diffs) and diff_id[i] != diff_id[i+1]:
            return i+1
    return False


def Q2_is_report_safe(report):
    report_cp1 = report.copy()
    report_cp2 = report.copy()
    lens = len(report)
    if lens < 2:
        return False
    if lens == 2 and abs_c(report[0]-report[1]):
        return True

    diffs, diff_id = [], []
    for x, y in zip(report[:-1], report[1:]):
        diffs.append(y-x)
        if y-x > 0:
            diff_id.append(1)
        elif y-x == 0:
            diff_id.append(0)
        else:
            diff_id.append(-1)
    bad_p = bad_point(diffs, diff_id)
    if bad_p:
        report_cp1.pop(bad_p)
        if bad_p+1 < lens:
            report_cp2.pop(bad_p+1)
        return Q1_is_report_safe(report_cp1) or Q1_is_report_safe(report_cp2)
    else:
        return Q1_is_report_safe(report)


def main():
    Q1_safe_reports = 0
    Q2_safe_reports = 0
    with open("./input.txt", "r") as reports:
        for report in reports:
            report = report.split()
            report = [int(level) for level in report]
            if Q1_is_report_safe(report):
                Q1_safe_reports += 1
            if Q2_is_report_safe(report) or Q2_is_report_safe(report[::-1]):
                print(report)
                Q2_safe_reports += 1
    print(f"answer to Q1: {Q1_safe_reports}")
    print(f"answer to Q2: {Q2_safe_reports}")


if __name__ == '__main__':
    main()
