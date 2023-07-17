from collections import defaultdict
import heapq
import math

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self._huristics = defaultdict(int)

    def add_edge(self, parent_node, node, edge_weight):
        # Add an edge between nodes parent_node and node with the given edge_weight
        self.graph[parent_node].append((node, edge_weight))

    def add_huristic(self, node, huristic):
        # Add heuristic value for the given node
        self._huristics[node] = huristic
        # Since we are adding a heuristic value for this node,
        # we initialize an empty list for this node in the graph.
        self.graph[node] = []


    def get_huristic(self, node, target) -> int:
        # Get the heuristic value for the given node and target
        return self._huristics[node]

    def best_first_search(self, start_node, target_node):
        # Best-First Search algorithm
        print("Best first search node traversal: ", end=" ")
        CLOSE_visited = set()
        priority_queue = [(self.get_huristic(start_node, target_node), start_node)]

        while priority_queue:
            (priority, current_node) = heapq.heappop(priority_queue)

            if current_node in CLOSE_visited:
                # Skip if the current node has already been visited
                continue
            
            print(f"({current_node}, {priority})", end=" ")
            CLOSE_visited.add(current_node)

            if current_node == target_node:
                # If we have reached the target node, return True
                return True

            for neighbor, weight in self.graph[current_node]:
                huristic = self.get_huristic(neighbor, target_node)
                # Calculate the heuristic value of the neighbor node with respect to the target
                if neighbor not in CLOSE_visited:
                    heapq.heappush(priority_queue, (huristic, neighbor))
                    # Add the neighbor node with its heuristic value to the priority queue
        return False

    def a_start_search(self, start_node, target_node):
        # A* Search algorithm
        print("A* search node traversal: ", end=" ")
        CLOSE_visited = set()
        g_score = defaultdict(int)
        priority_queue = [(self.get_huristic(start_node, target_node), start_node)]
        g_score[start_node] = 0

        while priority_queue:
            (priority, current_node) = heapq.heappop(priority_queue)

            if current_node in CLOSE_visited:
                # Skip if the current node has already been visited
                continue
            
            print(f"({current_node}, {priority})", end=" ")
            CLOSE_visited.add(current_node)

            if current_node == target_node:
                # If we have reached the target node, return True
                return True

            for neighbor, weight in self.graph[current_node]:
                huristic = self.get_huristic(neighbor,target_node) 
                # Calculate the heuristic value of the neighbor node with respect to the target
                g_score[neighbor] = weight + g_score[current_node]
                # Calculate the g-score (the actual cost to reach the neighbor node from the start node)
                
                if neighbor not in CLOSE_visited:
                    heapq.heappush(priority_queue, (g_score[neighbor] + huristic, neighbor))
                    # Add the neighbor node with its priority value (g-score + heuristic) to the priority queue
        return False

    def ida_star_search(self, start_node, target_node, increment_val=1):
        # Iterative Deepening A* Search algorithm
        print("Iterative Deepening A* search node traversal: ", end=" ")
        
        def dfs(current_node, path_cost, depth_limit):
            priority = path_cost + self.get_huristic(current_node, target_node)

            if priority > depth_limit:
                # If the priority value exceeds the depth limit, return priority and False
                return priority, False

            print(f"({current_node}, {priority})", end=" ")
            
            if current_node == target_node:
                # If we have reached the target node, return priority and True
                return priority, True

            min_cost = math.inf
            for neighbor, weight in self.graph[current_node]:
                new_cost, found = dfs(neighbor, path_cost + weight, depth_limit)
                # Recursively call dfs for the neighbor node
                if found:
                    return new_cost, True
                min_cost = min(min_cost, new_cost)
                # Update the minimum cost encountered in the search

            return min_cost, False

        depth_limit = self.get_huristic(start_node, target_node)
        while True:
            print(f"\nThreshold: {depth_limit} :",end=" ")
            _, found = dfs(start_node, 0, depth_limit)
            # Call dfs with the current depth limit
            if found:
                # If the target node is found within the depth limit, return True
                return True
            depth_limit = math.inf if depth_limit == math.inf else depth_limit + increment_val
            # Increment the depth limit for the next iteration
        
        return False


def Graph4(g:Graph):
    # Create the fourth graph and add heuristic values and edges
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
    g.add_edge(5, 6, 20)
    
    return 1, 6
    
def Graph3(g:Graph):
    # Create the third graph and add heuristic values and edges
    g.add_huristic(1, 12)
    g.add_huristic(2, 10)
    g.add_huristic(3, 16)
    g.add_huristic(4, 15)

    g.add_huristic(5, 12)
    g.add_huristic(6, 7)
    g.add_huristic(7, 11)
    g.add_huristic(8, 15)
    
    g.add_huristic(9, 12)
    g.add_huristic(10, 4)
    g.add_huristic(11, 1)
    g.add_huristic(12, 0)

    g.add_edge(1, 2, 2)
    g.add_edge(1, 5, 1)

    g.add_edge(2, 3, 1)
    g.add_edge(2, 6, 3)

    g.add_edge(3, 4, 2)
    g.add_edge(4, 8, 1)
    g.add_edge(5, 9, 1)

    g.add_edge(6, 5, 5)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 10, 4)
    
    g.add_edge(7, 3, 3)
    g.add_edge(7, 11, 10)

    g.add_edge(8, 7, 5)
    g.add_edge(8, 12, 15)

    g.add_edge(9, 10, 8)
    g.add_edge(10, 11, 3)
    g.add_edge(11, 12, 1)

    return 1, 12

if __name__ == '__main__':
    g = Graph()
    start_node, goal_node = Graph3(g)

    print(f"Start Node: {start_node}, Goal Node: {goal_node}")

    if g.best_first_search(start_node, goal_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")

    if g.a_start_search(start_node, goal_node): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")

    if g.ida_star_search(start_node, goal_node, 2): print("\t[GOAL FOUND]")
    else: print("\t[GOAL NOT FOUND]")    
