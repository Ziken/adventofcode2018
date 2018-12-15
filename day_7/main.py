from collections import defaultdict, deque


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        in_data = []
        with open(file_name) as file:
            for line in file:
                splitted_line = line.split(" ")
                in_data.append((splitted_line[1], splitted_line[7]))
        return in_data

    def get_answer_part_1(self):
        adjacency_list = defaultdict(list)
        number_of_connections = defaultdict(lambda: 0)
        for (from_node, to_node) in self.puzzle_input:
            number_of_connections[to_node] += 1
            adjacency_list[from_node].append(to_node)

        available_nodes = set()
        for to_node in adjacency_list:
            if number_of_connections[to_node] == 0:
                available_nodes.add(to_node)

        answer = ""
        while available_nodes:
            current_node = min(available_nodes)
            available_nodes.remove(current_node)
            answer += current_node
            for to_node in adjacency_list[current_node]:
                number_of_connections[to_node] -= 1
                if number_of_connections.get(to_node, -1) == 0:
                    number_of_connections[to_node] -= 1
                    available_nodes.add(to_node)

        print("Part 1:", answer)

    def get_answer_part_2(self):
        adjacency_list = defaultdict(list)
        number_of_connections = defaultdict(lambda: 0)
        for (from_node, to_node) in self.puzzle_input:
            number_of_connections[to_node] += 1
            adjacency_list[from_node].append(to_node)

        available_nodes = set()
        for to_node in adjacency_list:
            if number_of_connections[to_node] == 0:
                available_nodes.add(to_node)

        max_number_of_workers = 5
        second = 0
        workers = deque()
        while available_nodes or workers:
            used_nodes = []
            while available_nodes and len(workers) < max_number_of_workers:
                node = min(available_nodes)
                available_nodes.remove(node)
                workers.append([ord(node) - 64 + 60, node])

            complete_nodes = []
            min_sec = min(workers, key=lambda x: x[0])[0]
            for id_worker in range(len(workers)):
                workers[id_worker][0] -= min_sec
                if workers[id_worker][0] == 0:
                    complete_nodes.append(id_worker)

            for i in complete_nodes:
                used_nodes.extend(workers[i][1])
                del workers[i]

            second += min_sec

            for current_node in used_nodes:
                for to_node in adjacency_list[current_node]:
                    number_of_connections[to_node] -= 1
                    if number_of_connections.get(to_node, -1) == 0:
                        number_of_connections[to_node] -= 1
                        available_nodes.add(to_node)

        print("Part 2:", second)

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")

