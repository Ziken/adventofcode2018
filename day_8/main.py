class Node:
    def __init__(self):
        self.children = []
        self.meta = []
        self.value = 0


class Solution:
    def __init__(self, input_file_name):
        self.puzzle_input = self.read_input_from_file(input_file_name)

    def read_input_from_file(self, file_name):
        with open(file_name) as file:
            in_data = file.readlines()[0]

        in_data = list(map(int, in_data.split()))
        root = self.parse_input(in_data)
        return root

    def parse_input(self, data):
        ptr = 0

        def generate_tree(sliced_data):
            nonlocal ptr
            node = Node()
            num_of_children, num_of_meta = sliced_data[ptr], sliced_data[ptr + 1]
            ptr += 2
            children = []
            while num_of_children:
                children.append(generate_tree(sliced_data))
                num_of_children -= 1

            meta = sliced_data[ptr:ptr + num_of_meta]

            if not children:
                node.value = sum(meta)
            else:
                for m in meta:
                    try:
                        node.value += children[m-1].value
                    except IndexError:
                        pass

            node.children = children
            node.meta = meta
            ptr += num_of_meta
            return node

        root = generate_tree(data)
        return root

    def get_answer_part_1(self):
        def get_sum_of_meta(node):
            s = sum(node.meta)
            for ch in node.children:
                s += get_sum_of_meta(ch)

            return s

        print("Part 1:", get_sum_of_meta(self.puzzle_input))

    def get_answer_part_2(self):
        print("Part 2:",  self.puzzle_input.value)

    def get_answers(self):
        self.get_answer_part_1()
        self.get_answer_part_2()


if __name__ == "__main__":
    try:
        solutions = Solution("input.txt")
        solutions.get_answers()
    except FileNotFoundError as err:
        print("File input.txt not found.")
