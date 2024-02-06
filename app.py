from flask import Flask, request, jsonify
from algorithms.bfs import bfs
from utils import generate_board
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/board', methods=['POST'])
def get_board():
    data = request.get_json()
    start = data.get('start')
    finish = data.get('finish')
    total_cols = data.get('totalCols')
    total_rows = data.get('totalRows')

    board = generate_board(start, finish, total_cols, total_rows)

    return jsonify(board)


@app.route('/api/bfs', methods=['POST'])
def bfs_endpoint():
    data = request.get_json()
    nodes = data.get('nodes')
    start_node = data.get('startNode')
    end_node = data.get('endNode')

    print(start_node, end_node)

    res = bfs(nodes, start_node, end_node)

    print(res)

    return jsonify(res)


if __name__ == '__main__':
    app.run()
