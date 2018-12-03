from collections import Counter


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            return [line.strip() for line in file]

    def get_answer_part_1(self):
        two_same_letters = 0
        three_same_letters = 0
        for box in self.puzzle_input:
            letters_counter = Counter(box).values()
            if 2 in letters_counter:
                two_same_letters += 1
            if 3 in letters_counter:
                three_same_letters += 1

        print("Part 1:", two_same_letters * three_same_letters)

    def get_answer_part_2(self):
        for first_box_id in range(len(self.puzzle_input)):
            for second_box_id in range(first_box_id + 1, len(self.puzzle_input)):
                first_box = self.puzzle_input[first_box_id]
                second_box = self.puzzle_input[second_box_id]
                if len(first_box) != len(second_box):
                    continue

                same_letters = list(filter(lambda x: x[0] == x[1], zip(first_box, second_box)))
                if len(same_letters) - len(first_box) == -1:
                    print("Part 2: ", end="")
                    for f, s in same_letters:
                        print(f, end="")
                    print("")

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
