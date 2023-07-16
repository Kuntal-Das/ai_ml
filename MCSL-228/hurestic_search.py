from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.huristics = defaultdict(int)

    def add_edge(self, parent_node, node, edge_weight):
        self.graph[parent_node].append((node, edge_weight))

    def add_huristic(self, node, huristic):
        self.huristics[node] = huristic
        self.graph[node] = []

    def best_first_search(self, start_node, target_node):
        visited = set()
        priority_queue = [(self.huristics[start_node], start_node)]

        while priority_queue:
            (priority, current_node) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            
            print(current_node, end=" ")
            visited.add(current_node)

            if current_node == target_node:
                return True

            for neighbor, weight in self.graph[current_node]:
                huristic = self.huristics[neighbor]
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (huristic, neighbor))
        return False

def Graph1(g:Graph):
    g.add_huristic(1, 5)
    g.add_huristic(2, 4)
    g.add_huristic(3, 23)
    g.add_huristic(4, 2)
    g.add_huristic(5, 3)
    g.add_huristic(6, 0)

    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 14)
    
    return 1, 6
    

if __name__ == '__main__':
    g = Graph()
    start_node, target_node = Graph1(g)

    if g.best_first_search(start_node, target_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")