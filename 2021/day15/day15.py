from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight_u, weight_v=None):
        if weight_v is None:
            weight_v = weight_u

        self.edges[u][v] = weight_v
        self.edges[v][u] = weight_u


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    queue = PriorityQueue()
    queue.put((0, start_vertex))

    while not queue.empty():
        (dist, current_vertex) = queue.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]

                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance

                    if new_cost < old_cost:
                        queue.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def load(name: str) -> tuple:
    with open(name, "r") as file:
        array = []
        lines = [line.replace('\n', '') for line in file.readlines() if line]
        for line in lines:
            if line:
                array.append([int(digit) for digit in line])

        return array


def part1(edges: list) -> int:
    size = len(edges)
    graph = Graph(size ** 2)

    for x in range(size):
        for y in range(size):
            if x > 0:
                graph.add_edge(x + y * size, x - 1 + y * size, edges[x - 1][y], edges[x][y])
            if y > 0:
                graph.add_edge(x + y * size, x + (y - 1) * size, edges[x][y - 1], edges[x][y])
            if x + 1 < size:
                graph.add_edge(x + y * size, x + 1 + y * size, edges[x + 1][y], edges[x][y])
            if y + 1 < size:
                graph.add_edge(x + y * size, x + (y + 1) * size, edges[x][y + 1], edges[x][y])

    D = dijkstra(graph, 0)
    max_key = max(D.keys())
    result = D[max_key] - edges[0][0] + edges[-1][-1]
    return result


def part2(edges: list) -> int:
    origin_size = len(edges)
    edges = edges * 5
    for i in range(origin_size):
        edges[i] *= 5
    size = len(edges)
    for i in range(size):
        for j in range(size):
            if i < origin_size and j < origin_size:
                continue

            value = edges[i][j]
            i_factor = i // origin_size
            j_factor = j // origin_size
            new_value = value + i_factor + j_factor
            edges[i][j] = new_value if new_value <= 9 else new_value - 9

    graph = Graph(size ** 2)

    for x in range(size):
        for y in range(size):
            if x > 0:
                graph.add_edge(x + y * size, x - 1 + y * size, edges[x - 1][y], edges[x][y])
            if y > 0:
                graph.add_edge(x + y * size, x + (y - 1) * size, edges[x][y - 1], edges[x][y])
            if x + 1 < size:
                graph.add_edge(x + y * size, x + 1 + y * size, edges[x + 1][y], edges[x][y])
            if y + 1 < size:
                graph.add_edge(x + y * size, x + (y + 1) * size, edges[x][y + 1], edges[x][y])

    D = dijkstra(graph, 0)
    max_key = max(D.keys())
    result = D[max_key] - edges[0][0] + edges[-1][-1]
    return result


if __name__ == '__main__':
    input_array = load('input-15')

    # result_part1 = part1(input_array)
    # print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
