from flask import Flask, request, jsonify
import logging
from logging.handlers import HTTPHandler

app = Flask(__name__)

app.config['DEBUG'] = True

handler = HTTPHandler(host='127.0.0.1:3000', url='/log', method='POST')

logger = logging.getLogger('logs')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


@app.route('/log', methods=['POST'])
def log():
    log_text = f'{request.form.get("levelname", "")} | {request.form.get("name", "")} | {request.form.get("asctime", "")} | {request.form.get("message", "")}'
    print(log_text)
    if request.form.get("message", ""):
        with open('flask_logs.txt', 'a') as f:
            f.write(log_text + '\n')
    return 'OK', 200


@app.route('/logs', methods=['GET'])
def logs():
    with open('flask_logs.txt', 'r') as f:
        lines = f.readlines()
    last = lines[-10:]
    return jsonify(last), 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)