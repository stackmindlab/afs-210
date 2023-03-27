graph = {
    'A': {'B': 2, 'C': 1, 'D': 3, 'E': 9, 'F': 20},
    'B': {'C': 4, 'E': 3},
    'C': {'D': 8},
    'D': {'E': 5},
    'E': {'F': 5},
    'F': {'G': 2, 'H': 2, 'C': 2},
    'G': {'F': 1, 'H': 6},
    'H': {'G': 8, 'F': 9},
    'I': {}

}

# finds shortest path between 2 nodes of a graph using BFS

def breadth_first_search(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            # go through all neighbor nodes, construct a new path and
            # push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # return path if neighbor is goal
                if neighbor == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "Route Not Possible"


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path, shortest_paths[end][1]


print("Shortest path between a and h is",
      breadth_first_search(graph, 'A', 'H'))
print("Cheapest path between a and h is", dijsktra(graph, 'A', 'H')[0])
print("The cost of going between a and h is", dijsktra(graph, 'A', 'H')[1])
