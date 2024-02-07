from node import Node
from typing import List


def get_closest_neighbors(node: Node, grid: List[List[Node]]) -> List[Node]:
    neighbors = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    for d in directions:
        row, col = node.row + d[1], node.col + d[0]
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and \
                not grid[row][col].is_visited and not grid[row][col].is_wall:
            neighbors.append(grid[row][col])
    return neighbors


def get_wall_neighbors(node: Node, grid: List[List[Node]]) -> List[Node]:
    neighbors = []
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    for d in directions:
        row, col = node.row + d[1], node.col + d[0]
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            neighbors.append(grid[row][col])
    return neighbors


def init_grid(nodes, for_maze=False) -> List[List[Node]]:
    return [[Node(row=i, col=j,
                  is_wall=True if for_maze else node['isWall'],
                  is_start=node['isStart'],
                  is_finish=node['isFinish'],
                  weight=node['weight'])
             for j, node in enumerate(row)]
            for i, row in enumerate(nodes)]


def generate_board(start, finish, total_cols: int, total_rows: int):
    nodes = [
        [
            Node(col, row,
                 is_start=(start['col'] is col) and (start['row'] is row),
                 is_finish=(finish['col'] is col) and (finish['row'] is row)).to_dict()
            for col in range(total_cols)
        ]
        for row in range(total_rows)
    ]

    return {
        "nodes": nodes,
        "startNode": {
            "row": start['row'],
            "col": start['col']
        },
        "endNode": {
            "row": finish['row'],
            "col": finish['col']
        }
    }
