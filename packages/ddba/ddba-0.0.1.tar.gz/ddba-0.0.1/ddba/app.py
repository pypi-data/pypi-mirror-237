import json
import os
import logging

import openai
from flask import Flask, request, Response, render_template, jsonify
from flask_cors import CORS

from ddba.core import functions, available_functions

logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)


app = Flask(__name__,
            static_folder='frontend', static_url_path='/',
            template_folder='frontend')
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/chat/completions', methods=['POST'])
def chat_completions():
    req = request.json
    print(req)
    stream = req.get('stream')
    if stream:

        def iter_resp():
            for chunk in openai.ChatCompletion.create(
                    model=req.get('model'),
                    messages=req.get('messages'),
                    functions=functions,
                    function_call="auto",  # auto is default, but we'll be explicit
                    stream=True,
            ):
                yield "data: " + json.dumps(chunk.to_dict()) + '\n\n'

        return Response(iter_resp(), mimetype='text/event-stream')

    resp = openai.ChatCompletion.create(
        model=req.get('model'),
        messages=req.get('messages'),
        # functions=req.get('functions'),
        # function_call="auto",  # auto is default, but we'll be explicit
        stream=False,
    )
    return jsonify(resp.to_dict())


@app.route('/api/v1/exec_func', methods=['POST'])
def exec_func():
    req = request.json
    name = req.get('name')
    arguments = req.get('arguments')

    args = json.loads(arguments)
    fn = available_functions[name]
    resp = fn(**args)

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
