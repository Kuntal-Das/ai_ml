from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node, goal_node):
        print("\nBFS node traversal: ", end= " ")
        CLOSE_visited = set()
        OPEN_queue = []

        CLOSE_visited.add(start_node)
        OPEN_queue.append(start_node)

        while OPEN_queue:
            node = OPEN_queue.pop(0)
            print(node, end=" ")
            if node == goal_node:
                break

            for adjacent_node in self.graph[node]:
                if adjacent_node not in CLOSE_visited:
                    CLOSE_visited.add(adjacent_node)
                    OPEN_queue.append(adjacent_node)

    def dfs(self, start_node, goal_node):
        print("\nDFS node traversal: ", end=" ")
        CLOSE_visited = set()
        OPEN_stack = []

        CLOSE_visited.add(start_node)
        OPEN_stack.append(start_node)

        while OPEN_stack:
            node = OPEN_stack.pop(0)
            print(node, end=" ")
            if node == goal_node:
                break

            for adjacent_node in self.graph[node]:
                if adjacent_node not in CLOSE_visited:
                    CLOSE_visited.add(adjacent_node)
                    OPEN_stack.insert(0, adjacent_node)

if __name__ == '__main__':
    # Example usage
    g = Graph()
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

    start_node, goal_node = 1, 8
    print("Traversal starting node", start_node)
    print("Traversal goal node", goal_node)
    g.bfs(start_node, goal_node)
    g.dfs(start_node, goal_node)