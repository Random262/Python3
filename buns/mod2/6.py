from flask import Flask
import os

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:file_path>')
def preview(size, file_path):
    path = os.path.abspath(file_path)
    with open(path, 'r') as file:
        text = file.read(size)
        res_size = len(text)
    return f'<b>{path}</b> {res_size}<br>{text}'


if __name__ == "__main__":
    app.run(debug=True)