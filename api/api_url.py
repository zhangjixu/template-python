from api import app
from flask import request
import json


@app.route("/get", methods=["GET"])
def get():
    """
    get 请求参数解析
    Returns:

    """
    name = request.args.get("name")
    return "get 请求 " + name


@app.route("/post", methods=["POST"])
def post():
    """
    post 请求解析 json 参数格式
    Returns:

    """
    json_data = json.loads(request.get_data(as_text=True))
    name = json_data["name"]
    return "post 请求 " + name
