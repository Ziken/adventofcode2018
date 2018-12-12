import re
from collections import defaultdict


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        # 2h = 120 min
        # 0-59 => from 00:00 to 00:59
        # 60-119 => from 23:00 to 23:59
        input = defaultdict(lambda: [0 for i in range(120)])
        pattern = re.compile(r"\[([0-9\-]+) ([0-9]+):([0-9]+)\] ([\w\W]+[^\n])")
        with open(file_name) as file:
            for line in file:
                data = pattern.match(line)
                date, hour, minute, action_desc = str(data.group(1)), int(data.group(2)), int(data.group(3)), data.group(4)
                action = 0 # No state

                if "shift" in action_desc:
                    guard_regexp = re.match(r"[\w]+ #([\d]+)", action_desc)
                    action = int(guard_regexp.group(1))
                elif "wakes" in action_desc:
                    action = -2
                elif "falls" in action_desc:
                    action = -1

                if hour > 0:
                    input[date][60+minute] = action
                else:
                    input[date][minute] = action

        return input

    def get_answers(self):
        guards_nap_length = defaultdict(lambda: defaultdict(lambda: 0)) # make list of 120 elements
        total_nap_length = defaultdict(lambda: 0)
        current_guard = 0
        for day in sorted(self.puzzle_input.keys()):
            fell_asleep = False
            for minute, action in enumerate(self.puzzle_input[day]):
                if action > 0:
                    current_guard = action
                elif action == -1:
                    fell_asleep = True
                elif action == -2:
                    fell_asleep = False

                if fell_asleep:
                    total_nap_length[current_guard] += 1
                    guards_nap_length[current_guard][minute] += 1

        max_total_nap = 0
        max_total_nap_guard = 0
        for guard, total_nap in total_nap_length.items():
            if total_nap > max_total_nap:
                max_total_nap = total_nap
                max_total_nap_guard = guard

        nap_length_in_same_minutes, what_minute = 0, 0
        for minutes, length in guards_nap_length[max_total_nap_guard].items():
            if length > nap_length_in_same_minutes:
                nap_length_in_same_minutes = length
                what_minute = minutes
        print("Part 1:", max_total_nap_guard * what_minute)

        best_guard, nap_length_in_same_minutes, what_minute = 0, 0, 0
        for guard in guards_nap_length:
            for minutes, length in guards_nap_length[guard].items():
                if length > nap_length_in_same_minutes:
                    # print(guard, minutes)
                    best_guard = guard
                    nap_length_in_same_minutes = length
                    what_minute = minutes

        print("Part 2:", best_guard*what_minute)


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
