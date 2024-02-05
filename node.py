import json


class Node:
    def __init__(self, col, row, is_wall=False, is_start=False, is_finish=False):
        self.col = col
        self.row = row
        self.is_visited = False
        self.is_wall = is_wall
        self.is_start = is_start
        self.is_finish = is_finish
        self.previous_node = None
        self.when_visited = 0

    def to_dict(self):
        return {
            'col': self.col,
            'row': self.row,
            'is_visited': self.is_visited,
            'is_wall': self.is_wall,
            'is_start': self.is_start,
            'is_finish': self.is_finish,
            'previous_node': self.previous_node.to_dict() if self.previous_node else None,
            'when_visited': self.when_visited,
        }
