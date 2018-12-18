import re


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            points = []
            velocity = []
            in_pattern = re.compile(r"position=<([ 0-9-]+), ([ 0-9-]+)> velocity=<([ 0-9-]+), ([ 0-9-]+)>")
            for line in file:
                matched = in_pattern.match(line)
                if matched:
                    m = matched.group
                    points.append([int(m(1)), int(m(2))])
                    velocity.append([int(m(3)), int(m(4))])
                else:
                    raise Exception("Regexp not match")

        return points, velocity

    def get_answers(self):
        points, velocity = self.puzzle_input
        max_y = 100
        min_y = 0
        second = 0
        while abs(max_y) - abs(min_y) > 10:
            for p in range(len(points)):
                points[p][0] += velocity[p][0]
                points[p][1] += velocity[p][1]

            max_y = max(max(points, key=lambda x: x[1]))
            min_y = min(min(points, key=lambda x: x[1]))
            second += 1

        max_x = max(max(points, key=lambda x: x[0]))
        min_x = min(min(points, key=lambda x: x[0]))

        print("Part 1:")
        for y in range(min_y, max_y + 1, 1):
            for x in range(min_x, max_x + 1, 1):
                if [x, y] in points:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()

        print("Part 2", second)


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
