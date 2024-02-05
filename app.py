from flask import Flask, request, jsonify
from algorithms.bfs import bfs
from utils import generate_board

app = Flask(__name__)


@app.route('/api/board', methods=['POST'])
def get_board():
    data = request.get_json()
    start = data.get('start')
    finish = data.get('finish')
    total_cols = data.get('totalCols')
    total_rows = data.get('totalRows')

    print(start, finish, total_cols, total_rows)

    board = generate_board(start, finish, total_cols, total_rows)

    return jsonify(board)


@app.route('/bfs')
def bfs_endpoint():
    data = request.get_json()
    nodes = data.get('nodes')
    start_node = data.get('startNode')
    end_node = data.get('endNode')

    res = bfs(nodes, start_node, end_node)

    return jsonify(res)


if __name__ == '__main__':
    app.run()
