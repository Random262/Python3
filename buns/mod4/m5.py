import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def ps():
    res_args = request.args.getlist('arg')
    user_cmd = ''.join(res_args)
    clean_user_cmd = shlex.quote(user_cmd)
    result = subprocess.run(['ps', clean_user_cmd], capture_output=True, text=True)
    return f"<pre>{result.stdout}<pre>"


if __name__ == '__main__':
    app.run(debug=True)
