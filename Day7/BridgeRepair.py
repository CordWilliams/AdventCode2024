import sys
sys.set_int_max_str_digits(1000000)

def read(file):
    with open(file, "r") as file:
        input_values = []
        output = []

        for line in file:
            parts = line.split(':')
            test_val = int(parts[0].strip())
            output.append(test_val)
            curr_nums = list(map(int, parts[1].strip().split()))
            input_values.append(curr_nums)
    return input_values, output

def is_target_possible_with_add_mul(curr_nums, target):
    results = {0}

    for num in curr_nums:
        new_results = set()
        for res in results:
            new_results.add(res + num)
            new_results.add(res * num)

        results = new_results

    return target in results

def is_target_possible_with_add_mul_join(curr_nums, target):
    results = {curr_nums[0]}

    for num in curr_nums[1:]:
        new_results = set()
        for res in results:
            new_results.add(res + num)
            new_results.add(res * num)
            new_results.add(int(str(res) + str(num)))

        results = new_results

    return target in results

def find_sum_using_operators(equation_input_values, expected_equation_output_values):
    total_sum_2, total_sum_3 = 0, 0
    for i in range(len(equation_input_values)):
        inputs = equation_input_values[i]
        output = expected_equation_output_values[i]
        if is_target_possible_with_add_mul(inputs, output):
            total_sum_2 += output
        if is_target_possible_with_add_mul_join(inputs, output):
            total_sum_3 += output

    return total_sum_2, total_sum_3

def main():
    example_input_file = "einput.txt"
    input_file = "input.txt"

    equation_input_values, expected_equation_output_values = read(input_file)

    total_sum_2, total_sum_3 = find_sum_using_operators(equation_input_values, expected_equation_output_values)

    print(f"Total Sum using + and * operators: {total_sum_2}")
    print(f"Total Sum using +, *, || operators: {total_sum_3}")


if __name__ == "__main__":
    main()
