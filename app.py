import json
import platform
import logging
import os

from flask import Flask, jsonify
from flask import request

import language_processor as lp

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "config.json"
abs_file_path = os.path.join(script_dir, rel_path)
with open(abs_file_path) as json_data_file:
    CONFIG = dict(json.load(json_data_file))

app = Flask(__name__)
PORT = 6789

@app.route('/')
def index():
    return '<h1>My handsome natural language parser!</h1>'

@app.route('/api')
def api():
    peer = request.args.get('peer')
    msg = request.args.get('msg')
    token = request.args.get('token')
    return jsonify({ 'answer': lp.get_answer(peer, msg) })

if __name__ == '__main__':
    app.run(debug=True,port=PORT)