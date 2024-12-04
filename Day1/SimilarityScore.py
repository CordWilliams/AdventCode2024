def get_location_ids():
    list1 = []
    list2 = []

    with open("location_ids.txt", "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    return list1, list2


class SimilarityScore:

    def computeSimilarityScore(self):
        left_ids, right_ids = get_location_ids()

        right_freq = dict()
        for id in right_ids:
            right_freq[id] = right_freq.get(id, 0) + 1

        score = 0
        for id in left_ids:
            score += (id * right_freq.get(id, 0))

        return score


ss = SimilarityScore()
print(ss.computeSimilarityScore())