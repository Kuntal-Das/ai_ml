class Puzzle:
    def __init__(self, state, parent, move):
        self.state = state
        self.parent = parent
        self.move = move
        self.goal_state = '1472863-5'#' 12345678-'

    def generate_children(self):
        children = []
        moves = ['up', 'down', 'left', 'right']
        blank_index = self.state.index('-')
        for move in moves:
            if self.is_valid_move(move, blank_index):
                child_state = self.get_child_state(move, blank_index)
                child = Puzzle(child_state, self, move)
                children.append(child)
        return children

    def is_valid_move(self, move, blank_index):
        if move == 'up' and blank_index >= 3:
            return True
        elif move == 'down' and blank_index <= 5:
            return True
        elif move == 'left' and blank_index % 3 != 0:
            return True
        elif move == 'right' and (blank_index + 1) % 3 != 0:
            return True
        return False

    def get_child_state(self, move, blank_index):
        child_state = list(self.state)
        if move == 'up':
            new_index = blank_index - 3
        elif move == 'down':
            new_index = blank_index + 3
        elif move == 'left':
            new_index = blank_index - 1
        else:
            new_index = blank_index + 1
        child_state[blank_index], child_state[new_index] = child_state[new_index], child_state[blank_index]
        return ''.join(child_state)

    def solve(self):
        visited = set()
        stack = [self]
        while stack:
            current_node = stack.pop()
            if current_node.state == self.goal_state:
                path = []
                while current_node.move:
                    path.append(current_node.move)
                    current_node = current_node.parent
                path.reverse()
                return path
            visited.add(current_node.state)
            children = current_node.generate_children()
            for child in children:
                if child.state not in visited:
                    stack.append(child)
        return None

start_state = '12348-765'#'15786-324'#
puzzle = Puzzle(start_state, None, None)
path = puzzle.solve()
print(path)
