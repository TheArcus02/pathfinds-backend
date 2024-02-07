import random
from typing import List
from node import Node
from utils import get_wall_neighbors, init_grid


def generate_maze(nodes) -> List[List[dict]]:
    """
    Generate a maze on the grid using Prim's algorithm

    :param nodes: list of node objects
    :return: board
    """
    start_row, start_col = (0, 0)

    grid = init_grid(nodes, for_maze=True)
    grid[start_row][start_col].is_wall = False

    frontier = get_wall_neighbors(grid[start_row][start_col], grid)

    while frontier:
        current: Node = random.choice(frontier)
        frontier.remove(current)

        neighbors = get_wall_neighbors(current, grid)
        in_maze_neighbors = [n for n in neighbors if not n.is_wall]

        if in_maze_neighbors:
            current.is_wall = False
            connect_to_maze: Node = random.choice(in_maze_neighbors)

            wall_to_remove_row = (current.row + connect_to_maze.row) // 2
            wall_to_remove_col = (current.col + connect_to_maze.col) // 2
            grid[wall_to_remove_row][wall_to_remove_col].is_wall = False

            new_frontiers = get_wall_neighbors(current, grid)
            for cell in new_frontiers:
                if cell not in frontier and cell.is_wall:
                    frontier.append(cell)

    return map_response(grid)


def map_response(grid: List[List[Node]]) -> List[List[dict]]:
    res = []
    for row in grid:
        row_list = []
        for node in row:
            if node.is_start or node.is_finish:
                node.is_wall = False
            row_list.append(node.to_dict())
        res.append(row_list)
    return res
