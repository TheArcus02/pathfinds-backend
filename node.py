import json


class Node:
    def __init__(self, col, row, weight=0, is_wall=False, is_start=False,
                 is_finish=False, is_path=False):
        self.col = col
        self.row = row
        self.distance = 1e9
        self.weight = weight
        self.heuristic = 1e9
        self.is_visited = False
        self.when_visited = 0
        self.is_wall = is_wall
        self.is_start = is_start
        self.is_finish = is_finish
        self.is_path = is_path
        self.previous_node = None
        self.when_visited = 0

    def to_dict(self):
        return {
            'col': self.col,
            'row': self.row,
            'distance': self.distance,
            'weight': self.weight,
            'heuristic': self.heuristic,
            'isVisited': self.is_visited,
            'whenVisited': self.when_visited,
            'isWall': self.is_wall,
            'isStart': self.is_start,
            'isFinish': self.is_finish,
            'isPath': self.is_path,
            'previousNode': self.previous_node.to_dict() if self.previous_node else None,
        }
