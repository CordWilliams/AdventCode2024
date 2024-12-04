class HistorianHysteria:

    def computeTotalDistance(self, listA, listB):
        sorted_a = sorted(listA)
        sorted_b = sorted(listB)

        distance = 0
        for i in range(len(sorted_a)):
            num_a = sorted_a[i]
            num_b = sorted_b[i]

            distance += abs(num_a - num_b)

        return distance


list1 = []
list2 = []

with open("input_list.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

hh = HistorianHysteria()
print(hh.computeTotalDistance(list1, list2))