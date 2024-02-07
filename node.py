import json


class Node:
    def __init__(self, col, row, weight=0, is_wall=False, is_start=False,
                 is_finish=False, is_path=False):
        self.col = col
        self.row = row
        self.distance = float('inf')
        self.weight = weight
        self.heuristic = float('inf')
        self.total_cost = float('inf')
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
            'distance': 1e9 if self.distance == float('inf') else self.distance,
            'weight': self.weight,
            'heuristic': 1e9 if self.heuristic == float('inf') else self.heuristic,
            'totalCost': 1e9 if self.total_cost == float('inf') else self.total_cost,
            'isVisited': self.is_visited,
            'whenVisited': self.when_visited,
            'isWall': self.is_wall,
            'isStart': self.is_start,
            'isFinish': self.is_finish,
            'isPath': self.is_path,
            'previousNode': self.previous_node.to_dict() if self.previous_node else None,
        }

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __gt__(self, other):
        return self.total_cost > other.total_cost

    def __repr__(self):
        return f"Node({self.row}, {self.col}," \
               f" distance={self.distance}," \
               f" heuristic={self.heuristic}," \
               f" total_cost={self.total_cost})"
