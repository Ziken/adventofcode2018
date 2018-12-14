from collections import defaultdict


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        in_data = []
        with open(file_name, "r") as file:
            for line in file:
                in_data.append(tuple(map(int, line.split(', '))))
        return in_data

    def get_d(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def get_answer_part_1(self):
        areas_size = defaultdict(lambda: 0)
        gird_size = 400
        for y in range(gird_size):
            for x in range(gird_size):
                best = self.puzzle_input[0]
                tied = False
                for point in self.puzzle_input[1:]:
                    if self.get_d(point[0], point[1], x, y) < self.get_d(best[0], best[1], x, y):
                        best = point
                        tied = False
                    elif self.get_d(point[0], point[1], x, y) == self.get_d(best[0], best[1], x, y):
                        tied = True

                if not tied:
                    areas_size[best] += 1

        infinite_areas = set()

        for i in range(gird_size):
            best1 = self.puzzle_input[0]
            best2 = self.puzzle_input[0]
            best3 = self.puzzle_input[0]
            best4 = self.puzzle_input[0]
            # check borders of grid
            for point in self.puzzle_input:
                if self.get_d(point[0], point[1], 0, i) < self.get_d(best1[0], best1[1], 0, i):
                    best1 = point

                if self.get_d(point[0], point[1], gird_size - 1, i) < self.get_d(best2[0], best2[1], gird_size - 1, i):
                    best2 = point

                if self.get_d(point[0], point[1], i, gird_size-1) < self.get_d(best3[0], best3[1], i, gird_size-1):
                    best3 = point

                if self.get_d(point[0], point[1], i, 0) < self.get_d(best4[0], best4[1], i, 0):
                    best4 = point
            infinite_areas.add(best1)
            infinite_areas.add(best2)
            infinite_areas.add(best3)
            infinite_areas.add(best4)

        finite_areas = set(areas_size.keys()) - infinite_areas
        max_finite_area = 0
        for area in finite_areas:
            max_finite_area = max(areas_size[area], max_finite_area)

        print("Part 1:", max_finite_area)

    def get_answer_part_2(self):
        distances_to_all_points = defaultdict(lambda: 0)
        gird_size = 400
        for y in range(gird_size):
            for x in range(gird_size):
                distance = 0
                for point in self.puzzle_input:
                    distance += self.get_d(point[0], point[1], x, y)
                distances_to_all_points[distance] += 1

        max_area = 0
        for distance in distances_to_all_points.keys():
            if distance < 10000:
                max_area += distances_to_all_points[distance]

        print("Part 2:", max_area)

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    solutions = Solution("input.txt")
    solutions.get_answers()
