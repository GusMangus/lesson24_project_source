import os

from utils import get_query
from flask import Flask, request, abort, jsonify, Response
from typing import Optional, Union, List

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Response:
    cmd1: Optional[str] = request.args.get('cmd1')
    val1: Optional[str] = request.args.get('val1')
    cmd2: Optional[str] = request.args.get('cmd2')
    val2: Optional[str] = request.args.get('val2')
    file_name: Optional[str] = request.args.get('file_name')

    if not (cmd1 and val1 and file_name):
        abort(400, 'Проверьте данные')

    file_path: str = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400, 'Файл не найден')

    with open(file_path, 'r', encoding='utf-8') as file:
        result: Union[str, List] = get_query(cmd1, val1, file)
        if cmd2 and val2:
            result = get_query(cmd2, val2, result)
        return jsonify(result)
    return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)