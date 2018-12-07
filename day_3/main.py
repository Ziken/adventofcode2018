import re


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        input = []
        with open(file_name) as file:
            for line in file:
                data = re.match(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)[\n]*", line, re.M | re.I)
                input.append({
                    "start": {
                        "x": int(data.group(2)),
                        "y": int(data.group(3)),
                    },
                    "end": {
                        "x": int(data.group(2)) + int(data.group(4)),
                        "y": int(data.group(3)) + int(data.group(5)),
                    },
                    "id_fabric": int(data.group(1))
                })
            return input

    def get_answers(self):
        square = [[0 for x in range(1000)] for y in range(1000)]
        overlap_fabrics = [True] * (len(self.puzzle_input) + 1)
        overlapping_inches = 0
        for i in range(len(self.puzzle_input)):
            fabric = self.puzzle_input[i]
            for y in range(fabric["start"]["y"], fabric["end"]["y"]):
                for x in range(fabric["start"]["x"], fabric["end"]["x"]):
                    if square[y][x] == 0:
                        square[y][x] = fabric["id_fabric"]
                    elif square[y][x] == -1:
                        overlap_fabrics[fabric["id_fabric"]] = False
                    elif square[y][x] > 0:
                        overlapping_inches += 1
                        overlap_fabrics[fabric["id_fabric"]] = False
                        overlap_fabrics[square[y][x]] = False
                        square[y][x] = -1  # mark as counted inch

        separated_fabric = list(filter(lambda x: x[1], enumerate(overlap_fabrics)))[1][0]
        print("Answer part 1:", overlapping_inches)
        print("Answer part 2:", separated_fabric)


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
