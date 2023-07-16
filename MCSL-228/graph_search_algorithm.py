from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        # self.CLOSE_visited = set()

    # def reset_visited_set(self):
    #     self.CLOSE_visited = set()

    def add_edge(self, u, v):
        # if u not in self.graph:
        #     self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_node, goal_node):
        print("BFS node traversal: ", end= " ")
        CLOSE_visited = set()
        OPEN_queue = []

        CLOSE_visited.add(start_node)
        OPEN_queue.append(start_node)

        while OPEN_queue:
            node = OPEN_queue.pop(0)
            print(node, end=" ")
            if node == goal_node:
                return True
                break

            for adjacent_node in self.graph[node]:
                if adjacent_node not in CLOSE_visited:
                    CLOSE_visited.add(adjacent_node)
                    OPEN_queue.append(adjacent_node)
        
        return False

    def dfs(self, start_node, goal_node):
        print("DFS node traversal: ", end=" ")
        CLOSE_visited = set()
        OPEN_stack = []

        CLOSE_visited.add(start_node)
        OPEN_stack.append(start_node)

        while OPEN_stack:
            node = OPEN_stack.pop(0)
            print(node, end=" ")
            if node == goal_node:
                return True
                break

            for adjacent_node in self.graph[node]:
                if adjacent_node not in CLOSE_visited:
                    CLOSE_visited.add(adjacent_node)
                    OPEN_stack.insert(0, adjacent_node)
        return False

    def _dfs_recursive(self, current_node, target_node, CLOSE_visited):
        if current_node == target_node:
            print(current_node, end=" ")
            return True
        
        # if start_node in CLOSE_visited:
        #     return False
        
        print(current_node, end=" ")
        CLOSE_visited.add(current_node)

        for adjacent_node in self.graph[current_node]:
            if adjacent_node not in CLOSE_visited and self._dfs_recursive(adjacent_node, target_node, CLOSE_visited):
                return True
        
        return False
    
    def dfs_recursive(self, start_node, goal_node):
        CLOSE_visited = set()
        print("Recursive DFS node traversal: ", end=" ")
        return self._dfs_recursive(start_node, goal_node, CLOSE_visited)

    def iddfs(self, start_node, goal_node, max_depth):
        print(f"Iterative DFS node traversal with depth[{max_depth}]: ", end=" ")
        for depth in range(1, max_depth + 1):
            CLOSE_visited = set()
            print(f"\nDepth: {depth}:", end=" ")
            if self._dfs_by_depth(start_node, goal_node, CLOSE_visited, depth):
                return True
        return False

    def _dfs_by_depth(self, current_node, target_node, CLOSE_visited, depth):
        if depth <= 0:
            return False
        
        if current_node == target_node:
            print(current_node, end=" ")
            return True

        print(current_node, end=" ")
        CLOSE_visited.add(current_node)

        for neighbor in self.graph[current_node]:
            if neighbor not in CLOSE_visited and self._dfs_by_depth(neighbor, target_node, CLOSE_visited, depth - 1):
                return True

        return False


def Graph1(g):
    g.add_edge(1, 2) 
    g.add_edge(1, 3) 
    g.add_edge(1, 4) 
    g.add_edge(2, 6) 
    g.add_edge(2, 3) 
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 7)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 5)
    g.add_edge(9, 6)
    g.add_edge(9, 8)
    return 1, 8

def Graph2(g):
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')

    g.add_edge('B', 'E')
    g.add_edge('B', 'F')

    g.add_edge('C', 'G')
    g.add_edge('C', 'H')

    g.add_edge('D', 'I')
    g.add_edge('D', 'J')

    g.add_edge('E', 'K')
    g.add_edge('E', 'L')

    g.add_edge('F', 'L')
    g.add_edge('F', 'M')

    g.add_edge('G', 'N')

    g.add_edge('H', 'O')
    g.add_edge('H', 'P')
    
    g.add_edge('I', 'P')
    g.add_edge('I', 'Q')
    
    g.add_edge('J', 'R')

    g.add_edge('K', 'S')
    g.add_edge('L', 'T')

    g.add_edge('P', 'U')

    return 'A', 'M'

if __name__ == '__main__':
    g = Graph()

    start_node, goal_node = Graph2(g)

    print("Traversal starting node", start_node)
    print("Traversal goal node", goal_node)

    if g.bfs(start_node, goal_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")
        
    if g.dfs(start_node, goal_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")

    if g.dfs_recursive(start_node, goal_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")

    if g.iddfs(start_node, goal_node, 5): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")