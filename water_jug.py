from collections import deque
import copy


class water_jug_problem:
    def __init__(self, jug1=4, jug2=3):
        self.jug1 = jug1
        self.jug2 = jug2

    def fill_jug1(self, curr_state, is_verbose=True):
        if is_verbose:
            print(f"Fill {self.jug1}-gallon jug")
        return (self.jug1, curr_state[1])

    def fill_jug2(self, curr_state, is_verbose=True):
        if is_verbose:
            print(f"Fill {self.jug2}-gallon jug")
        return (curr_state[0], self.jug2)

    def empty_jug1(self, curr_state, is_verbose=True):
        if is_verbose:
            print(f"Empty {self.jug1}-gallon jug")
        return (0, curr_state[1])

    def empty_jug2(self, curr_state, is_verbose=True):
        if is_verbose:
            print(f"Empty {self.jug2}-gallon jug")
        return (curr_state[0], 0)

    def pour_jug2_jug1_until_full(self, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour water from {self.jug2}-gallon jug into {self.jug1}-gallon jug until {self.jug1}-gallon jug is full")
        return (self.jug1, curr_state[1] - (self.jug1 - curr_state[0]))

    def pour_jug1_jug2_until_full(self, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour water from {self.jug1}-gallon jug into {self.jug2}-gallon jug until {self.jug2}-gallon jug is full")
        return (curr_state[0] - (self.jug2 - curr_state[1]), self.jug2)

    def pour_allfrom_jug1_jug2(self, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour all water from {self.jug2}-gallon jug into {self.jug1}-gallon jug")
        return (curr_state[0] + curr_state[1], 0)

    def pour_allfrom_jug2_jug1(self, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour all water from {self.jug1}-gallon jug into {self.jug2}-gallon jug")
        return (0, curr_state[0] + curr_state[1])

    def pourout_fromjug1(self, amount, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour some water {amount} out from {self.jug1}-gallon jug")
        return (curr_state[0] - amount, curr_state[0])

    def pourout_fromjug2(self, amount, curr_state, is_verbose=True):
        if is_verbose:
            print(
                f"Pour some water {amount} out from {self.jug2}-gallon jug")
        return (curr_state[0], curr_state[1] - amount)

    possible_steps = {
        1: fill_jug1,
        2: fill_jug2,
        3: empty_jug1,
        4: empty_jug2,
        5: pour_jug2_jug1_until_full,
        6: pour_jug1_jug2_until_full,
        7: pour_allfrom_jug1_jug2,
        8: pour_allfrom_jug2_jug1,
        9: pourout_fromjug1,
        10: pourout_fromjug2,
    }

    def get_next_possible_steps(self, curr_state):
        step_list = list()
        for i in self.possible_steps.keys():
            next_state = (-1, -1)
            if i == 9:
                for j in range(1, self.jug1):
                    next_state = self.possible_steps[i](
                        self, j, curr_state, False)
                    if (self.is_vaild_state(curr_state, next_state)):
                        step_list.append((i, j))

            elif i == 10:
                for j in range(1, self.jug2):
                    next_state = self.possible_steps[i](
                        self, j, curr_state, False)
                    if (self.is_vaild_state(curr_state, next_state)):
                        step_list.append((i, j))
            else:
                next_state = self.possible_steps[i](self, curr_state, False)
                if (self.is_vaild_state(curr_state, next_state)):
                    step_list.append((i, -1))

        return step_list

    def is_vaild_state(self, curr_state, next_state):
        return next_state[0] >= 0 and next_state[1] >= 0 and next_state[0] <= self.jug1 and next_state[1] <= self.jug2 and next_state != curr_state

    def BFS(self, target, initial_state=(0, 0), visited={}):
        # isSolvable = False
        path = []
        visited_copy = copy.deepcopy(visited)
        visited_copy[initial_state] = True
        neighbours = self.get_next_possible_steps(initial_state)

        for (i, j) in neighbours:
            next_state = (-1, -1)
            if i == 9 or i == 10:
                next_state = self.possible_steps[i](
                    self, j, initial_state, False)
            else:
                next_state = self.possible_steps[i](self, initial_state, False)

            if (next_state[0] == target[0]):# and next_state[1] == target[1]):
                visited_copy[next_state] = True
                path.append((i, j))
                break

            # or visited_copy[next_state] == False:
            if next_state not in visited_copy.keys():
                tpath = self.BFS(target, next_state,visited_copy)
                if len(tpath) > 0 and tpath[-1][0] == target[0]:
                    visited_copy[next_state] = True
                    path.extend(tpath)
                    return path

        return path

    def print_path(self, path, initial_state=(0, 0)):
        next_state = initial_state
        for (i, j) in path:
            print(next_state, end=" :\t")
            if i == 9 or i == 10:
                next_state = self.possible_steps[i](self, j, next_state)
            else:
                next_state = self.possible_steps[i](self, next_state)


# Driver code
if __name__ == '__main__':
    print("Path from initial state "
          "to solution state ::")
    wjp = water_jug_problem()
    path = wjp.BFS((2, 0))
    wjp.print_path(path)

# This code is contributed by mohit kumar 29
