class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            return [int(line.strip()) for line in file]

    def get_answer_part_1(self):
        result = sum(self.puzzle_input)
        print("Part 1:", result)

    def get_answer_part_2(self):
        past_sums = dict()
        sum_found_twice = False
        current_sum = 0
        i = 0
        while not sum_found_twice:
            current_sum += self.puzzle_input[i]
            p = past_sums.get(current_sum, 0)
            if p >= 1:
                sum_found_twice = True
            past_sums[current_sum] = p + 1
            i += 1
            i %= len(self.puzzle_input)
        print("Part 2:", current_sum)

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    solutions = Solution("input.txt")
    solutions.get_answers()
