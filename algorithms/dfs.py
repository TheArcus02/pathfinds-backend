from typing import List
from node import Node
from utils import get_closest_neighbors


def dfs(nodes, start_node, end_node) -> List[Node]:
    """
    Depth first search algorithm

    :param nodes: list of node objects
    :param start_node: starting node col and row
    :param end_node: ending node col and row
    :return: nodes visited in order
    """

    visits = 0
    visited_in_order = []

    rows = len(nodes)
    cols = len(nodes[0]) if rows > 0 else 0

    grid = [[Node(row=i, col=j,
                  is_wall=node['isWall'],
                  is_start=node['isStart'],
                  is_finish=node['isFinish'])
             for j, node in enumerate(row)]
            for i, row in enumerate(nodes)]

    start_node = grid[start_node['row']][start_node['col']]
    end_node = grid[end_node['row']][end_node['col']]

    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node.is_visited:
            continue

        current_node.is_visited = True
        visits += 1
        current_node.when_visited = visits
        visited_in_order.append(current_node.to_dict())

        if current_node == end_node:
            return visited_in_order

        neighbors = get_closest_neighbors(current_node, grid)

        for n in neighbors:
            if not n.is_visited:
                n.previous_node = current_node
                stack.append(n)

    return visited_in_order
