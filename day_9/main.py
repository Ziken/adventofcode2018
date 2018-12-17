from collections import deque, defaultdict


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            raw_data = file.readline()

        in_data = list(map(int, filter(str.isdigit ,raw_data.split())))
        return {
            "last_marble": in_data[1],
            "players": in_data[0],
        }

    def get_result(self, number_of_players, last_marble):
        board = deque([0])
        players_score = defaultdict(lambda: 0)
        for marble_index in range(1, last_marble+1):
            if marble_index % 23 == 0:
                board.rotate(7)
                players_score[marble_index % number_of_players] += marble_index + board.pop()
                board.rotate(-1)
            else:
                board.rotate(-1)
                board.append(marble_index)

        return max(players_score.values())

    def get_answers(self):
        print("Part 1:", self.get_result(self.puzzle_input["players"], self.puzzle_input["last_marble"]))
        print("Part 1:", self.get_result(self.puzzle_input["players"], self.puzzle_input["last_marble"]*100))


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
