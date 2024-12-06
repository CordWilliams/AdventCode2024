from collections import defaultdict

def read_update(file):
    with open(file, "r") as file:
        updates = list()
        for line in file.readlines():
            updates.append([int(char) for char in line.split(",")])
        return updates

def read_rules(file):
    data = defaultdict(list)
    with open(file, "r") as file:
        for line in file.readlines():
            num1, num2 = line.split("|")
            data[int(num1)].append(int(num2))
        return data

def is_valid_update(update, rules):
    page_to_index = {update[i]: i for i in range(len(update))}

    for i, page in enumerate(update):
        next_page_by_rule = rules.get(page, -1)
        next_page_by_rules = [page_to_index.get(page, -1) for page in next_page_by_rule]
        for index in next_page_by_rules:
            if index != -1 and i > index:
                return False

    return True

def compute_sum(updates, rules):
    mid_sum = 0
    for update in updates:
        if is_valid_update(update, rules):
            n = len(update)
            mid = n // 2 - 1 if n % 2 == 0 else n // 2
            mid_sum += update[mid]

    return mid_sum


def is_invalid_update(update, rules):
    page_to_index = {update[i]: i for i in range(len(update))}

    for i, page in enumerate(update):
        next_page_by_rule = rules.get(page, -1)
        next_page_by_rules = [page_to_index.get(page, -1) for page in next_page_by_rule]
        for index in next_page_by_rules:
            if index != -1 and i > index:
                return True

    return False

def correct_update(update, rules):
    while is_invalid_update(update, rules):
        page_to_index = {update[i]: i for i in range(len(update))}
        for i, curr_page in enumerate(update):
            pages_that_current_page_should_come_before = rules.get(curr_page, -1)
            next_page_by_rules = [page_to_index.get(page, -1) for page in pages_that_current_page_should_come_before]
            for index in sorted(next_page_by_rules):
                if index != -1 and i > index:
                    temp = update[index]
                    update[index] = update[i]
                    update[i] = temp

    return update

def compute_sum_after_updates_corrected(updates, rules):
    mid_sum = 0
    for update in updates:
        if is_invalid_update(update, rules):
            update = correct_update(update, rules)
            n = len(update)
            mid = n // 2 - 1 if n % 2 == 0 else n // 2
            mid_sum += update[mid]

    return mid_sum

example_updates_file = "example_updates.txt"
example_rules_file = "example_rules.txt"
updates_file = "updates.txt"
rules_file = "ordering_rules.txt"

page_updates = read_update(updates_file)
page_rules = read_rules(rules_file)

print(compute_sum(updates=page_updates, rules=page_rules))
print(compute_sum_after_updates_corrected(updates=page_updates, rules=page_rules))