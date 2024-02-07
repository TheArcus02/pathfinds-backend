from node import Node
from collections import deque
from utils import get_closest_neighbors, init_grid
from typing import List


def bfs(nodes, start_node, end_node) -> List[Node]:
    """
    Breath first search pathfinding algorithm

    :param nodes: list of node objects
    :param start_node: starting node col and row
    :param end_node: ending node col and row
    :return: nodes visited in order
    """
    visits = 0
    visited_in_order = []

    rows = len(nodes)
    cols = len(nodes[0]) if rows > 0 else 0

    grid = init_grid(nodes)

    start_node = grid[start_node['row']][start_node['col']]
    end_node = grid[end_node['row']][end_node['col']]

    queue = deque([start_node])

    start_node.is_visited = True

    while queue:
        current_node = queue.popleft()

        visits += 1
        current_node.when_visited = visits
        visited_in_order.append(current_node.to_dict())

        if current_node == end_node:
            return visited_in_order

        neighbors = get_closest_neighbors(current_node, grid)

        for n in neighbors:
            n.is_visited = True
            n.previous_node = current_node
            queue.append(n)
