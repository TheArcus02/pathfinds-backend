import heapq
from typing import List
from node import Node
from utils import get_closest_neighbors, init_grid


def dijkstra(nodes, start_node, end_node) -> List[Node]:
    """
    Dijkstra pathfinding algorithm

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

    priority_queue = [start_node]

    start_node.distance = 0

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.is_visited:
            continue

        current_node.is_visited = True
        visits += 1
        current_node.when_visited = visits
        visited_in_order.append(current_node.to_dict())

        if current_node == end_node:
            return visited_in_order

        for n in get_closest_neighbors(current_node, grid):
            temp_distance = current_node.distance + n.weight + 1

            if temp_distance < n.distance:
                n.distance = temp_distance
                n.total_cost = temp_distance
                n.previous_node = current_node
                heapq.heappush(priority_queue, n)
    return visited_in_order
