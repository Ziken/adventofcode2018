import re
from collections import defaultdict


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            data_in = file.readlines()[0]

        return data_in

    def reduce_polymer(self, polymer: bytearray, omit_char1, omit_char2):
        # polymer = bytearray(self.puzzle_input, 'ascii')
        reduced_polymer = [0]
        j = 0

        for unit in polymer:
            if unit == omit_char1 or unit == omit_char2:
                continue
            if abs(reduced_polymer[j] - unit) == 32:
                j -= 1
                reduced_polymer.pop()
            else:
                reduced_polymer.append(unit)
                j += 1
        return j

    def get_answer_part_1(self):
        polymer = bytearray(self.puzzle_input, 'ascii')
        print("Answer part 1:", self.reduce_polymer(polymer, 0, 0))

    def get_answer_part_2(self):
        polymer = bytearray(self.puzzle_input, 'ascii')
        lp = [self.reduce_polymer(polymer, i + 65, i + 97) for i in range(25)]
        print("Answer part 2:", min(lp))

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
