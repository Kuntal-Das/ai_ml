from queue import PriorityQueue


class Puzzle:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.goal_state = '1472836-5'#'12345678-'

    def __lt__(self, other):
        return self.cost < other.cost

    def generate_children(self):
        children = []
        moves = ['up', 'down', 'left', 'right']
        for move in moves:
            child_state = self.get_child_state(move)
            if child_state is not None:
                child = Puzzle(child_state, self, move, self.depth + 1, 0)
                child.cost = self.calculate_cost(child)
                children.append(child)
        return children

    def get_child_state(self, move):
        blank_index = self.state.index('-')
        if move == 'up':
            if blank_index < 3:
                return None
            else:
                new_index = blank_index - 3
        elif move == 'down':
            if blank_index > 5:
                return None
            else:
                new_index = blank_index + 3
        elif move == 'left':
            if blank_index in [0, 3, 6]:
                return None
            else:
                new_index = blank_index - 1
        else:
            if blank_index in [2, 5, 8]:
                return None
            else:
                new_index = blank_index + 1
        child_state = list(self.state)
        child_state[blank_index], child_state[new_index] = child_state[new_index], child_state[blank_index]
        return ''.join(child_state)

    def calculate_cost(self, child):
        cost = 0
        for i in range(9):
            if child.state[i] != '-':
                goal_index = self.goal_state.index(child.state[i])
                distance = abs(i // 3 - goal_index // 3) + \
                    abs(i % 3 - goal_index % 3)
                cost += distance
        return cost + child.depth

    def solve(self):
        frontier = PriorityQueue()
        frontier.put(self)
        explored = set()
        while not frontier.empty():
            current_node = frontier.get()
            if current_node.state == self.goal_state:
                path = []
                while current_node.move:
                    self.print_state(current_node.state)  # print current state
                    path.append(current_node.move)
                    current_node = current_node.parent
                path.reverse()
                return path
            explored.add(current_node.state)
            children = current_node.generate_children()
            for child in children:
                if child.state not in explored:
                    frontier.put(child)

    def print_state(self, state):
        for i in range(0, 9):
            if (i + 1) % 3 == 0:
                print(state[i], end="\n")
            else:
                print(state[i], end="\t")

        print()


start_state = '12348-765'#'15786-324'
puzzle = Puzzle(start_state, None, None, 0, 0)
path = puzzle.solve()
print(path)
