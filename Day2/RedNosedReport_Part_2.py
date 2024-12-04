def readReports():
    data = []

    with open("reports.txt", "r") as file:
        for line in file:
            row = list(map(int, line.split()))
            data.append(row)

    return data

def is_safe_report(report):
    is_increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    is_decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True
    return False

def getNumberOfSafeReports():
    reports = readReports()
    num_safe = sum(1 for report in reports if is_safe_with_dampener(report))
    return num_safe

print(getNumberOfSafeReports())
