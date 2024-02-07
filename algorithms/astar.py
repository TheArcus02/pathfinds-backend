import heapq
from node import Node
from typing import List
from utils import get_closest_neighbors, init_grid


def heuristic(node: Node, end_node: Node) -> float:
    return abs(node.row - end_node.row) + abs(node.col - end_node.col)


def astar(nodes, start_node, end_node) -> List[Node]:
    """
    A* pathfinding algorithm

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

    start_node.distance = 0
    start_node.heuristic = heuristic(start_node, end_node)
    start_node.total_cost = start_node.heuristic

    open_set: List[Node] = []
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.is_visited:
            continue

        current_node.is_visited = True
        visits += 1
        current_node.when_visited = visits
        visited_in_order.append(current_node.to_dict())

        if current_node == end_node:
            return visited_in_order

        for n in get_closest_neighbors(current_node, grid):
            tentative_g_score = current_node.distance + n.weight + 1

            if tentative_g_score < n.distance:
                n.previous_node = current_node
                n.distance = tentative_g_score
                n.heuristic = heuristic(n, end_node)
                n.total_cost = n.distance + n.heuristic

                heapq.heappush(open_set, n)
    return visited_in_order
